from aromtool.contact import Contact
from aromtool.ring import Ring
from aromtool.utils.math.mathutil import MathUtil
from aromtool.calculator import EnergyCalculator
from ase import Atoms

# Define the mol2 ring from ligand
mol2_symbols = ['C', 'C', 'H', 'C', 'C', 'H', 'C', 'H', 'C']
mol2_positions = [[106.876,17.424,97.544 ],
                 [106.793,18.503,98.487 ],
                 [106.7001,19.5244,98.1359],
                 [106.833,18.229,99.892 ],
                 [106.932,16.93,100.366 ],
                 [106.9508,16.7397,101.433 ],
                 [107.008,15.86,99.456 ],
                 [107.0763,14.8482,99.8391],
                 [106.998,16.065, 98.05  ]]
mol2_ring = Ring(mol2_symbols, mol2_positions)

# Define the pdb ring from protein
pdb_symbols = ['C', 'C', 'C', 'C', 'C', 'C', 'H', 'H', 'H', 'H', 'H']
pdb_positions = [[113.145,  17.914,  98.484],
                 [110.935,  17.201,  99.075],
                 [112.897,  17.569,  97.134],
                 [110.677,  16.855,  97.747],
                 [112.17 ,  17.738,  99.455],
                 [111.669,  17.044,  96.772],
                 [114.115,  18.324,  98.765],
                 [110.162,  17.05 ,  99.828],
                 [113.671,  17.716,  96.381],
                 [109.709,  16.44 ,  97.468],
                 [111.473,  16.778,  95.733]]
pdb_ring = Ring(pdb_symbols, pdb_positions)

# Build contact
contact = Contact( mol2_ring, pdb_ring)
print('Dihedral angle:\n', contact.angle)
print('Distance:\n', contact.distance)

# Determine whether there is aromatic stacking interaction or not. Output the results if there is aromatic stacking interaction.
iscontact = MathUtil.isContact(mol2_ring.centroid,pdb_ring.centroid)
if iscontact[1]:
    print('Dihedral angle:\n', contact.angle)
    print('Distance:\n', contact.distance)
	# Combine data from ligand and protein
    symbols1 = mol2_symbols + pdb_symbols
    positions1 = mol2_positions + pdb_positions
    atoms_contact = Atoms(symbols1,positions1)

    # Build Ring
    atoms_ring = Ring(atoms_contact.symbols, atoms_contact.positions)
    print('Centroid: \n', atoms_ring.centroid)
    print('Normal vector:\n', atoms_ring.normal_vector)

    # Select predictive model
    pinn = ('AromNN-PiBPTT.pb')

    # Define the calculator
    energy_calculator = EnergyCalculator(pinn)

    # Access the energy
    energy = energy_calculator.get_energy(atoms_contact)
    print('Energy: ')
    print(energy)
else:
    print('no aromatic stacking interaction')

#----------------------------------------------------------------------
from aromtool.contact import Contact
from aromtool.builder import ContactBuilder
from ase.io import write,read
from aromtool.ring import Ring
from aromtool.calculator import EnergyCalculator

mol2path = r'7std_ligand.mol2'
pdbpath = r'7std_protein.pdb'

# Access the list of aromatic stacking interaction
builder=ContactBuilder(mol2path, pdbpath)
contacts=builder.get_contacts()
print('Aromatic stacking interaction:')
print(contacts)

# Access the number of aromatic stacking interaction
contact_numbers=len(contacts)
print('Number of aromatic stacking interaction:')
print(contact_numbers)

# Access the first aromatic stacking interaction, define as contact0
contact0=contacts[0]
print('the first aromatic stacking interaction:')
print(contact0)

# Access the dihedral angle of contact0
angle=contact0.angle
print('Dihedral angle:')
print(angle)

# Access the distance of contact0
distance=contact0.distance
print('Distance: ')
print(distance)

# Access the contact type(Ben-Phe, Ben-Tyr or Ben-Trp) of contact0
print('Contact type: ')
print(contact0.contact_type)

# Access the PDB code of contact0
print('PDB code:')
print(contact0.pdb_code)

# Export the xyz file
builder.to_xyz('./')

# Get xyz file
xyz_contact = read('./contact/7std_contact_3.xyz')

# Build ring
ring = Ring(xyz_contact.symbols, xyz_contact.positions)

print('Centroid:\n', ring.centroid)
print('Normal vector:\n', ring.normal_vector)

# Select predictive model
pinn = ('AromNN-PiBPTT.pb')

# Define the calculator
energy_calculator = EnergyCalculator(pinn)

# Access energy of the aromatic stacking interaction
energy = energy_calculator.get_energy(xyz_contact)
print('Energy: ')
print(energy)

# Separate ligand and protein
mol2_symbols = xyz_contact.symbols[:12]
pdb_symbols = xyz_contact.symbols[12:]
mol2_positions = xyz_contact.positions[:12]
pdb_positions = xyz_contact.positions[12:]

# Build ring of ligand and protein respectively
mol2_ring = Ring(mol2_symbols, mol2_positions)
pdb_ring = Ring(pdb_symbols, pdb_positions)

# Build contact
contact = Contact( mol2_ring, pdb_ring)

print('Dihedral angle:\n', contact.angle)
print('Distance:\n', contact.distance)
