from aromtool.builder import EnergyCalculator
from ase.io import read
import time
import os
# 能量计算器模型
pinn='pi_below_0_4000.pb'

# 能量计算器实例化
energy_calculator=EnergyCalculator(pinn)

# 获取能量
path=r'E:\paper\thesis\application\16wj\md_all_5000\after\16wj\aromatic_set\contact'

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


files=get_files(path)
start_time=time.time()
count=0
for file in files:
    print(file)
    energy=energy_calculator.get_energy(read(file)) # contact为Contact对象。
    print(energy)
    count +=1
    print(count)
    if count==5000:
        break
end_time=time.time()
print('文件处理结束，用时：{}'.format(end_time - start_time))


