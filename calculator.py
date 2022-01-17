'''This module defines a calculator class named PINN for calculating energy of contacts. and PINN is modified from TensorAlloy.
Citation:
Xin Chen, Xing-Yu Gao, Ya-Fan Zhao, De-Ye Lin, Wei-Dong Chu, Hai-Feng Song,
TensorAlloy: An automatic atomistic neural network program for alloys,
Computer Physics Communications,
Volume 250,
2020,
107057,
ISSN 0010-4655,
https://doi.org/10.1016/j.cpc.2019.107057.
'''

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
