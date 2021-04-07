aromkit脚本使用步骤

aromkit脚本路径： aromkit/bin/script/general_set


步骤1：过滤-基于配体
建立包含一个bezene环配体的一般集和精集的子数据集。

输入：数据集的根路径。目录名：general_set

输出：一个新的子数据集。目录名: general_set_w_ben

脚本：filter_ar.py

[2678， 1042]



步骤2：生成接触
生成原始“xyz”格式的联系人。

输入：子数据集的根路径。dirname: general_set_w_ben

输出：在子数据集的每个子目录中产生一个新文件。文件名：xxxx_contact_raw.xyz

脚本：build_contact.py


注：仅过滤得到C.ar，不含N.ar或其他。


步骤3：过滤-基于蛋白残基
过滤苯-苯丙氨酸子数据集，该子数据集仅包含与苯-苯丙氨酸的接触。

Input: root path of the sub-dataset. dirname: general_set_w_ben
Output: a new sub-dataset. dirname: general_set_w_ben_phe
Script: filter_ben_phe.py



步骤4: 拆分
拆分xxxx_contact_raw.xyz文件。

Input: root path of the sub-dataset. dirname: general_set_w_ben_phe
Output:  One or more than one new files in each subdirectory of the sub-dataset. file name: xxxx_contact_x_raw.xyz
Script: split_contact_xyz.py


步骤5: 转换
将“xyz”文件转换为“mol2”文件

Input: root path of the sub-dataset. dirname: general_set_w_ben_phe
Output:  One or more than one new files in each subdirectory of the sub-dataset. file name: xxxx_contact_x_raw.mol2
Script: to_contact_mol2.py

步骤6：加氢

Input: root path of the sub-dataset. dirname: general_set_w_ben_phe
Output:  One or more than one new files in each subdirectory of the sub-dataset. file name: xxxx_contact_x_standard.mol2
Script: add_hydrogen.py


步骤7:置换

将“mol2”文件转换为标准“xyz”文件。

Input: root path of the sub-dataset. dirname: general_set_w_ben_phe
Output:  One or more than one new files in each subdirectory of the sub-dataset. file name: xxxx_contact_x_standard.xyz
Script: mol2_to_standard_xyz.py


步骤8：计算接触能量。

Input: root path of the sub-dataset. dirname: general_set_w_ben_phe
Output:  One 'dat' file in root path. file name: gen_energy.dat
Script: calculate_enerygy.py, piNN.py, piNN.pb


步骤9：生成“xls”格式的能源汇总文件。

Input: root path of the sub-dataset. dirname: general_set_w_ben_phe
Output:  One 'xls' file in root path. file name: gen_energy_sum.xls
Script: build_energy_sum.py


步骤10：拟合校正后的评分函数参数。

Input: file path of the sub-dataset. filename:  gen_energy_sum.xls
Output:  parameters of the fitting function.
Script: fit_function.py


步骤11：预测和评估校正后的功能。

Input: file path of the sub-dataset. filename:  gen_energy_sum.xls
Output:  parameters of the fitting function.
Script: predict.py
