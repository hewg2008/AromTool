import fire
import os

from aromtool.builder import ContactBuilder, EnergyCalculator, BatchBuilder
from aromtool.reporter import ReportManager
from aromtool.builder import Builder


def build_rings(file, format):
    filter=['PHE', 'TYR', 'TRP']
    if format=='mol2':
        rings = Builder.get_mol2_rings(file)
        for ring in rings:
            atom_list=ring.to_atom_list()
            print(atom_list)
    if format=='pdb':
        rings = Builder.get_pdb_rings(file, filter)
        for ring in rings:
            atom_list = ring.to_atom_list()
            print(atom_list)

def build_contacts(mol2path, pdbpath, savedir,excelpath):
    energyCalculator = EnergyCalculator('pi_below_0_4000.pb')
    pdb_code=os.path.basename(mol2path)[0:4]
    builder = ContactBuilder(mol2path, pdbpath, pdb_code)
    contacts=builder.get_contacts()
    print(contacts)
    builder.to_xyz(savedir)
    builder.setEnergy(energyCalculator)
    ReportManager.export(excelpath, [builder])


def build_dataset(indir, outdir, outexcel,residue_types=['PHE', 'TYR', 'TRP'],threshold=8.0):

    energyCalculator = EnergyCalculator('pinn_500k.pb')
    #批量构建接触
    batches = BatchBuilder.build_batch(indir, outdir, residue_types, energyCalculator, threshold=threshold)
    print('批量接触构建结束')
    #批量导出报表
    ReportManager.export(outexcel, batches)
    print('报表构建结束')

if __name__ == '__main__':
    # fire.Fire()



    indir=r"E:\datasets\pdbbind\refined_set"
    outdir=r'E:\datasets\pdbbind\refined_set_all_out'
    outxlsx=r'E:\datasets\pdbbind\refined_set_all_out\report.xlsx'
    residue_types=['PHE','TYR', 'TRP']
    build_dataset(indir, outdir, outxlsx, residue_types=residue_types, threshold=8)



# # from aromtool.builder import Builder
#
#
# pdbpath = '1a52_protein.pdb'
#
# # filter=['PHE', 'TYR', 'TRP']
# # rings=Builder.get_pdb_rings(pdbpath, filter)
#
# # mol2文件路径
# mol2path = '1a52_ligand.mol2'
#
# #构建环列表
# rings=Builder.get_mol2_rings(mol2path)
# print(rings)
# print(rings[0])
#
# # 获取环的数目
# ring_numbers=len(rings)
# print(ring_numbers)
# # 获取第一个环的元素种类
# elements=rings[0].elements
# print(elements)
# # 获取第一个环的所有原子坐标
# positions=rings[0].positions
# print(positions)
#
# #获取第一个环的质心
# centroid=rings[0].centroid
#
# #获取第一个环的法向量
# normal_vector=rings[0].normal_vector
# print(rings[0].normal_vector)

