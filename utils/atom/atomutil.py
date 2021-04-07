from aromtool.io.file import File
from aromtool.configs.protein_configs import amino_acid_table


class Atomutil:

    #  Parse atom information from pdb file.
    @staticmethod
    def parse_atom(atom):
        # ATOM    426  N   PHE A  27      24.836  51.701  57.730  1.00 12.77           N
        recod_name = atom[0:6].strip()
        serial = atom[6:11].strip()
        name = atom[12:16].strip()
        # altLoc = atom[17:17].strip()
        resName = atom[17:20].strip()
        # chainID = atom[21:22].strip()
        resSeq = atom[22:26].strip()
        iCode = atom[27:27].strip()
        x = atom[30:38].strip()
        y = atom[38:46].strip()
        z = atom[46:54].strip()
        occupancy = atom[54:60].strip()
        tempFactor = atom[60:66].strip()
        element = atom[76:78].strip()
        charge = atom[78:80].strip()
        atom_items=[recod_name,serial,name,resName,resSeq,iCode,x,y,z,occupancy,tempFactor,element,charge]
        return atom_items



    # 氨基酸字符串
    @staticmethod
    def get_amino_acid_str(atom_list):
        amino_str = ''
        atom_list.sort()
        for atom in atom_list:
            name = atom[0]
            amino_str += name

        return amino_str


    # 生成指定的氨基酸
    # atom_list  原子列表
    # amino_acid 格式如['c','H','C1'...] 等
    @staticmethod
    def generate_amino_acid(atom_list, amino_acid):

        amino_acid_group = [] #氨基酸组
        i = 0
        atom_num = len(amino_acid)
        amino_acid_group.append([])
        for index, atom in enumerate(atom_list):
            name = atom[0]
            if name in amino_acid:
                amino_acid_group[i].append(atom)

            if len(amino_acid_group[i]) == atom_num:
                i += 1
                amino_acid_group.append([])

        amino_acids = []
        amino_acid.sort()
        amino_acid_str = ''.join(amino_acid)
        # 匹配原子组，进行过滤
        for index, one_amino_acid in enumerate(amino_acid_group):
            if len(one_amino_acid) == 0:
                continue

            one_amino_acid.sort()
            if Atomutil.get_amino_acid_str(one_amino_acid) == amino_acid_str:
                amino_acids.append(one_amino_acid)

        return amino_acids


    # 获取氨基酸的名称
    @staticmethod
    def get_amino_acid_name(an_table, atom_list):
         name = ''
         amino_acid_str = Atomutil.get_amino_acid_str(atom_list)

         for key,item in an_table.items():
             item['ring'].sort()
             if amino_acid_str == ''.join(item['ring']):
                 return key
         return  name



    # 原子结构，字符串表示转换
    @staticmethod
    def atom_tostring(atom,format=None):
        atom_str = ''
        if format == None:
           atom_str += "{0:8}{1:<16}{2:<16}{3:<16}\n".format(atom[0], str(atom[1][0]), str(atom[1][1]),
                                                                   str(atom[1][2]))
        else:
            atom_str += format.format(atom[0], str(atom[1][0]), str(atom[1][1]),
                                                              str(atom[1][2]))
        return atom_str


    # 原子列表，在字符串转换
    @staticmethod
    def atom_list_tostring(atom_list,format = None):
        atom_list_str = ''
        for atom in atom_list:
            atom_list_str += Atomutil.atom_tostring(atom,format)
        return atom_list_str


    @staticmethod
    def find(atom_list, index):
        for i, item in enumerate(atom_list):
            if item[2] == index:
                return item

        return False

    @staticmethod
    def find_bone_data(atom, boneData, ar_atom_list, atom_list):
        for b in boneData:
            bone_data = b.split()
            if bone_data[1] == atom[2]:  # 判断他的索引是不是相同
                ar_item = Atomutil.find(ar_atom_list, bone_data[1])  # 判断在不在列表里面
                if ar_item == False:
                    atom_item = Atomutil.find(atom_list, bone_data[1])  # 继续找
                    if atom_item and atom_item[4] == 'H':
                        ar_atom_list.append(atom_item)
                        return True
                else:
                    return True
        return False

    @staticmethod
    def split_list(alist, keystr):
      """
             Split list by a marked string

             Parameters:

             alist: list
                 element in list should be list in the form of ['C', [0.0, 0.0, 0.0] if atom is C atom.
             keystr: str
                 A string to mark the element position where to split.
             Returns:
             rings_list: dict
                key is ring_utils number, value is ring_utils atom list.
              """

      index_list=Atomutil.find_index(alist, keystr)
      rings_list=locals()
      for i in range(1, len(index_list)):
            rings_list['ring0']=alist[0:index_list[0]]
            rings_list['ring_utils' + str(i)] = alist[index_list[i-1]:index_list[i]]
            rings_list['ring_utils' + str(i+1)]=alist[index_list[i]:]
      return rings_list


    @staticmethod
    def find_index(alist, keystr):
        """
                    Find index list for a marked string

                    Parameters:

                    alist: list
                        element in list should be list in the form of ['C', [0.0, 0.0, 0.0] if atom is C atom.
                    keystr: str
                        A string to mark the element position where to split.
                    Returns:
                    rings_list: list
                       Indices of the keystr.
                     """
        index_list = []
        for index, item in enumerate(alist):
            if item[0] == keystr:
                index_list.append(index)
        return index_list