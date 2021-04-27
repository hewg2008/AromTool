from aromtool.ring import Ring
symbols = ['C', 'C', 'H', 'C', 'C', 'H', 'C', 'H', 'C']
positions = [[106.876,17.424,97.544 ],
             [106.793,18.503,98.487 ],
             [106.7001,19.5244,98.1359],
             [106.833,18.229,99.892 ],
             [106.932,16.93,100.366 ],
             [106.9508,16.7397,101.433 ],
             [107.008,15.86,99.456 ],
             [107.0763,14.8482,99.8391],
             [106.998,16.065, 98.05  ]]
ring = Ring(symbols, positions)
print(ring)
#------------------------------------------------------------------------------------
from aromtool.builder import Builder

mol2path = r'7std_ligand.mol2'

# Generate the list of ring objects
rings=Builder.get_mol2_rings(mol2path, only_ch=False)
print('the list of ring objects:')
print(rings)

# Print the number of rings
ring_numbers=len(rings)
print('the number of rings:')
print(ring_numbers)

# the first ring
ring=rings[0]
print('the first ring:')
print(ring)

# the element of the first ring
elements=ring.elements
print('element: ')
print(elements)

# coordinate:
positions=ring.positions
print('coordinate: ')
print(positions)

#------------------------------------------------------------

from aromtool.builder import Builder

pdbpath = r'7std_protein.pdb'

# Generate the list of ring objects
rings=Builder.get_pdb_rings(pdbpath,filters=['PHE', 'TYR', 'TRP'])

print('the list of ring objects:')
print(rings)

# the number of rings:
ring_numbers=len(rings)
print('the number of rings:')
print(ring_numbers)

# the first ring
ring=rings[0]
print('the first ring:')
print(ring)

# the element of the first ring
elements=ring.elements
print('elements: ')
print(elements)

# coordinate:
positions=ring.positions
print('coordinate: ')
print(positions)

#centroid:
centroid=ring.centroid
print('centroid: ')
print(centroid)

#Print the normal vector:
normal_vector=ring.normal_vector
print('normal vector: ')
print(normal_vector)