import logging
import os
import re
import pybel

from aromtool.io.file import File
from aromtool.utils.atom.atomutil import Atomutil
from rdkit import Chem
from rdkit.Chem.rdMolAlign import AlignMol


def convert_file_via_ob(infile, informat, outfile, outformat):
    """
         Convert files in regular chemical formats via openbabel, generate a new file in 'outformat' style.

         Parameters:
         infile: str
             Path of infile
         informat: str
             File format type
         outfile: str
             Path of outfile
         outformat: str
             Path of outfile
         Returns:
             None
    """

    mols = pybel.readfile(informat, infile)
    out = open(outfile, 'w')
    for mol in mols:
        out.writelines(mol.write(outformat) + '\n')
    out.close()


def readxyzfile(path):
    alldata = []
    rel = [] #接触的关系，ligand-PHE 等关系
    with open(path, 'r') as f:
        content = f.read()
        array = re.split('Contact number:\d', content)
        for item in array:
            if item != '':
                xyzbody,body_type = getxyzbody(item)
                if len(xyzbody) > 0:
                    alldata.append(xyzbody)
                    rel = rel+body_type
                else:
                    logging.info('PDB Code: {}, contains no contact'.format(path))
    return alldata,rel


def getxyzbody(content):
        contact = content.split('\n')
        atom_list = []
        index = -1
        body_type = [];
        for line in contact:
            if line == '':
                continue
            if line.isdigit():
                atom_list.append([int(line), []])
                index +=1
            else:
                if line.find('ligand_ring') == -1 and line.find('Protein_ring') == -1 and line.find('Contact number') == -1:
                    atom = line.split()
                    atom[0] = atom[0][0:1]  # 处理原子，取第一个字母
                    atom_list[index][1].append([atom[0],[atom[1],atom[2],atom[3]]])
                else:
                    if line.find('Protein_ring') != -1:
                       body_type.append(line.split(':')[1])
                    if line.find('ligand_ring') != -1:
                        body_type.append('ligand')

        return atom_list,body_type





# 生成对应的环xyz文件
def buildxyz(filePath, f, alldata):
    # print('生成对应的环xyz文件')
    floders = os.path.join(filePath, f,'ring_utils')
    if not os.path.exists(floders):
        os.makedirs(floders)
    ring_paths = []
    for r_index,rings in enumerate(alldata):
        for index, ring in enumerate(rings):
            atom_str = ''
            atom_str += str(ring[0])+'\n\n'
            atom_str += Atomutil.atom_list_tostring(ring[1])+"\n"
            global  save_path
            if index == 0:
                save_path = os.path.join(floders, f+'_ligand_ring'+str(r_index+1)+'.xyz')
                ring_paths.append(save_path)
            else:
                save_path = os.path.join(floders, f+'_protein_ring'+str(r_index+1)+'.xyz')
                ring_paths.append(save_path)
            with open(save_path,'w') as file:
              file.write(atom_str)

    return ring_paths

def add_hydrogen(infile, format, outfile):
        """
             Add hydrogen to molecule.

             Parameters:
             infile: str
                 Path of infile
             format: str
                 File format type
             outfile: str
                 Path of outfile

             Returns:
                 None
        """

        mols = pybel.readfile(format, infile)
        out = open(outfile, 'w')
        for mol in mols:
            mol.addh()
            out.writelines(mol.write(format) + '\n')
        out.close()


#将xyz文件转换mol格式，喂给rdkit使用
def xyz2mol(ring_paths):
    # print('批量转换mol文件')
    for xyz_path in ring_paths:
        newfile = xyz_path.replace('.xyz','.mol2')
        convert_file_via_ob(xyz_path,'xyz',newfile,'mol2')


def to_add_hydrogen(ring_paths):
    for xyz_path in ring_paths:
        mol2_path = xyz_path.replace('.xyz', '.mol2')
        new_mol2_path = mol2_path.replace('.mol2', 'h_.mol2')
        add_hydrogen(mol2_path, 'mol2', new_mol2_path)



def get_atoms_positions(mol):
    atoms = []
    for i in range(0, mol.GetNumAtoms()):
        atom = mol.GetAtomWithIdx(i)
        symbol = atom.GetSymbol()
        pos = mol.GetConformer().GetAtomPosition(i)
        atoms.append([symbol,[pos[0],pos[1],pos[2]]])
    return atoms


# 生成参考后的xyz文件,原子数
def write_xyz_file(save_path,atom_list):
    # print('生成参考后的xyz文件')
    atom_str = ''
    atom_str += str(len(atom_list)) + '\n\n'
    atom_str += Atomutil.atom_list_tostring(atom_list,format="{0:8}{1:<26}{2:<26}{3:<26}\n") + "\n"
    with open(save_path, 'w') as file:
        file.write(atom_str)


# 修正到参考坐标
def replaceAtoms(ring_paths,body_type,root_path):
    # print('替换参考的文件坐标')

    refpath = {"ligand": 'lib/data/reference/ref_Ben_ligand.mol2', "phe":'lib/data/reference/ref_Phe.mol2',
                  'trp': 'lib/data/reference/ref_Trp.mol2', 'tyr': 'lib/data/reference/ref_Tyr.mol2'}

    for index, xyz_path in enumerate(ring_paths):
        type = body_type[index].lower()
        system_path = os.path.join(root_path, refpath[type]) # 获取对应的模型路径进行替换
        ref = Chem.MolFromMol2File(system_path, sanitize=False)
        ref = Chem.AddHs(ref, explicitOnly=False, addCoords=True)

        mol_path = xyz_path.replace('.xyz', 'h_.mol2')
        probe = Chem.MolFromMol2File(mol_path, sanitize=False)
        probe = Chem.AddHs(probe, explicitOnly=False, addCoords=True)

        AlignMol(ref, probe)
        atom_list = get_atoms_positions(ref)
        if xyz_path.find('ligand_ring') != -1 :
           save_path = xyz_path.replace('ligand_ring', 'ligand_ring_stand')
           write_xyz_file(save_path, atom_list)
        else:
           save_path = xyz_path.replace('protein_ring', 'protein_ring_stand')
           write_xyz_file(save_path, atom_list)


# 合并2个xyz文件
def mergeAtoms(ring_paths):
    print('合并2个xyz文件')
    ligand_list = []
    for xyz_path in ring_paths:
        if xyz_path.find('ligand_ring') !=-1:
            ligand_list.append(xyz_path)
    files = []
    for xyz_path in ligand_list:
        ligand_ring_path = xyz_path.replace('ligand_ring', 'ligand_ring_stand')
        protein_ring_path = xyz_path.replace('ligand_ring', 'protein_ring_stand')
        atom_listA = readxyz(ligand_ring_path)
        atom_listB = readxyz(protein_ring_path)

        atom_listC = atom_listA + atom_listB
        save_path = xyz_path.replace('ligand_ring', 'contact_ring_stand')
        write_xyz_file(save_path,atom_listC)
        #合并内容
        files.append(os.path.basename(save_path))
    return  files


#读取xyz 返回原子列
def readxyz(filename):
  print('读取xyz')
  with open(filename,'r') as f:
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







def split_ring(filePath,root_path):

    floders = File.getDir(filePath)
    t = 0
    for f in floders:
        t += 1
        print("拆分文件夹" + f + "数据: " + str(t) + '/' + str(len(floders)))
        contact_path = os.path.join(filePath, f, f + "_contact.xyz")
        alldata,rel = readxyzfile(contact_path)
        # print(alldata)
        if len(alldata) >= 1:
           ring_paths = buildxyz(filePath,f,alldata)
           xyz2mol(ring_paths)
           to_add_hydrogen(ring_paths)
           replaceAtoms(ring_paths,rel,root_path)
           files = mergeAtoms(ring_paths)
           config_path = os.path.join(filePath, f, f+'_contact.config')
           new_list = files
           with open(config_path,'w') as f:
                f.write('\n'.join(new_list))


