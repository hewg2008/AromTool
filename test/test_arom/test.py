
from aromtool.builder import ContactBuilder, EnergyCalculator, BatchBuilder
from aromtool.reporter import ReportManager
import pybel
from aromtool.utils.ring.filter_ring import getAromaticAtomInfoOfMolList
from aromtool.io.file import File
from aromtool.utils.atom.atomutil import Atomutil
from aromtool.configs.protein_configs import amino_acid_table
from aromtool.ring import Ring
mol2path = '1a52_ligand.mol2'
pdbpath = '1a52_protein.pdb'

'''
def simpleTest():
    mol2path = r'G:\pyabs\labs\dist\refined_phe\1ai4\1ai4_ligand.mol2'
    pdbpath = r'G:\pyabs\labs\dist\refined_phe\1ai4\1ai4_protein.pdb'

    savepath = r'G:\pyabs\labs\dist\contact'
    excelpath = r'G:\pyabs\labs\dist\contact\all.xlsx'
    energyCalculator = EnergyCalculator('./lib/data/piNN/pi_below_0_4000.pb')
    builder = ContactBuilder(mol2path, pdbpath, '1ai4')
    builder.to_xyz(savepath)
    builder.setEnergy(energyCalculator)
    # 报表导出
    ReportManager.export(excelpath, [builder])


'''

def batchTest():
    energyCalculator = EnergyCalculator('pi_below_0_4000.pb')
    #批量处理
    srcPath = r"E:\datasets\pdbbind\test"
    totalPath = r'E:\datasets\pdbbind\testout'
    excelpath = r'E:\datasets\pdbbind\testout\all.xlsx'
    allbuilder = BatchBuilder.build_batch(srcPath, totalPath, ['PHE', 'TYR', 'TRP'], energyCalculator)
    # 批量导出报表
    ReportManager.export(excelpath, allbuilder)


# batchTest()



# from aromtool.builder import Builder
# filter=['PHE', 'TYR', 'TRP']
# rings=Builder.get_pdb_rings(pdbpath, filter)
# rings=Builder.get_mol2_rings(mol2path)
# print(rings)
# print(rings[0])
# # 获取环的数目
# ring_numbers=len(rings)
# print(ring_numbers)
# # 获取第一个环的元素种类
# elements=rings[0].elements
# print(elements)
# # 获取第一个环的所有原子坐标
# positions=rings[0].positions
# print(positions)
# print(rings[0].normal_vector)


# from aromtool.builder_parallel import ContactBuilder, BatchBuilder
from aromtool.builder import ContactBuilder, BatchBuilder
from aromtool.calculator import  EnergyCalculator

# 假设用户希望从PDBBind的refined set数据集中构建芳香接触的数据集。
src_dataset= r"E:\paper\thesis\application\16wj\f2f\after\16wj" #源数据集路径。
dst_dataset= r'E:\paper\thesis\application\16wj\f2f\after\aromatic_set' # 目标数据集路径。
reportPath = r'E:\paper\thesis\application\16wj\f2f\after\report.xlsx' # 报表输出路径
# energyCalculator = EnergyCalculator('pi_below_0_4000.pb') # 能量计算器对象。

# 批量构建并生成芳香接触数据集。
# batchbuilder = BatchBuilder.build_dataset(src_dataset, dst_dataset,reportPath,'pi_below_0_4000.pb',['PHE'], threshold=6.0)

# 生成芳香接触数据集汇总报表。
# ReportManager.export(reportPath, batchbuilder)



# 构建16wj_md_all_5000

src_dataset= r"E:\paper\thesis\application\16wj\md_all_5000\after\test2\16wj" #源数据集路径。
dst_dataset= r'E:\paper\thesis\application\16wj\md_all_5000\after\test2\aromatic_set' # 目标数据集路径。
reportPath = r'E:\paper\thesis\application\16wj\md_all_5000\after\test2\report.xlsx' # 报表输出路径
energyCalculator = EnergyCalculator('pi_below_0_4000.pb') # 能量计算器对象。

# 批量构建并生成芳香接触数据集。
import time
start = time.time()
# batchbuilder = BatchBuilder.build_dataset(src_dataset, dst_dataset,reportPath,'pi_below_0_4000.pb',['PHE'], threshold=6.0)
# batchbuilder = BatchBuilder.build_fast_batch(src_dataset, dst_dataset,['PHE'],energyCalculator, threshold=6.0)
end = time.time()
# print('文件处理结束，用时：{}'.format(end - start))

# new intiate face to face

src_dataset= r"E:\paper\thesis\application\16wj\f2f\new\after\16wj" #源数据集路径。
dst_dataset= r'E:\paper\thesis\application\16wj\f2f\new\after\aromatic_set' # 目标数据集路径。
reportPath = r'E:\paper\thesis\application\16wj\f2f\new\after\report.xlsx' # 报表输出路径
energyCalculator = EnergyCalculator('pi_below_0_4000.pb') # 能量计算器对象。

# 批量构建并生成芳香接触数据集。
import time
start = time.time()
batchbuilder = BatchBuilder.build_dataset(src_dataset, dst_dataset,reportPath,'pi_below_0_4000.pb',['PHE','TYR', 'TRP'], threshold=6.0)
# batchbuilder = BatchBuilder.build_fast_batch(src_dataset, dst_dataset,['PHE'],energyCalculator, threshold=6.0)
end = time.time()
print('文件处理结束，用时：{}'.format(end - start))