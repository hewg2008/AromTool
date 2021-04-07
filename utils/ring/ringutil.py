

# 环工具集
# 拆分2个环接触，输出单个文件
class RingUtil:

    #将接触拆分2个环分表输出
    @staticmethod
    def split_ring(contact_list):
      rings = []
      for atom_list in contact_list:
          ring_str = RingUtil.get_ring_str(atom_list)
          rings.append(ring_str)
      return rings


    @staticmethod
    def atom_tostring(atom):
        atom_str = ''
        atom_str += "{0:8}{1:<16.4f}{2:<16.4f}{3:<16.4f}\n".format(atom[0], atom[1][0], str(atom[1][1]), str(atom[1][2]))
        return atom_str


    @staticmethod
    def get_ring_str(atom_list):
        atom_list_str = ''
        for atom in atom_list:
           atom_list_str += RingUtil.atom_tostring(atom)
        return atom_list_str


    @staticmethod
    def write(path, data):
        with open(path, 'w') as f:
           f.write(data)