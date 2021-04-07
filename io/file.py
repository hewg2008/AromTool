'''Dealing io of file.'''

import os
import shutil


class File:

    @staticmethod
    def getDir(dir):
        """ 获取文件夹所有文件 """
        dirs = os.listdir(dir)
        dir_list = []
        for i in range(0, len(dirs)):
            path = os.path.join(dir, dirs[i])
            if os.path.isdir(path):
                dir_list.append(dirs[i])
        return dir_list

    @staticmethod
    def getAllFiles(dir, filelist):
        """ 递归获取所有的文件路径 """
        list_dir = os.listdir(dir)
        for f in list_dir:
            sub_dir = os.path.join(dir, f)
            if os.path.isdir(sub_dir):
                File.getAllFiles(sub_dir, filelist)
            else:
                filelist.append(f)

    @staticmethod
    def walk(path):
        """ 获取文件夹所有文件路径 """
        if not os.path.exists(path):
            return []
        files_paths = []
        for parent, dirnames, filenames in os.walk(path):
            for filename in filenames:
                files_paths.append(os.path.join(parent, filename))
        return files_paths

    @staticmethod
    def parse_mol2_data(path):
        """ Get mol2 atom information from pdb file '.
                        Parameters:
                        path: str
                            Path of the file.
                        Returns:
                            cont: list
                            Content of atom information in mol2 file
                """
        #print('Parsing mol2 file...')
        global mol2cont
        with open(path, 'r') as mol2file:
            while not mol2file.tell() == os.fstat(mol2file.fileno()).st_size:
                line = mol2file.readline()
                if line.startswith("@<TRIPOS>ATOM"):
                    mol2cont = []
                    line = mol2file.readline()
                    while not line.startswith("@<TRIPOS>BOND"):
                        mol2cont.append(line)
                        line = mol2file.readline()
                        if mol2file.tell() == os.fstat(mol2file.fileno()).st_size:
                            mol2cont.append(line)
                            break
                    mol2cont[-1] = mol2cont[-1].rstrip()  # removes blank line at file end
        return mol2cont

    @staticmethod
    def parse_bone_data(path):
        """ 解析Mo2bone文件数据 """
        # print('正在分析mo2文件')
        with open(path, 'r') as mol2file:
            while not mol2file.tell() == os.fstat(mol2file.fileno()).st_size:
                line = mol2file.readline()
                if line.startswith("@<TRIPOS>BOND"):
                    mol2cont = []
                    line = mol2file.readline()
                    while not line.startswith("@<TRIPOS>SUBSTRUCTURE"):
                        mol2cont.append(line)
                        line = mol2file.readline()
                        if mol2file.tell() == os.fstat(mol2file.fileno()).st_size:
                            mol2cont.append(line)
                            break
                    mol2cont[-1] = mol2cont[-1].rstrip()  # removes blank line at file end
                    return mol2cont

    @staticmethod
    def parse_pdb_data(path):
        """ Get protein atom information from pdb file '.
                Parameters:
                path: str
                    Path of the file.
                Returns:
                    cont: list
                    Content of atom information in pdb file
        """
        cont = []
        with open(path, 'r') as file:
            while not file.tell() == os.fstat(file.fileno()).st_size:
                line = file.readline()
                if line.startswith("ATOM"):
                    while line.startswith("ATOM"):
                        cont.append(line)
                        line = file.readline()
                        if file.tell() == os.fstat(file.fileno()).st_size:
                            cont.append(line)
                            break
                    cont[-1] = cont[-1].rstrip()
                    # yield "".join(mol2cont)
        return cont

    @staticmethod
    def writeFile(path, data):
        """ 生成文件 """
        with open(path, 'w') as out_file:
            out_file.write(data)
            out_file.write('\n')



    def writeString(path, data):
        """ 生成文件 """
        with open(path, 'w') as out_file:
            out_file.write(data)




    @staticmethod
    def copydir(src, dst, filter_dir=None):
        """ copy file '.
                   Parameters:
                   src: str
                   Path of the file.
                   dst: str
                   target Path of the file.
           """
        if filter_dir  != None and len(filter_dir) == 0:
            return

        if not os.path.exists(dst):
            os.makedirs(dst)


        if filter_dir:
            for d in filter_dir:
                source_path = os.path.join(src, d)
                for root, dirs, files in os.walk(source_path):
                    for file in files:
                        src_file = os.path.join(root, file)
                        target_file = os.path.join(dst, d)
                        if not os.path.exists(target_file):
                            os.makedirs(target_file)
                        shutil.copy(src_file, target_file)
        else:
            for filename in os.listdir(src):
                source_path = os.path.join(src, filename)
                for root, dirs, files in os.walk(source_path):
                    target_path = os.path.join(dst, filename)
                    if not os.path.exists(target_path):
                        os.makedirs(target_path)
                    for file in files:
                        src_file = os.path.join(root, file)
                        target_file = os.path.join(target_path, file)
                        shutil.copy(src_file, target_file)
