'''This module defines Ring class which combines Atoms class from ASE.'''

from ase.atoms import Atoms
import numpy as np

from aromtool.utils.math.vertor import Vector
from aromtool.utils.atom.atomutil import Atomutil


class Ring:

    def __init__(self, symbols, positions):
        self._atoms = Atoms(symbols, positions)
        self.elements=self._atoms.get_chemical_symbols()
        self.positions=self._atoms.positions
        self.centroid = self._get_centroid()
        self._normal_vector = self._get_normal_vector()

    def __add__(self, ring):
        """A magic method to add two rings."""
        if type(ring) == type(self):
            symbols = self._atoms.get_chemical_symbols() + ring.atoms.get_chemical_symbols()
            positions = np.concatenate((self._atoms.positions, ring.atoms.positions), axis=0)
            return Atoms(symbols, positions)
        else:
            raise TypeError

    def _get_centroid(self):
        """Get centroid."""
        positions = self._removeH()
        atom_number = len(positions)
        atom_sum = np.sum(positions, axis=0)
        return Vector(atom_sum[0] / atom_number, atom_sum[1] / atom_number, atom_sum[2] / atom_number)

    def _removeH(self):
        """Remove Hydrogen."""
        symbols = self._atoms.symbols
        positions = self._atoms.positions
        filler_pos = []
        for i, symbol in enumerate(symbols):
            if symbol.lower() == 'h':
                continue
            filler_pos.append(positions[i])
        return filler_pos

    @property
    def centroid(self):
        return self._centroid

    @centroid.setter
    def centroid(self, value):
        self._centroid = value

    @property
    def atoms(self):
        return self._atoms

    @property
    def normal_vector(self):
        """Get normal vector of the ring."""
        return self._normal_vector

    @normal_vector.setter
    def normal_vector(self, value):
        """Set normal vector value."""
        self._normal_vector = value

    @property
    def ring_type(self):
        """Get ring type."""
        return self._ring_type

    @ring_type.setter
    def ring_type(self, value):
        """Set ring type."""
        self._ring_type = value

    @property
    def residue_type(self):
        """Get residue type like PHE, TYR, TRP."""
        return self._residue_type

    @residue_type.setter
    def residue_type(self, value):
        """Set residue type."""
        self._residue_type = value

    def _vector3D(self, a, b):
        vector = [a[0] - b[0], a[1] - b[1], a[2] - b[2]]
        return vector

    def _get_normal_vector(self):
        """Get normal vector."""
        positions = self._atoms.get_positions()
        a1 = self._vector3D(positions[0], positions[1])
        a2 = self._vector3D(positions[0], positions[2])
        x1,y1,z1=a1[0],a1[1],a1[2]
        x2,y2,z2=a2[0],a2[1],a2[2]
        normal_vector=[y1*z2-y2*z1,z1*x2-z2*x1,x1*y2-x2*y1]
        #normal_vector = np.multiply(np.array(a2), np.array(a1))
        #normal_vector = normal_vector.tolist()
        return Vector(normal_vector[0], normal_vector[1], normal_vector[2])

    def update(self, symbols, positions):
        """Update ring data."""
        self._atoms = Atoms(symbols, positions)
        self.centroid = self._get_centroid()
        self._normal_vector = self._get_normal_vector()

    def to_atom_list(self):
        """Ring instance to list format in form of [c,[x,yz]]."""
        atom_list = []
        symbols = self._atoms.symbols
        for index, atom in enumerate(symbols):
            pos = self._atoms.positions[index]
            atom_list.append([atom, pos])
        return atom_list

    def get_xyz(self):
        """Get strings for xyz file."""
        atom_list = self.to_atom_list()
        atom_str = ''
        atom_str += str(len(atom_list)) + '\n\n'
        atom_str += Atomutil.atom_list_tostring(atom_list) + "\n"
        return atom_str

    def to_xyz(self, save_path):
        """Output ring information to xyz file."""
        xyz_str = self.get_xyz()
        with open(save_path, 'w') as file:
            file.write(xyz_str)

from collections import Counter
def get_ligand_ring_type(ligand_ring:Ring):

    ligand_ring_type=None
    ele_dict=Counter(ligand_ring.elements)
    if len(ele_dict)<=2 and ele_dict['C']==6:
        ligand_ring_type='benzene'
    elif len(ele_dict)<=2 and ele_dict['C']>6:
        ligand_ring_type='carbocycle'
    elif len(ele_dict)>=2 and ele_dict['C']<6:
        ligand_ring_type = 'heterocycle'

    return ligand_ring_type




