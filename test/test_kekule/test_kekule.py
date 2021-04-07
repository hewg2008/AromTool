import os
import numpy as np
import pybel
from aromtool.utils.ring.filter_ring import getAromaticAtomInfoOfMolList



# def getAllFiles(dir, filelist):
# 	""" 递归获取所有的文件路径 """
# 	list_dir = os.listdir(dir)
# 	for f in list_dir:
# 		sub_dir = os.path.join(dir, f)
# 		if os.path.isdir(sub_dir):
# 			getAllFiles(sub_dir)
# 		else:
# 			filelist.append(f)
# 	return filelist
#
def convert_file_via_ob(infile, informat, outformat):
    mols = pybel.readfile(informat, infile)
    for mol in mols:
        mol200str = mol.write(outformat)
        return mol200str

mol2path = '1a42_ligand.mol2'
pdbpath = '1a42_protein.pdb'

mol2str=convert_file_via_ob(mol2path, 'mol2', 'mol')
a=getAromaticAtomInfoOfMolList(mol2str)
print(len(a))
i=0
print(a)
print(type(a))
print(a[0][0])
for atom in a[0]:
    print(atom)
    i +=1
print(i)