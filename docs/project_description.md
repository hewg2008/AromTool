
首先，在系统中新建一个目录(文件夹)，命名为aromtool。将这个项目的所有文件都存储在这个目录以保证import语句正常工作。  

在aromtool中，用户输入一个包含配体（mol2格式）, 蛋白（pdb格式）文件的PDB源数据集。

然后用户从配体和蛋白文件中取出芳香环，获取相关属性比如原子种类，原子坐标，环质心坐标，环法向量,环类型。  

接着，如果有需要判断芳香环的类型从而以所得芳香环类型作为过滤参考值过滤源数据集，则判断芳香环的类型，然后进行过滤，
生成新的子数据集。 
 
如果不需要判断芳香环的类型，则进行下一步。
 
接着，进行接触判断，接触判断依据为芳香环质心之间的距离，若有接触，将有接触的PDB挑出生成一个新的子数据集。  
然后生成接触的类型，进行环的加氢（addh函数）和替换(align函数），然后生成.xyz格式接触文件。

接着，调用神经网络模型计算器进行接触的能量计算。将生成的能量写入接触文件。

接着，进行报表的输出。最后输出一个子数据集（包含接触文件的PDB）和一个报表。

命令行操作  
Usage:  
  aromtool [options] <input-dir>  

  create aromatic contact dataset from source PDB dataset in input director.  
  
  
Options:  
  -h, --help            show this help message and exit.    
  -f <mode>, --ligandfilter-mode=<mode>  
                        filter dataset according to <mode>.   
                        Correct modes are:    
                        'all' no filter.   
                        'benzene' filter all PDBs with ligand without benzene.    
                        'carbocycle' filter all PDBs with ligand with heterocycle.     
                        'heterocycle' filter all PDBs with ligand without heterocycle.    
                        [DEFAULT: all]    
  -fc <mode>, --filtercontact-mode=<mode>
                        'aLL' no filter   
                        'phe' filter                      
                        'tyr' filter
                        'trp' filter        
                         [current: all]
  -e <mode>, --extract=<mode>
                        extract contact and output .xyz files with contact conformations.    
                        Correct modes are :   
                        'yes' extract   
                        'no' Not extract   
                        [current: yes]  
  -r <mode>, --output-reporter=<mode>  
                        output reporter of analysis of contact dataset.  
                        Correct modes are :     
                        'yes' output reporter   
                        'no' Not output reporter   
  
  -i < input director name>, --input_dir=<input director name>
                        set the input director.   
                        [current: none]
