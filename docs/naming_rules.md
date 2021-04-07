### 0 包命名

aromkit: 包名。
模块名： calculator, 注：这个模块有子模块， piNN
模块名： config.
模块名： io
模块名： utils
模块名： bin, 



###1 脚本命名：
filter_ben.py: 过滤苯环的脚本，即筛选出配体文件只含有纯种6个C.ar标注的原子。
build_contact.py: 构建接触的脚本。
filter_ben_phe.py： 筛选苯环与苯环（蛋白的苯环取名phe）接触的脚本
split_contact_xyz.py： 拆分xxxx_contact_raw.xyz文件的脚本。
convert_xyz_to_mol2.py: 将“xyz”文件转换为“mol2”文件
add_hydrogen.py: 加氢脚本
convert_mol2_to_standard_xyz.py: 转换脚本
calculate_enerygy.py： 计算能量脚本
build_statistics.py: 构建统计的脚本

###2  变量命名

全局变量：
大写。全局变量名一律大写。
可能出现的全局变量名：
LOG_PATH
LOGGER_NAME
THRESHOLD

列表变量：


###3 路径变量： 
前缀: PRO_PREFIX, LIG_PREFIX, 后缀: PRO_SUFFIX, LIG_SUFFIX
数量：阿拉伯数字，如1， 2， 。。。
配体文件可能出现的后缀名： LIG_SUFFIX1=_contact

接触可能出现的文件命名： 
xxxx_contact_raw.xyz：   第一次生成的接触文件，包含所有的接触及接触的描述。
xxxx_contact_x_raw.xyz： 第二次生成接触文件，每个文件仅含单独的一个接触。
xxxx_contact_x_raw.mol2： 第三次生成的接触文件，将上一步出现的xyz文件转化为mol2文件。
xxxx_contact_x_standard.mol2： 第四次生成的接触文件，将上一步生成的mol2文件（通过加氢操作后完整的接触文件）
xxxx_contact_x_standard.xyz： 第五次生成的基础文件，将上一步生成的mol2文件转成标准的xyz文件。


能量可能出现的文件命名：
变量命名： 
GENERAL_ENERGY_DAT, REFINE_ENERGY_DAT
文件命名：
general_energy.dat： 针对general数据集生成的能量文件。
refine_energy.dat:  针对general数据集生成的能量文件。

统计可能出现的文件命名：
变量命名： 
GENERAL_STATISTICS, REFINE_STATISTICS

文件命名：
general_statistics.xls
refine_statistics.xls

配置文件命名：
xxxx_contact.config

日志文件命名：
变量命名：
LOG_PATH
文件命名：
general_xxxx.log: 其中xxxx为当前执行脚本的名字前缀。

数据集目录命名：
general_set: 源数据集名。
general_set_ben: 筛选出配体文件只含有纯种6个C.ar标注的原子后构成的子数据集。
general_set_ben_phe:只含有ben_phe接触类型的子数据集。

refine_set: 源数据集名。
refine_set_ben: 筛选出配体文件只含有纯种6个C.ar标注的原子后构成的子数据集。
refine_set_ben_phe:只含有ben_phe接触类型的子数据集。


### 4 函数命名
动词加名词，需要时加介词。词之间强制加下划线， 动词和名词尽量用全名，不要用缩写。
getvector-->get_normal_vector
要注重解析，获取等的区别应用。

### 5 专业名词： 

分子组成：
原子： atom
原子信息： atom_information
原子坐标： atom_coordinate
原子种类： atom_type
元素： element, 有时候与原子种类通用。
键： bond
键连信息： connectivity.
分子： molecule, atoms
配体： ligand
环： ring
苯环： benzene， 缩写ben。 注意：纯种6个C.ar才是苯环。
芳香性： aromatic， 缩写ar. 
芳香环： aromatic ring.
蛋白： protein
芳香残基： aromatic residue, 比如PHE, TYR, TRP。
氨基酸： amino acid， 缩写 aa


几何名词：
距离： distance
质心：centroid
质心距离：  centroid distance
平面： plane
角度： angle
向量： vector
法向量： normal vector
旋转： rotate
平移：translate
置换： permutate

物理化学动力学名词：
接触：contact， 有时候也用stack来描述接触，虽然字面意思有点差别，但是在这里是一个意思。
堆积： stack


