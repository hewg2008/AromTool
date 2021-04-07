# RDKit 获取芳香环的原子信息

from rdkit import Chem
from rdkit.Chem.Lipinski import NumAromaticRings
import numpy as np

# 读取mol2文件，返回整个分子（mol对象）
# mol = Chem.MolFromMol2File(r'E:\datasets\pdbbind\test_all\phe-filter\1a52\1a52_ligand.mol2')
# print('分子对象：')
# print(mol)

# 返回分子的芳香环总数
# rings = NumAromaticRings(mol)
# print('环的总数')
# print(rings)

# 通过调用Mol对象的GetAromaticAtoms()方法获取环的所有芳香原子（这里是一个原子序列对象）
# atomseq = mol.GetAromaticAtoms()
# print('芳香原子序列对象：')
# print(atomseq)

# 通过一个for循环遍历获取芳香环原子的原子索引
# atom_index_list=[]
# for i in range(0, atomseq.__len__()):
#     atom=atomseq.__getitem__(i)
#     atom_index_list.append(atom.GetIdx())
# print('芳香原子索引列表： ')
# print(atom_index_list)

# 获取环原子信息
# symbol_list=[]
# for index in atom_index_list:
#     atom=mol.GetAtomWithIdx(index)
#     symbol_list.append(atom.GetSymbol())
# print('环的元素： ')
# print(symbol_list)

# 通过链式调用Mol对象的GetConformer().GetAtomPosition()获取原子的坐标位置
# atom_position_list=[]
# for index in atom_index_list:
#     atom_position=mol.GetConformer().GetAtomPosition(index)
#     atom_position_list.append([atom_position[0], atom_position[1],atom_position[2]])
# print('环的原子坐标： ')
# print(np.array(atom_position_list))



# 通过Mol对象的GetAtomWithIdx()方法获取相应原子序号的Atom对象。
# atom_list=[]
# for index in atom_index_list:
#     atom=mol.GetAtomWithIdx(index)
#     atom_list.append(atom)
# print(atom_list)

# 构建分子指纹
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import MACCSkeys
from rdkit.Chem import DataStructs

# 构建Mol对象
mol = Chem.MolFromSmiles('CCCN')
mol2 = Chem.MolFromSmiles('CCCO')

# 生成MACCS分子指纹
fp1 = MACCSkeys.GenMACCSKeys(mol)
print(fp1)
print (len(fp1.ToBitString()))
fp1_morgan = AllChem.GetMorganFingerprint(mol,2)
print(fp1_morgan)
print (fp1_morgan.GetLength())

fp1_morgan_hashed = AllChem.GetMorganFingerprintAsBitVect(mol,2,nBits=1024)
fp1_morgan_hashed_bit=fp1_morgan_hashed.ToBitString()
print(fp1_morgan_hashed_bit)

fp2 = MACCSkeys.GenMACCSKeys(mol2)
print (fp2.ToBitString())

fp2_morgan = AllChem.GetMorganFingerprint(mol2,2)
print (fp2_morgan.GetLength())
fp2_morgan_hashed = AllChem.GetMorganFingerprintAsBitVect(mol2,2,nBits=1024)
a=fp2_morgan_hashed.ToBitString()
print(a)
print('len a: ', len(a))

similarity1=DataStructs.FingerprintSimilarity(fp1,fp2)
print(similarity1)

similarity2=DataStructs.FingerprintSimilarity(fp1_morgan_hashed,fp2_morgan_hashed)
print(similarity2)





















































