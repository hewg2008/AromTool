# 1. Introduction

**AromTool** is a Python based program for analyzing aromatic interactions between ligands (mostly drugs, or other material monomers) and receptors (mostly proteins, or other material monomers). With the help of the popular open source computational physio-chemistry libraries, such as ASE, OpenBabel, RDKit, Kekule, etc., and the internally integrated aromatic contact energy calculator based on neural network model as the back-end calculation tool, it can:
  
1 recognize, filter, transform, extract, construct and manipulate aromatic rings in ligand (mol2 format) and receptor (PDB format) files.

2 determine whether the aromatic ring between ligand and receptor has contact, construct and operate the aromatic contact, and output the contact conformation file in XYZ format.

3 output aromatic contact type, geometry (including contact distance and angle) and energy report (Excel format).   

**AromTool** is mainly designed for pharmaceutical  scientists to implement aromatic stacking analysis, build aromatic contact data sets and generate aromatic stacking analysis reports.

AromTool has the following design objectives:

1 Simple and easy to use. It can be used through command line tools and python scripts. For novice programmers (especially researchers in the field of materialization), python scripts are easy to understand (unlike C + +, Java and other languages with high learning costs), and it is very simple to use various functions of aromtool. All the tasks of aromtool are done through python.

2 Automatic integration of batch processing function. Unlike other physical chemistry programs such as MOE, Schrodinger and RDKit, users need to write batch code again.

3 Open source code is convenient for customization and extension. The code is based on the object-oriented Python style, and the core class is based on the numpy array (ndarray). It is convenient to integrate into all the Python code, and can easily expand the class or module. For example, calculators can customize other energy calculators.

# 2. Installation    
  **AromTool** can be installed locally by downloading the entire package. Currently only supports **Windows** system. 
  
## Dependencies

python                    3.7.6   
tensorflow                1.13.1  
scikit-learn              0.23.2  
scipy                     1.5.4  
numpy                     1.18.1    
pandas                    1.1.5   
xlwt                      1.3.0  
ase                       3.20.0   
openbabel                 2.4.1    
rdkit                     2019.09.3     
pyexecjs                  1.5.1    
sqlite                    3.30.1     

# 3. Usage

Description Below  displays how to use AromTool. All related scripts and data files are in director of 'example'.

## Build Ring
 
The basic object of AromTool is the Ring object. Combined with Atoms object from ASE, the Ring object not only remains the attributes and methods of Atoms object like collection of each atoms, but it also includes the attributes of centroid, normal vector, PDB codes and contact type, as well as methods about conversion of data's structure and so on. 

### Build Ring from Data

Two parameters are needed in order to build ring from data - symbols(atoms' elements) and positions(coordinate of atoms).
```python
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
```

### Build Ring from File
Build ring from file and assessing information about the ring.

#### From mol2 File
```python
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
```

Results:
```python
the list of ring objects:
[<aromtool.ring.Ring object at 0x0000000010F3AAC8>]
the number of rings:
1
the first ring:
<aromtool.ring.Ring object at 0x0000000010F3AAC8>
element: 
['C', 'C', 'H', 'C', 'H', 'C', 'C', 'H', 'C', 'H']
coordinate: 
[[30.937   8.868  35.491 ]
 [30.985   9.313  34.198 ]
 [31.463   8.7096 33.4348]
 [30.43   10.519  33.868 ]
 [30.4725 10.862  32.8406]
 [29.828  11.292  34.804 ]
 [29.769  10.823  36.093 ]
 [29.27   11.4144 36.8521]
 [30.329   9.622  36.437 ]
 [30.2858  9.2759 37.4634]]
```
#### Build Ring from PDB File
```python  
from aromtool.builder import Builder

pdbpath = r'7std_protein.pdb'

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

```

Results:
```python
the list of ring objects:
[<aromtool.ring.Ring object at 0x00000000120A13C8>, <aromtool.ring.Ring object at 0x00000000120A3C48>, <aromtool.ring.Ring object at 0x00000000120A3E08>, <aromtool.ring.Ring object at 0x00000000120A3FC8>, <aromtool.ring.Ring object at 0x00000000120A61C8>, <aromtool.ring.Ring object at 0x00000000120A63C8>, <aromtool.ring.Ring object at 0x00000000120A6588>, <aromtool.ring.Ring object at 0x00000000120A6748>, <aromtool.ring.Ring object at 0x00000000120A6908>, <aromtool.ring.Ring object at 0x00000000120A6388>, <aromtool.ring.Ring object at 0x00000000120A6C48>, <aromtool.ring.Ring object at 0x00000000120A6E08>, <aromtool.ring.Ring object at 0x00000000120A6FC8>, <aromtool.ring.Ring object at 0x00000000120AB1C8>, <aromtool.ring.Ring object at 0x00000000120AB388>, <aromtool.ring.Ring object at 0x00000000120AB548>, <aromtool.ring.Ring object at 0x00000000120AB708>, <aromtool.ring.Ring object at 0x00000000120AB8C8>, <aromtool.ring.Ring object at 0x00000000120ABA88>, <aromtool.ring.Ring object at 0x00000000120ABC48>, <aromtool.ring.Ring object at 0x00000000120ABE08>, <aromtool.ring.Ring object at 0x00000000120ABFC8>, <aromtool.ring.Ring object at 0x00000000120B11C8>, <aromtool.ring.Ring object at 0x00000000120B1388>, <aromtool.ring.Ring object at 0x00000000120B1548>, <aromtool.ring.Ring object at 0x00000000120B1708>, <aromtool.ring.Ring object at 0x00000000120B18C8>, <aromtool.ring.Ring object at 0x00000000120B1A88>, <aromtool.ring.Ring object at 0x00000000120B1C48>, <aromtool.ring.Ring object at 0x00000000120B1E08>, <aromtool.ring.Ring object at 0x00000000120B1FC8>, <aromtool.ring.Ring object at 0x00000000120B61C8>, <aromtool.ring.Ring object at 0x00000000120B6388>, <aromtool.ring.Ring object at 0x00000000120B6548>, <aromtool.ring.Ring object at 0x00000000120B6708>, <aromtool.ring.Ring object at 0x00000000120B68C8>, <aromtool.ring.Ring object at 0x00000000120B6A88>, <aromtool.ring.Ring object at 0x00000000120B6C48>, <aromtool.ring.Ring object at 0x00000000120B6E08>, <aromtool.ring.Ring object at 0x00000000120B6FC8>, <aromtool.ring.Ring object at 0x00000000120BC1C8>, <aromtool.ring.Ring object at 0x00000000120BC388>, <aromtool.ring.Ring object at 0x00000000120BC548>, <aromtool.ring.Ring object at 0x00000000120BC708>, <aromtool.ring.Ring object at 0x00000000120BC8C8>, <aromtool.ring.Ring object at 0x00000000120BCA88>, <aromtool.ring.Ring object at 0x00000000120BCC48>, <aromtool.ring.Ring object at 0x00000000120BCE08>, <aromtool.ring.Ring object at 0x00000000120BCFC8>, <aromtool.ring.Ring object at 0x00000000120C21C8>, <aromtool.ring.Ring object at 0x00000000120C2388>, <aromtool.ring.Ring object at 0x00000000120C2548>, <aromtool.ring.Ring object at 0x00000000120C2708>, <aromtool.ring.Ring object at 0x00000000120C28C8>, <aromtool.ring.Ring object at 0x00000000120C2A88>, <aromtool.ring.Ring object at 0x00000000120C2C48>, <aromtool.ring.Ring object at 0x00000000120C2E08>, <aromtool.ring.Ring object at 0x00000000120C2FC8>, <aromtool.ring.Ring object at 0x00000000120C81C8>, <aromtool.ring.Ring object at 0x00000000120C8388>, <aromtool.ring.Ring object at 0x00000000120C8548>, <aromtool.ring.Ring object at 0x00000000120C8708>, <aromtool.ring.Ring object at 0x00000000120C88C8>, <aromtool.ring.Ring object at 0x00000000120C8A88>, <aromtool.ring.Ring object at 0x00000000120C8C48>, <aromtool.ring.Ring object at 0x00000000120C8E08>, <aromtool.ring.Ring object at 0x00000000120C8FC8>, <aromtool.ring.Ring object at 0x00000000120CD1C8>, <aromtool.ring.Ring object at 0x00000000120CD388>]
the number of rings:
69
the first ring:
<aromtool.ring.Ring object at 0x00000000120A13C8>
elements: 
['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'H', 'H', 'H', 'H', 'H', 'H', 'N']
coordinate: 
[[25.3   19.741 37.075]
 [24.444 19.885 35.014]
 [24.758 18.534 35.275]
 [23.884 20.231 33.774]
 [24.81  20.638 36.186]
 [23.99  17.886 33.129]
 [24.538 17.525 34.342]
 [23.662 19.231 32.839]
 [25.664 19.987 38.073]
 [25.592 17.607 37.017]
 [23.628 21.267 33.55 ]
 [23.806 17.118 32.378]
 [24.79  16.487 34.562]
 [23.23  19.484 31.871]
 [25.272 18.473 36.537]]
centroid: 
24.517555555555557,19.127111111111113,34.90788888888889
normal vector: 
-2.7468270000000055,-0.4237380000000033,1.1112400000000038

```

## Build Contact
---
   
Contact object is the main object of AromTool. It contains entries to the geometry information(distance, dihedral angle) and energy of aromatic stacking interaction. Besides, Contact object contains PDB codes and the attribute of rings from ligand(TODO) or protein.

### Build Contact From Coordinates and Elements
To directly build contact , 2 ring objects needed.  
After building contact, the values of centroid and normal vector can be accessed from attribute. The following codes show how to build contact and then access contacts' information.

```python
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
```

Results:
```python
Dihedral angle:
 105.10978137419309
Distance:
 5.08591544529266
Dihedral angle:
 105.10978137419309
Distance:
 5.08591544529266
Centroid: 
 109.41108333333335,17.277666666666665,98.5385
Normal vector:
 -1.3420170999999852,-0.11674599999999846,0.015462900000001917
Energy: 
-1.2557073816289344

```
Noticeably, no information about contact type and PDB code provided.

### Build Contact From File
To build contact, two ring objects are required. In this way, the ring objects are built from source files. For example, in PDBbind dataset, the source files are mol2 file(ligand) and pdb file(protein) respectively.
After building contact, the values of centroid and normal vector can be accessed. The following codes show how to build and access contact.

```python
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

```

Result:
```python
Aromatic stacking interaction:
[<aromtool.contact.Contact object at 0x00000000120A1C88>, <aromtool.contact.Contact object at 0x00000000120A1CC8>, <aromtool.contact.Contact object at 0x00000000120A1308>, <aromtool.contact.Contact object at 0x00000000120A1388>, <aromtool.contact.Contact object at 0x00000000120A14C8>]
Number of aromatic stacking interaction:
5
the first aromatic stacking interaction:
<aromtool.contact.Contact object at 0x00000000120A1C88>
Dihedral angle:
54.85164826612596
Distance: 
7.937098904608785
Contact type: 
ligand-TYR
PDB code:
7std
Centroid:
 29.014547731366488,8.083097986013163,33.9761719264379
Normal vector:
 1.137826539285975,0.5890535484905051,0.2523573790994627
Energy: 
-1.402616054196005
Dihedral angle:
 96.70880737455842
Distance:
 5.367289369585858

```


##  Energy Calculation

Calculate the energy from a contact file via calling a trained model. More models in the director of data\predictive_model)
```python
from aromtool.calculator import EnergyCalculator
from ase.io import read

# Access the coordinate data from ring file.
xyz_contact = read(r'.\contact\7std_contact_4.xyz')

# Choose a model(More models in the director of data\predictive_model)
pinn = ('AromNN-PiBPTT.pb') 

# Define a calculator
energy_calculator = EnergyCalculator(pinn)

# Access the energy
energy = energy_calculator.get_energy(xyz_contact)
print('energy: ')
print(energy)
```

Results:
```python
energy: 
-2.6499349970290718
```

## Export Report

Information about the name, contact type, contact distance, contact angle and energy are included in the report.
```python
from aromtool.builder import BatchBuilder
from aromtool.calculator import EnergyCalculator
from aromtool.reporter import ReportManager

# access the stacking interaction from refined set of PDBBind
# Define the directory of input files.
src_dataset = r'.\dataset'
# Define the directory of output xyz files
dst_dataset = r'.\dataset\AS'
# Define the report's path
reportPath = r'.\dataset\report.xlsx'
# Define calculator
energycalculator = 'AromNN-PiBPTT.pb'

# Put the above variables to BatchBuilder
batchbuilder = BatchBuilder.build_dataset(src_dataset, dst_dataset, reportPath, energycalculator)

# Exportation of report
ReportManager.export(reportPath, batchbuilder)
```

Results(tail of flow shown):
```python
Parsing file 7std ... 8/8
2021-04-27 14:53:04,604 BatchBuilder INFO 7std has contact(s). 
-0.04566741800124969
-0.542801764886686
-1.402616054196005
-2.6499349970290718
-0.4476579656594951
Batch contact building is completed!
Report building is completed!
```
the tail of the report that we export is shown here:
[![g9TPsg.md.png](https://z3.ax1x.com/2021/04/27/g9TPsg.md.png)](https://imgtu.com/i/g9TPsg)

# 4. Questions and Issues
If you have any questions and issues, please do not hesitate to send me email directly: hewg3@mail2.sysu.edu.cn / wenganhe@icloud.com.




