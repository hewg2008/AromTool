'''This module defines Builder related classes for building up rings and contacts.'''

import os
import shutil

import pybel
from ase import Atoms
from ase.db import connect
from rdkit import Chem
from rdkit.Chem.rdMolAlign import AlignMol

from aromtool.io.file import File
from aromtool.utils.atom.atomutil import Atomutil
from aromtool.configs.protein_configs import amino_acid_table
from aromtool.utils.ring.filter_ring import getAromaticAtomInfoOfMolList
from aromtool.utils.math.mathutil import MathUtil
from aromtool.utils.path.path import Path
from aromtool.ring import Ring
from aromtool.contact import Contact
from aromtool.calculator import EnergyCalculator
from aromtool.log.debug import Logger
from aromtool.reporter import ReportManager


__all__ = ['BuilderUtil', 'Builder', 'RingBuilder', 'ContactBuilder', 'BatchBuilder']


class BuilderUtil:
    '''This class provides static utility functions for building.'''

    @staticmethod
    def convert(infile, informat, outfile, outformat):
        '''Convert files among different file formats'''
        mols = pybel.readfile(informat, infile)
        out = open(outfile, 'w')
        for mol in mols:
            out.writelines(mol.write(outformat) + '\n')
        out.close()

    @staticmethod
    def xyz2mol(ring_paths):
        '''Converter xyz format file to mol2 format file.'''
        for xyz_path in ring_paths:
            newfile = xyz_path.replace('.xyz', '.mol2')
            BuilderUtil.convert(xyz_path, 'xyz', newfile, 'mol2')

    @staticmethod
    def _add_hydrogen(infile, format, outfile):
        mols = pybel.readfile(format, infile)
        out = open(outfile, 'w')
        for mol in mols:
            mol.addh()
            out.writelines(mol.write(format) + '\n')
        out.close()

    @staticmethod
    def add_hydrogen(ring_paths):
        '''Add hydrogen to ring file in mol2 format.'''
        for xyz_path in ring_paths:
            mol2_path = xyz_path.replace('.xyz', '.mol2')
            new_mol2_path = mol2_path.replace('.mol2', '_h.mol2')
            BuilderUtil._add_hydrogen(mol2_path, 'mol2', new_mol2_path)

    @staticmethod
    def get_atoms_positions(mol):
        '''Get atoms information via RDKit.'''
        atoms = []
        for i in range(0, mol.GetNumAtoms()):
            atom = mol.GetAtomWithIdx(i)
            symbol = atom.GetSymbol()
            pos = mol.GetConformer().GetAtomPosition(i)
            atoms.append([symbol, [pos[0], pos[1], pos[2]]])
        return atoms

    @staticmethod
    def write_xyz_file(save_path, atom_list):
        atom_str = ''
        atom_str += str(len(atom_list)) + '\n\n'
        atom_str += Atomutil.atom_list_tostring(atom_list, format="{0:8}{1:<26}{2:<26}{3:<26}\n") + "\n"
        with open(save_path, 'w') as file:
            file.write(atom_str)

    @staticmethod
    def replaceAtoms(ring_paths, residue_types):
        '''Replace raw ring with reference ring'''
        refpath = {"ligand": 'aromtool\\data\\reference\\ref_Ben_ligand.mol2', "phe": 'aromtool\\data\\reference\\ref_Phe.mol2',
                   'trp': 'aromtool\\data\\reference\\ref_Trp.mol2', 'tyr': 'aromtool\\data\\reference\\ref_Tyr.mol2'}
        root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

        for index, xyz_path in enumerate(ring_paths):
            type = residue_types[index].lower()
            system_path = os.path.join(root_path, refpath[type]) # 获取对应的模型路径进行替换
            ref = Chem.MolFromMol2File(system_path, sanitize=False)
            ref = Chem.AddHs(ref, explicitOnly=False, addCoords=True)

            mol_path = xyz_path.replace('.xyz', '_h.mol2')
            probe = Chem.MolFromMol2File(mol_path, sanitize=False)
            probe = Chem.AddHs(probe, explicitOnly=False, addCoords=True)

            AlignMol(ref, probe)
            atom_list = BuilderUtil.get_atoms_positions(ref)
            if xyz_path.find('ligand_raw_ring') != -1:
                save_path = xyz_path.replace('ligand_raw_ring', 'ligand_ring')
                BuilderUtil.write_xyz_file(save_path, atom_list)
            else:
                save_path = xyz_path.replace('protein_raw_ring', 'protein_ring')
                BuilderUtil.write_xyz_file(save_path, atom_list)

    @staticmethod
    def readxyz(filename):
        '''Read xyz file.'''
        with open(filename, 'r') as f:
            content = f.read()
            contact = content.split('\n')
            atom_list = []
            for line in contact:
                if line == '':
                    continue
                if line.isdigit():
                    continue
                else:
                    atom = line.split()
                    atom_list.append([atom[0], [atom[1], atom[2], atom[3]]])

            return atom_list

    @staticmethod
    def getAtoms(filename):
        '''Get atoms information in Atoms instance.'''
        with open(filename, 'r') as f:
            content = f.read()
            contact = content.split('\n')
            symbols = []
            positions = []
            for line in contact:
                if line == '':
                    continue
                if line.isdigit():
                    continue
                else:
                    atom = line.split()
                    symbols.append(atom[0])
                    positions.append([atom[1], atom[2], atom[3]])

            return Atoms(symbols, positions)

    @staticmethod
    def mergeAtoms(ring_paths, xyz_save_path):
        '''Merge rings to form contact conformation.'''
        ligand_list = []
        for xyz_path in ring_paths:
            if xyz_path.find('ligand_raw_ring') != -1:
                ligand_list.append(xyz_path)
        files = []
        for xyz_path in ligand_list:
            ligand_ring_path = xyz_path.replace('ligand_raw_ring', 'ligand_ring')
            protein_ring_path = xyz_path.replace('ligand_raw_ring', 'protein_ring')
            atom_listA = BuilderUtil.readxyz(ligand_ring_path)
            atom_listB = BuilderUtil.readxyz(protein_ring_path)

            atom_listC = atom_listA + atom_listB
            save_path = xyz_path.replace('ligand_raw_ring', 'contact')
            save_path = os.path.join(xyz_save_path, os.path.basename(save_path))
            BuilderUtil.write_xyz_file(save_path, atom_listC)
            # 合并内容
            files.append(save_path)
        return files

    @staticmethod
    def copy_target_file(from_files, to_path):
        """Copy files."""
        if not os.path.exists(to_path):
            os.makedirs(to_path)
        for f in from_files:
            shutil.copy(f, to_path)

class Builder:
    def __init__(self, file):
        self.file=file


    @staticmethod
    def get_mol2_rings(mol2_path, only_ch=True):
        '''Get ligand ring from mol2 file.'''
        mols = pybel.readfile('mol2', mol2_path)
        mol200str = ''
        for mol in mols:
            mol200str = mol.write('mol')
        mol2data = getAromaticAtomInfoOfMolList(mol200str)
        mol2_ring_list = []
        if mol2data:
            mol2_ring_list =Builder._to_molist(mol2data, only_ch=only_ch)
        return mol2_ring_list

    @staticmethod
    def _to_molist(mol2data, only_ch=True):
        ring_list = []
        for ringitem in mol2data:
            # ring = []
            symbols = []
            positions = []
            for atom in ringitem:
                if only_ch and (atom['symbol'].find('S') >= 0 or atom['symbol'].find('N') >= 0 or
                                atom['symbol'].find('P') >= 0 or atom['symbol'].find('O') >= 0 or
                                atom['symbol'].find('F') >= 0 or atom['symbol'].find('Cl') >= 0 or
                                atom['symbol'].find('Br') >= 0 or atom['symbol'].find('I') >= 0 or
                                atom['symbol'].find('Ru') >= 0):  # 不能包含[C，N，O，S，P，F，Cl，Br，I]原子，因为目前神经网络没有算好
                    symbols = []
                    positions = []
                    break
                symbols.append(atom['symbol'])
                positions.append([atom['coord']['x'], atom['coord']['y'], atom['coord']['z']])
                # ring.append([atom['symbol'], [atom['coord']['x'], atom['coord']['y'], atom['coord']['z']]])

            if len(positions) > 0:
                # 构建一个ring对象
                mol2_ring = Ring(symbols, positions)
                mol2_ring.residue_type = 'ligand'  # Currently ligand type only has value of 'ligand'.
                ring_list.append(mol2_ring)

        return ring_list


    @staticmethod
    def get_pdb_rings(protein_path, filters=['PHE', 'TYR', 'TRP']):
        '''Get protein ring from pdb file.'''
        allproteinFile = File.parse_pdb_data(protein_path)
        pdb_list = []
        # 过滤返回 pdb的环结构，原子列表
        for amino_acid_type in filters:
            atom_list = []
            pdb_list.append(atom_list)
            for f in allproteinFile:
                item = Atomutil.parse_atom(f)
                # print("type: " + item[3] + " x: " + item[6] + " y: " + item[7] + " z: " + item[8])
                if item[3] == amino_acid_type:
                    atom_list.append([item[2], [float(item[6]), float(item[7]), float(item[8])]])

        ring_list = []
        rings = []
        for amino_acid_type in filters:
            for atom_list in pdb_list:
                r = Atomutil.generate_amino_acid(atom_list, amino_acid_table[amino_acid_type]['ring'])  # 拆分多个环
                if len(r) > 0:
                    # 构建一个ring对象
                    rings = r + rings

        for ring_item in rings:
            symbols = [item[0][:1] for item in ring_item]
            positions = [item[1] for item in ring_item]
            pdb_ring = Ring(symbols, positions)
            pdb_ring.residue_type = Atomutil.get_amino_acid_name(amino_acid_table, ring_item)
            ring_list.append(pdb_ring)

        return ring_list

class RingBuilder(Builder):
    '''Build rings from mol2，pdb files.'''

    def __init__(self, mol2file=None, pdbfile=None, residue_types=['PHE', 'TYR', 'TRP']):
        self.pdb_code = os.path.basename(mol2file)[0:4]
        self.ligand_ring_list = self.get_mol2_rings(mol2file)
        self.protein_ring_list = self.get_pdb_rings(pdbfile, residue_types)
    def get_mol2_rings(self, mol2file):
        return self.get_mol2_rings(mol2file)
    def get_pdb_rings(self, pdbfile, residue_types):
        return self.get_pdb_rings(pdbfile, residue_types)

class ContactBuilder:
    '''Build contacts from mol2，pdb files.'''

    def __init__(self, mol2file, pdbfile, residue_types=['PHE', 'TYR', 'TRP'],threshold=8.0):
        self.pdb_code = os.path.basename(mol2file)[0:4]
        self.ligand_ring_list = Builder.get_mol2_rings(mol2file)
        self.protein_ring_list = Builder.get_pdb_rings(pdbfile, residue_types)
        self.contact_number = 0
        self.contacts = []
        if len(self.ligand_ring_list) > 0 and len(self.protein_ring_list) > 0:
            self.contacts = self.get_contacts(threshold=threshold)
            self.contact_number = len(self.contacts)

    def hasContact(self):
        if self.contact_number > 0:
            return True
        return False

    def get_contacts(self,threshold=8.0):
        '''Get contact list'''
        contacts_list = []
        for ligring in self.ligand_ring_list:
            for proring in self.protein_ring_list:
                distance, result = MathUtil.isContact(ligring.centroid, proring.centroid, threshold=threshold)
                if result:
                    contact = Contact(ligring, proring)
                    contact.distance = distance
                    contact.pdb_code = self.pdb_code
                    contact.angle = MathUtil.getAngle(ligring.normal_vector, proring.normal_vector)
                    contacts_list.append(contact)
        return contacts_list

    def to_xyz(self, save_path):
        """Generate xyz file with contact information."""
        ring_path = os.path.join(save_path, 'ring')
        contact_path = os.path.join(save_path, 'contact')
        if not os.path.exists(ring_path):
            os.makedirs(ring_path)

        if not os.path.exists(contact_path):
            os.makedirs(contact_path)

        # Generate xyz files with contacts.
        contacts_list = self.contacts
        ring_paths = []
        residue_types = []
        for index, contact in enumerate(contacts_list):
            mol_xyz_path = os.path.join(ring_path, '{0}_ligand_raw_ring_{1}.xyz'.format(contact.pdb_code, index + 1))
            pdb_xyz_path = os.path.join(ring_path, '{0}_protein_raw_ring_{1}.xyz'.format(contact.pdb_code, index + 1))
            ring_paths.append(mol_xyz_path)
            ring_paths.append(pdb_xyz_path)
            contact.mol_to_xyz(mol_xyz_path)
            contact.pdb_to_xyz(pdb_xyz_path)
            residue_types.append(contact.mol_ring.residue_type)
            residue_types.append(contact.pdb_ring.residue_type)

        # convert xyz file to mol2 file.
        BuilderUtil.xyz2mol(ring_paths)

        # Add hydrogen.
        BuilderUtil.add_hydrogen(ring_paths)

        # Replace raw ring with refernce ring.
        BuilderUtil.replaceAtoms(ring_paths, residue_types)

        # Merge and generate contact file in xyz format.
        xyzfiles = BuilderUtil.mergeAtoms(ring_paths, contact_path)
        self.xyzfiles = xyzfiles

        # Set raw contact values. C = A+B
        for index, contact in enumerate(contacts_list):
            xyz_path = xyzfiles[index]
            atoms = BuilderUtil.getAtoms(xyz_path)
            contact.set_raw_contact(atoms)

    def setEnergy(self, energyCalculator):
        """Set energy value via calling EnergyCalculator."""
        contacts_list = self.contacts
        for index, contact in enumerate(contacts_list):
            atoms = contact.get_raw_contact()
            contact.energy = energyCalculator.get_energy(atoms)
            print(contact.energy)

    def to_db(self, contacts, file):
        """Export to db file."""
        db = connect(file)
        result = False
        if contacts != None:
            result = True
            for contact in contacts:
                db = db.write(contact)
        return result

class BatchBuilder:

    @staticmethod
    def build_batch(data_src_path, result_path, residue_types, energyCalculator: EnergyCalculator, threshold=8.0):
        """Build in batch mode."""
        all_files = File.getDir(data_src_path)
        all_builders = []
        if not os.path.exists(result_path):
            os.makedirs(result_path)
        log_path = os.path.join(result_path, "info.log")
        # 日志设置
        logger = Logger.set_log(log_path, 'BatchBuilder')
        xyz_total_path = os.path.join(result_path, 'contact')

        if not os.path.exists(xyz_total_path):
            os.makedirs(xyz_total_path)

        t = 0
        xyz_files_list = []
        for f in all_files:
            mol2_path = Path.get_ligand_path(data_src_path, f)
            pdb_path = Path.get_protein_path(data_src_path, f)
            save_path = os.path.join(data_src_path, f)
            t += 1
            print("Parsing file " + f + " ... " + str(t) + '/' + str(len(all_files)))
            try:
                builder=ContactBuilder(mol2_path, pdb_path, residue_types, threshold=threshold)
                if builder.hasContact():
                    logger.info(f + ' has contact(s). ')
                    builder.to_xyz(save_path)
                    builder.setEnergy(energyCalculator)
                    all_builders.append(builder)
                    xyz_files_list += builder.xyzfiles
                else:
                    logger.info(f + ' has no contact. ')
            except Exception as e:
                logger.error(f + ' has Error: '+ str(e))

        # Copy files to a new folder.
        BuilderUtil.copy_target_file(xyz_files_list, xyz_total_path)
        return all_builders

    @staticmethod
    def build_dataset(indir, outdir, outexcel, calc, residue_types=['PHE', 'TYR', 'TRP'], threshold=8.0):

        energyCalculator = EnergyCalculator(calc)
        # 批量构建接触
        batches = BatchBuilder.build_batch(indir, outdir, residue_types, energyCalculator, threshold=threshold)
        print('Batch contact building is completed!')
        # 批量导出报表
        ReportManager.export(outexcel, batches)
        print('Report building is completed!')
