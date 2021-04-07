#Aromtool 

**Aromtool** 是一个基于Python构建，用于分析配体（通常是药物）和受体（通常是蛋白）之间相互作用的程序。  
借助于其内部集成的基于神经网络(**Neural Network**)模型的芳香接触能量计算器(**Aromatic Contact Energy  
 Calculator**)，其可以：  
1 识别、过滤、转换、抽取配体（mol2格式）和受体（pdb格式）文件中的芳香环。  
2 判断配体与受体之间的芳香环是否有接触，构建芳香接触并以xyz格式输出接触构象文件。  
3 输出芳香接触类型、几何（包括接触距离(**Distance**)与接触角度(**Angle**)）及能量(**Energy**)报表（Excel格式）。  

**Aromtool**的主要是为药物研发领域科学家提供一个简单的芳香接触数据集(**Dataset**)及分析报表  
(**Report**)生成工具, 其具有以下设计目标:  
1 简明易用。其可以通过命令行工具和Python脚本使用。而对于编程新手（尤其是物化领域的科研工作者）来说，  
Python 脚本易于理解（不像C++, Java等其他语言具有很高的学习成本），使用Aromtool的个各种功能都非常简单。  
2 自动集成批处理功能。不像其他物理化学程序如MOE, Schrodinger, RDKIT,需要使用者再次编写批处理代码。  
3 开源代码方便自定义及扩展。代码基于面向对象的Pythonic风格编写，核心类基于Numpy数组（ndarray)编写，方  
便融入所有python世界的代码，可以轻松进行类或模块的扩展。比如计算器可以自定义其他能量计算器。


#1 环境需求
python
tensorflow
scikit-learn
scipy
numpy
pandas
xlwt
toml
ase
openbabel
rdkit

# 2 程序目录树

aromtool
│ README.md
│ requirements.txt
│ setup.py
│ TODO.md
│
├─aromtool
│ │ init.py
│ │
│ ├─config
│ │ antable.py
│ │ init.py
│ │
│ ├─core
│ │ init.py
│ │
│ ├─io
│ │ file.py
│ │ format_convert.py
│ │ to_raw.py
│ │ to_systems.py
│ │ to_xyz.py
│ │ init.py
│ │
│ ├─resources
│ ├─tests
│ │ init.py
│ │
│ └─utils
│ atomutil.py
│ geometry.py
│ init.py
│
├─bin
│ └─script
│ │ analyse_alldata.py
│ │ analyse_all_6contact_data.py
│ │ analyse_ar_num.py
│ │ analyse_static.py
│ │ build_raw.py
│ │ build_xyz_debug.py
│ │ build_xyz_release.py
│ │ filter_ar.py
│ │ write.xlsx
│ │
│ └─log
│ all_contact.log
│ ar_num.log
│ build_ar.log
│ filter_ar.log
│ new.log
│
└─docs

#3 程序类图


#4 安装


#5 使用
arom



#6 案例




#7 使用许可




#8 文档使用者  
本文档适合能够使用Python语言执行简单命令的物理化学理论计算领域的科研工作者。主要是针对开发人员。


