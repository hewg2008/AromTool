from aromtool.io.file import File
from aromtool.utils.path import Path
from aromtool.utils.excelutil import ExcelUtil as excel

# 统计mol2文件 带*.ar的数据并生成 excel 表

clist = ['C.ar','N.ar','O.ar','S.ar','P.ar','O','S','P','Cl','F']


def parsemol2Data(mol2Path,f):
    allmofile = File.parse_mol2_data(mol2Path)

    atominfo = []
    cmap = {'C.ar': 0, 'N.ar': 0, 'O.ar': 0, 'S.ar': 0, 'P.ar': 0,'O':0,'S':0,'P':0,'Cl':0,'F':0} #统计数据
    atominfo.append(f)
    atominfo.append(cmap)
    for f in allmofile:
        item = f.split()
        if item[5] in clist:
            cmap[item[5]] += 1

    return atominfo


def build(path):

   floders = File.getDir(path)
   k = 0
   content = []
   for f in floders:
     k += 1
     mol2Path = Path.get_ligand_path(path, f)
     print('解析文件'+f+':'+str(k)+"/"+str(len(floders)))
     d = parsemol2Data(mol2Path, f)
     content.append([d[0],str(d[1]['C.ar']),str(d[1]['N.ar']),str(d[1]['O.ar']),str(d[1]['S.ar']),str(d[1]['P.ar']),str(d[1]['O']),str(d[1]['S']),str(d[1]['P']), str(d[1]['Cl']), str(d[1]['F'])])

   excel.write_excel('total.xlsx', content, columns=["item", "C.ar", "N.ar", "O.ar", "S.ar", "P.ar", "O", "S", "P", "Cl", "F"])


if __name__ == "__main__":
    build(r'G://pyabs//test//')