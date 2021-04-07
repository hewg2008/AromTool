
from ase.io import read
from ase.io import write
import pybel


# 读取mol的数据
def read_mol():
  atom = read('1a0q_ligand.mol')
  print(atom.symbols)
  print(atom.positions)


# 格式转换：例如 mol2  格式为 mol的数据
def converto(infile, informat, outfile, outformat):
    mols = pybel.readfile(informat, infile)
    out = open(outfile, 'w')
    for mol in mols:
        out.writelines(mol.write(outformat) + '\n')
    out.close()



def write_xyz():
    atom = read('1a0q_ligand.mol')
    write("1a0q.xyz", atom)
    #write("1a0q_ligand.gif", atom,interval=500)


def merger():
    atomA = read('1a0q_ligand.mol')
    converto('1ai4_ligand.mol2', 'mol2', '1ai4_ligand.mol', 'mol')
    atomB = read('1ai4_ligand.mol')
    atomC = atomA + atomB
    write("1a0q.xyz", atomC)


# converto('1a0q_ligand.mol2', 'mol2', '1a0q.mol', 'mol')
# read_mol()
# write_xyz()
merger()



