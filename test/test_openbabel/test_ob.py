import pybel

def convert_file_via_ob(infile, informat, outfile, outformat):
    """
         Convert files in regular chemical formats via openbabel, generate a new file in 'outformat' style.

         Parameters:
         infile: str
             Path of infile
         informat: str
             File format type
         outfile: str
             Path of outfile
         outformat: str
             Path of outfile
         Returns:
             None
    """

    mols = pybel.readfile(informat, infile)
    out = open(outfile, 'w')
    for mol in mols:
        out.writelines(mol.write(outformat) + '\n')
    out.close()

# path1=r'E:\paper\thesis\application\mol2_from_cdf\extracted_ligs\16wj_ligand_1.pdb'
# path2=r'E:\paper\thesis\application\mol2_from_cdf\extracted_ligs\16wj_ligand_1.mol2'
# convert_file_via_ob(path1, 'pdb', path2, 'mol2')

# 转换ligand文件,pdb格式转为mol2格式。

import os
from aromtool.io.file import File

def change_filename(srcdir):
    '''更改文件名'''
    files_generator = os.walk(srcdir)
    for root, dirs, files in files_generator:
        for file in files:
            print(file)
            prefix, number, subfix = file.split('.')[0], file.split('.')[2], file.split('.')[1]
            # if 'ligand' in prefix:
            #     new_name = prefix + '_' + number + '.' + 'mol2'
            # else:
            new_name = prefix + '_' + number + '.' + 'pdb'
            old_name=os.path.join(root, file)
            new_name=os.path.join(root, new_name)
            os.rename(old_name, new_name)

def get_files(sourcedir):
    print(sourcedir)
    files_generator=os.walk(sourcedir)
    file_paths=[]
    for root, dirs, files in files_generator:
        for file in files:
            print(file)
            file_path=os.path.join(root, file)
            print(file_path)
            file_paths.append(file_path)
    return file_paths

def pdb_2_mol2(files):
    for file in files:
        pdb_fpath=file
        fname=os.path.basename(file)
        root_path=os.path.dirname(file)
        prefix=fname.split('.')[0]

        mol2_fname=prefix+'.mol2'
        mol2_fpath=os.path.join(root_path, mol2_fname)
        print(mol2_fpath)
        print(pdb_fpath)
        convert_file_via_ob(pdb_fpath, 'pdb', mol2_fpath, 'mol2')
        os.remove(file)
def rename_pdb(srcdir):
    files_generator = os.walk(srcdir)
    file_paths = []
    for root, dirs, files in files_generator:
        for file in files:
            print(file)
            file_path = os.path.join(root, file)
            print(file_path)

def build_dir(fpaths, ftype=None):
    for file in fpaths:
        dirname=os.path.dirname(file)
        old_fname=os.path.basename(file)
        if ftype =='mol2':
            fname=os.path.basename(file).split('.')[0][0:4]+'_'+os.path.basename(file).split('_')[-1][:-5]
        else:
            fname = os.path.basename(file).split('.')[0][0:4] + '_' + os.path.basename(file).split('_')[-1][:-4]
        sub_dirname=os.path.join(dirname, fname)
        print('sub_name', sub_dirname)
        if not os.path.exists(sub_dirname):
            os.mkdir(sub_dirname)
        new_file=os.path.join(sub_dirname, old_fname )
        os.rename(file, new_file)


def main(srcdir):

    # 获取配体文件路径
    files= get_files(srcdir) # 获取文件路径
    print(files)
    build_dir(files)
    # pdb_2_mol2(files) # 转换格式


if __name__ == '__main__':
    # lig_dir = r'E:\paper\thesis\application\16wj\f2f\16wj\extracted_ligs'
    # pro_dir = r'E:\paper\thesis\application\16wj\f2f\16wj\extracted_pros'
    #
    # change_filename(lig_dir)  # 更改配体文件名
    # files = get_files(lig_dir)
    # pdb_2_mol2(files)
    # change_filename(pro_dir) # 更改蛋白文件名

    # # 5000_1
    # lig_dir=r'E:\paper\thesis\application\16wj\md_all\5000_1\extracted_ligs'
    # change_filename(lig_dir)  # 更改配体文件名
    # files = get_files(lig_dir)
    # pdb_2_mol2(files)

    # md_all_5000
    # lig_dir=r'E:\paper\thesis\application\16wj\md_all_5000\before\16wj\extracted_ligs'
    # change_filename(lig_dir)  # 更改配体文件名
    # files = get_files(lig_dir)
    # pdb_2_mol2(files)

    # pro_dir=r'E:\paper\thesis\application\16wj\md_all_5000\before\16wj\extracted_pros'
    # change_filename(pro_dir)  # 更改蛋白文件名

    # new initiate face to face
    lig_dir=r'E:\paper\thesis\application\16wj\f2f\new\16wj\extracted_ligs'
    change_filename(lig_dir)  # 更改配体文件名
    files = get_files(lig_dir)
    pdb_2_mol2(files)

    pro_dir = r'E:\paper\thesis\application\16wj\f2f\new\16wj\extracted_pros'
    change_filename(pro_dir)  # 更




    # main(lig_dir)
    # main(pro_dir)
    # lig_files=File.getAllFiles(lig_dir)
    # pro_files=File.getAllFiles(pro_dir)
    # path=r'E:\paper\thesis\application\16wj'
    # subdirs=os.listdir(r'E:\paper\thesis\application\16wj')
    # for subdir in subdirs:
    #     for pro_file in pro_files:
    #         print(pro_file)
    #         print(subdir.split('/')[-1])
            # if subdir.split('/')[-1]==
    # for i in range(1,100):
    #     subdir='16wj'+'_'+str(i)
    #     subdir=os.path.join(path, subdir)
    #     os.mkdir(subdir)


# 利用OB将不规则的mol2文件转为规则的mol2文件。不规则mol2文件-> xyz文件 -> xyz文件原子种类进行清洗 ->转为规则mol2文件。