'''
任务：将目录下的文件进行改名，根据文件名构建子目录，并将文件放入相应子目录
输入：目录：extracted_ligs，包含N个ligand文件。extracted_pros:包含N个protein文件。其中每一个ligand文件和protein文件是对应的。
输出：目录：N个子目录，子目录名为ligand文件或protein文件的前缀的第一个字符和序号，比如16wj_ligand_1.mol2文件
      对应的子目录名为：1001, 每个子目录包含一个ligand文件，一个protein文件,
      文件命名为：ligand文件:子目录名+'_ligand'+'.mol2', 比如1001_ligand.mol2。
                 protein文件:子目录名+'_protein'+'.pdb'。比如1001_protein.pdb。

实例：
输入：
E:.
│  filetree.txt
│
└─16wj
    ├─extracted_ligs
    │      16wj_ligand_1.mol2
    │      16wj_ligand_2.mol2
    │      16wj_ligand_3.mol2
    │      16wj_ligand_4.mol2
    │
    └─extracted_pros
            16wj_protein_1.pdb
            16wj_protein_2.pdb
            16wj_protein_3.pdb
            16wj_protein_4.pdb

输出：
│  filetree.txt
│
└─16wj
    ├─1001
    │      1001_ligand.mol2
    │      1001_protein.pdb
    │
    ├─1002
    │      1002_ligand.mol2
    │      1002_protein.pdb
    │
    ├─1003
    │      1003_ligand.mol2
    │      1003_protein.pdb
    │
    └─1004
            1004_ligand.mol2
            1004_protein.pdb

'''

import os, shutil, re, time


def change_filename(srcdir):
    '''更改文件名'''
    files_generator = os.walk(srcdir)
    for root, dirs, files in files_generator:
        for file in files:
            prefix, number, subfix = file.split('.')[0], file.split('.')[2], file.split('.')[1]
            new_name = prefix + '_' + number + '.' + subfix
            old_name=os.path.join(root, file)
            new_name=os.path.join(root, new_name)
            os.rename(old_name, new_name)


import os, shutil, re, time


# 获取子目录名字和路径列表
def get_subdir(in_path):
    dirs = os.listdir(in_path)
    subdir_list = []  # 子目录名字列表
    sub_path_list = []  # 子目录路径列表
    for subdir in dirs:
        dir_path = os.path.join(in_path,subdir)
        subdir_list.append(subdir)
        sub_path_list.append(dir_path)
    return subdir_list, sub_path_list


def get_file_path(in_path):
    # 遍历输入目录和子目录，获取输入目录下所有子文件夹路径和文件路径
    if not os.path.exists(in_path):
        print('输入目录不存在！')
    file_path_list = []  # 文件路径列表
    # in_dir_list = []  # 所有子文件夹路径
    # 遍历所有文件夹
    for root, dirs, files in os.walk(in_path):
        # print(root, 'root\n')  # 当前遍历的文件夹路径
        # print(dirs, 'dirs\n')  # dirs是一个list，是当前文件夹中所有目录的名字（不包括子目录）
        # print(files, 'files\n')  # 也是一个list，当前文件夹所有文件（不包括子目录）
        for file in files:
            # print(file)
            file_path = os.path.join(root, file)
            file_path_list.append(file_path)
        # for dir in dirs:
        #     in_dir = os.path.join(root, dir)
        #     in_dir_list.append(in_dir)
        # print(file_path_list)
    return file_path_list


# 创建文件夹
def build_dir(path):
    print('first subdir', path)
    if not os.path.exists(path):
        os.mkdir(path)


# 创建输出目录的第一层子文件夹
def build_out_path_subdir(out_path, subdir_list):
    for subdir in subdir_list:
        sub_path = os.path.join(out_path, subdir)
        build_dir(sub_path)


# 构建分类目录并对文件进行分类拷贝到分类目录
def build_sort_dir_and_sort_file(subdir_list, in_path, out_path):
    for subdir in subdir_list:
        sub_path = os.path.join(in_path, subdir)  # 输入子目录路径
        out_sub_path = os.path.join(out_path, subdir)  # 输出子目录路径
        file_path_list = get_file_path(sub_path)  # 获取输入目录下所有子文件夹路径和文件路径
        for file_path in file_path_list:
            # file_path_, file_name = os.path.split(file_path)
            file_name = os.path.split(file_path)[1].split('.')[0]  # 不包括后缀的文件名
            # file_name_num = re.findall(r'_\d', file_path)[0]
            new_subdir_name = re.sub(r'_.*_', '_', file_name)  # 根据文件名构建分类目录名
            # new_subdir_name = subdir + file_name_num
            out_path_last_sub_path = os.path.join(out_sub_path, new_subdir_name)
            # if file_path.count(subdir) > 1:  # 文件路径包含输出子目录名字符串超过一个判断为属于子目录这一类，防止混入其他类
            if subdir in file_name:  # 判断文件名是否为子目录类
                build_dir(out_path_last_sub_path)  # 创建子目录下的分类目录，如16wj_1目录
                shutil.copy(file_path, out_path_last_sub_path)  # 复制文件到对应分类目录


# 构建分类目录并对文件进行分类拷贝到分类目录，2
def build_sort_dir_and_sort_file2(subdir_list, in_path, out_path):
    for subdir in subdir_list:
        # print('subdir ', subdir)
        sub_path = os.path.join(in_path, subdir)  # 输入子目录路径
        out_sub_path = os.path.join(out_path, subdir)  # 输出子目录路径
        file_path_list = get_file_path(sub_path)  # 获取输入目录下所有子文件夹路径
        for file_path in file_path_list:
            file_name, file_suffix = os.path.split(file_path)[1].split('.')  # 文件名和后缀
            # print(file_name)
            sort, species, num = re.findall(r'(.*)_(.*)_(.*)', file_name)[0]  # 分类名，种类，序号
            print(sort, species, num)
            if int(num)<1000:
                new_subdir_name = str(1000+int(num)).replace('1', '0', 1) # 分类目录名
                print(new_subdir_name)
                new_file_name = new_subdir_name + '_' + species + '.' + file_suffix  # 新文件名
                out_path_last_sub_path = os.path.join(out_sub_path, new_subdir_name)  # 分类目录路径
                new_file_path = os.path.join(out_path_last_sub_path, new_file_name)  # 新文件路径
                # print(new_file_path)
            else:
                # print('num now',num)
                new_subdir_name = str(num)  # 分类目录名
                new_file_name = str(num) + '_' + species + '.' + file_suffix  # 新文件名
                out_path_last_sub_path = os.path.join(out_sub_path, new_subdir_name)  # 分类目录路径
                new_file_path = os.path.join(out_path_last_sub_path, new_file_name)  # 新文件路径
                # print(new_file_path)
            if subdir in file_name:  # 判断文件名是否为子目录类
                build_dir(out_path_last_sub_path)  # 创建子目录下的分类目录，如1001目录
                shutil.copy(file_path, new_file_path)  # 复制文件到对应分类目录，同时修改为新文件名


def main(in_path, out_path):
    build_dir(out_path)  # 创建输出根目录
    subdir_list, sub_path_list = get_subdir(in_path)  # 获取输入根目录下的子目录名称，返回列表
    build_out_path_subdir(out_path, subdir_list)  # 创建输出根目录下子目录
    build_sort_dir_and_sort_file2(subdir_list, in_path, out_path)  # 构建分类目录并对文件进行分类拷贝到分类目录


if __name__ == '__main__':
    # 启动程序
    start = time.time()
    IN_PATH = r'E:\paper\thesis\application\16wj\f2f\new\before'  # 输入目录
    OUT_PATH = r'E:\paper\thesis\application\16wj\f2f\new\after'  # 输出目录
    main(IN_PATH, OUT_PATH)
    end = time.time()
    print('文件处理结束，用时：{}'.format(end - start))
