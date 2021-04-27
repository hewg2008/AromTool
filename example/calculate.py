from aromtool.calculator import EnergyCalculator
from ase.io import read

# Access the coordinate data from ring file.
xyz_contact = read(r'.\contact\7std_contact_4.xyz')

# Choose a model
pinn = ('AromNN-PiBPTT.pb')

# Define a calculator
energy_calculator = EnergyCalculator(pinn)

# Access the energy
energy = energy_calculator.get_energy(xyz_contact)
print('energy: ')
print(energy)