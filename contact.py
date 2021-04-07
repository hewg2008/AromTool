'''This module defines Contact class which requires two Ring objects.'''

from ase import Atoms

from aromtool.ring import Ring
from aromtool.utils.math.mathutil import MathUtil


class Contact:
    def __init__(self, mol_ring: Ring, pdb_ring: Ring , threshold = 6.0):
        self.mol_ring = mol_ring
        self.pdb_ring = pdb_ring
        self._contact_type = None
        self.angle = 0
        self.distance = 0
        self.init_data(threshold)

    def init_data(self, threshold):
        distance, result = MathUtil.isContact(self.mol_ring.centroid, self.pdb_ring.centroid, threshold)
        if result:
            self.distance = distance
            self.angle = MathUtil.getAngle(self.mol_ring.normal_vector, self.pdb_ring.normal_vector)
            # self.set_raw_contact = self.mol_ring + self.pdb_ring
            atoms = self.mol_ring + self.pdb_ring
            #self._raw_contact = atoms
            self.set_raw_contact(atoms)

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
        self._angle = value

    @property
    def contact_type(self):
        if not self._contact_type:
            return self.mol_ring.residue_type + '-' + self.pdb_ring.residue_type
        return self._contact_type

    @contact_type.setter
    def contact_type(self, value):
        self._contact_type = value

    @property
    def pdb_code(self):
        return self._pdbcode

    @pdb_code.setter
    def pdb_code(self, value):
        self._pdbcode = value

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        self.__energy = value

    def mol_to_xyz(self, save_path):
        self.mol_ring.to_xyz(save_path)

    def pdb_to_xyz(self, save_path):
        self.pdb_ring.to_xyz(save_path)

    def set_raw_contact(self, value: Atoms):
        """Set to generate a raw contact."""
        self._raw_contact = value

    def get_raw_contact(self) -> Atoms:
        """Get raw contact. """

        return self._raw_contact