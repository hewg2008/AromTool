#Click使用指南
##1、Click介绍
Click 是基于 Python 构建的一个第三方命令行工具包，以可组合的方式创建漂亮的命令行接口，并根据需要使用尽可能少  
的代码。它是"命令行接口创建工具包"，旨在使编写命令行工具的过程快速而有趣，同时防止因无法实现预期的 CLI API 而  
导致的任何挫折。
Click 相比于 Python内置的命令行工具包Argparse，就好比 requests 相比于 urllib。其具有以下特点：  
1 命令的任意嵌套  
2 帮助页面自动生成  
3 支持在运行时延迟加载子命令  

##2、Click安装
使用“pip install click”命令安装，此教程以在Anaconda3的虚拟环境phychem安装为例，非虚拟环境安装在CMD（Conda prompt)窗口中
使用pip/conda命令安装即可。pip/conda会根据用户当前环境自动下载并安装所需配置环境（如软件包matplotlib，Numpy等）。

打开Anaconda3的Anaconda Prompt, 并激活phychem虚拟环境，输入安装命令安装

激活命令：
`conda activate phythem`

安装命令：
`pip install click`


##3、Click使用
###3.1 

```
import numpy as np
a = np.zeros((3, 2))
a[:, 1] = 1.0
a[1] = 2.0
print(a)
```
输出一个三行两列的二维数组，类似于一个大列表中三个列表元素，每个列表元素中有两个元素：
```
array([[ 0.,  1.],
       [ 2.,  2.],
       [ 0.,  1.]])
```
`a.shape`

计算数组是几行几列，结果：(3, 2)

`a.ndim`

计算数组的维度，结果：2

###3.2 ASE使用

（1）Atoms模块

Atoms对象是原子的集合。是ASE的核心模块。用Atoms定义CO分子的方法：
```
from ase import Atoms
d = 1.1
co = Atoms('CO', positions=[(0, 0, 0), (0, 0, d)])
```
在这里，第一个参数指定原子的类型，我们使用positions关键字指定原子的位置。其他可能的关键
字有：numbers，tags，momenta，masses，magmoms和charges。

如果是单个原子，则使用Atom模块，定义方法和前例基本相同

```
from ase import Atom
a1 = Atom('Si', (0, 0, 0))
a2 = Atom('H', (1.3, 0, 0), mass=2)
a3 = Atom(14, position=(0, 0, 0))  # 和a1相同
```
Atom在ase源码中的定义如下：

```class ase.atom.Atom(symbol='X', position=(0, 0, 0), tag=None, momentum=None, mass=None, magmom=None, charge=None, atoms=None, index=None)```

其中参数：

>symbol或number: str或int，可以是化学符号（str）或原子序数（int）。

>position: 三个浮点数的序列，表示原子的位置（x,y,z），提取方法“对象名.x/y/z”。

>tag: int，专用标签。

>momentum: 三个浮点数的序列，表示原子的动量。

>mass: float，以原子单位表示的原子质量。

>magmom: 单个或三个浮点数，表示磁矩。

>charge: float，表示电子电荷。

（2）io模块，写入和读取

将原子位置写入文件是通过以下write()功能完成的,其中实参slab是一个Atoms对象 ：

```
from ase.io import write
write('slab.xyz', slab)
```
这将以xyz格式写入文件。存储原子参数可能的格式为：

>xyz，最简单的格式

>cube，高斯立方体文件

>pdb，蛋白质数据库文件

>traj，ASE自己的轨迹格式

>py，Python脚本

从文件读取是这样完成的：

```
from ase.io import read
slab_from_file = read('slab.xyz')
```
如果文件包含多个系统（构象），则该write()函数的默认行为是返回最后一个（构象）。但是，我们可以执行以下
操作来加载特定的系统（构象）：
```
read('slab.traj')      # 最后一个构象
read('slab.traj', -1)  # 同上
read('slab.traj', 0)   # 第一个构象
```
###3.3 项目案例
下面以一个xyz文件为例，读取该文件构建Atoms实例，输出原子的种类，原子数量和每个原子的坐标。

文件链接：<https://pan.baidu.com/s/14XU0s192ioS4dXwuhmIWJw>，提取码：g3rs

```
from ase.io import read

Ben_Ben1 = read('Ben_Ben1.xyz')     #读取Ben_Ben1.xyz文件
print(Ben_Ben1.symbols)             #打印对象Ben_Ben1的化学符号
print(Ben_Ben1.positions)           #打印其所有原子的坐标
print(Ben_Ben1.positions.shape[0])  #打印其所有原子的数量
```
结果：
```
CHCHCHCHCHCHCHCHCHCHCHCH
[[ 6.97092438e-01  1.20622848e+00  0.00000000e+00]
 [ 1.23875148e+00  2.14233638e+00  4.92867588e-03]
 [ 1.39406620e+00  0.00000000e+00  0.00000000e+00]
 [ 2.47532548e+00  1.14333064e-04  1.09775644e-02]
 [ 6.96663336e-01 -1.20634366e+00 -1.37748483e-03]
 [ 1.23802159e+00 -2.14276805e+00  1.26101421e-03]
 [-6.96940684e-01 -1.20690302e+00 -5.07818264e-04]
 [-1.23779913e+00 -2.14373788e+00 -1.69760104e-03]
 [-1.39411733e+00  1.70803848e-04  1.98100687e-03]
 [-2.47586590e+00  2.65443726e-04  1.46101868e-03]
 [-6.96763966e-01  1.20684740e+00 -9.57037790e-05]
 [-1.23742524e+00  2.14379534e+00 -1.81194041e-04]
 [ 4.50058552e+00  2.37200533e+00  6.74192156e+00]
 [ 4.50162206e+00  3.43624146e+00  6.93457981e+00]
 [ 5.70729675e+00  1.68644360e+00  6.62103853e+00]
 [ 6.64363758e+00  2.21705114e+00  6.72574586e+00]
 [ 5.70649998e+00  3.14426375e-01  6.37771614e+00]
 [ 6.64354217e+00 -2.18111780e-01  6.28649450e+00]
 [ 4.49988318e+00 -3.72417724e-01  6.25749007e+00]
 [ 4.49990345e+00 -1.43752888e+00  6.06847410e+00]
 [ 3.29257358e+00  3.13332899e-01  6.38093363e+00]
 [ 2.35570451e+00 -2.19153282e-01  6.28651394e+00]
 [ 3.29316100e+00  1.68620952e+00  6.62090007e+00]
 [ 2.35646063e+00  2.21909406e+00  6.71477519e+00]]
24
```

（3）以EMT计算器计算能量

EMT为高效率计算器，下面以些计算器为例
```
from ase import Atoms
from ase.calculators.emt import EMT

d = 1.10
molecule = Atoms('CO2', [(0., 0., 0.), (0., 0., d),(0., 0., 0.)]) #创建对象
molecule.set_calculator(EMT())                                    #将计算作为参数附加到molecule对象
print(molecule.get_potential_energy(),'eV')                       #打印计算出的molecule对象的总能量
```
结果：
`79.04733847750316 eV`

##4 注意事项

