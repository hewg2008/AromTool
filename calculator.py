'''This module defines a calculator class for calculating energy of contacts.'''

from aromtool.utils.pinn.calculator import PINN
from aromtool.contact import Contact


class EnergyCalculator:

    def __init__(self, pnn_path):
        self.calc = PINN(pnn_path)

    def get_energy(self, contact):
        energy_total = 0
        if isinstance(contact, Contact):
            contact.atoms.set_cell([20, 20, 20])
        else:
            contact.set_cell([20, 20, 20])
        energy = self.calc.get_potential_energy(contact)*627.509/27.211
        energy_total += energy
        return energy_total
