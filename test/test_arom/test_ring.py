from aromtool.builder import Builder

# 获取1W6J配体的芳香环
mol2path = '16wj_ligand2.mol2'
#生成环对象列表
rings=Builder.get_mol2_rings(mol2path, only_ch=False)
print('环对象列表：')
print(rings)



# # 获取1W6J蛋白的芳香环
# mol2path = '16wj_protein.pdb'
# #生成环对象列表
# rings=Builder.get_pdb_rings(mol2path)
# print('环对象列表：')
# print(rings)


#
# mol2path = '1a52_ligand.mol2'
#
# #生成环对象列表
# rings=Builder.get_mol2_rings(mol2path, only_ch=False)
# print('环对象列表：')
# print(rings)
#
# # 获取环的数目
# ring_numbers=len(rings)
# print('环的总数：')
# print(ring_numbers)
#
# # 获取第一个环
# ring=rings[0]
# print('第一个环：')
# print(rings[0])

# 获取第一个环的元素
# elements=rings[0].elements
# print('环的元素： ')
# print(elements)
#
# # 获取第一个环的所有原子坐标
# positions=rings[0].positions
# print('环的原子坐标： ')
# print(positions)

'''
运行结果：
```python
环对象列表：
[<aromkit.ring.Ring object at 0x000000000B39E2C8>]
环的总数：
1
第一个环：
<aromkit.ring.Ring object at 0x000000000B39E2C8>
环的元素：
['C', 'C', 'H', 'C', 'C', 'H', 'C', 'H', 'C']
环的原子坐标：
[[106.876   17.424   97.544 ]
 [106.793   18.503   98.487 ]
 [106.7001  19.5244  98.1359]
 [106.833   18.229   99.892 ]
 [106.932   16.93   100.366 ]
 [106.9508  16.7397 101.433 ]
 [107.008   15.86    99.456 ]
 [107.0763  14.8482  99.8391]
 [106.998   16.065   98.05  ]]
'''

# from aromtool.builder import Builder
#
# pdbpath = '1a52_protein.pdb'
#
# #获取环对象列表
# rings=Builder.get_pdb_rings(pdbpath,filters=['PHE', 'TYR', 'TRP'])
#
# print('生成环对象列表：')
# print(rings)
#
# # 获取环的数目
# ring_numbers=len(rings)
# print('环的总数：')
# print(ring_numbers)
#
# # 获取第一个环
# ring=ring[0]
# print('第一个环：')
# print(rings[0])
#
# # 获取第一个环的元素
# elements=rings[0].elements
# print('环的元素： ')
# print(elements)
#
# # 获取第一个环的所有原子坐标
# positions=rings[0].positions
# print('环的原子坐标： ')
# print(positions)
#
# # 获取环的原子组成，以pdb文件的第一个环为例。
# elements=rings[0].elements
# print('环的元素： ')
# print(elements)
#
# # 获取环的原子坐标
# positions=rings[0].positions
# print('环的原子坐标： ')
# print(positions)
#
# # 获取环的质心
# centroid=rings[0].centroid
# print('环的质心： ')
# print(centroid)
#
# # 获取环的法向量
# normal_vector=rings[0].normal_vector
# print('环的法向量： ')
# print(normal_vector)

'''
#结果：
环的元素：
['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'H', 'H', 'H', 'H', 'H', 'H', 'N']
环的原子坐标：
[[ 97.898  27.775 105.448]
 [ 96.932  26.269 104.117]
 [ 97.128  27.456 103.387]
 [ 96.336  25.172 103.486]
 [ 97.432  26.496 105.428]
 [ 96.164  26.491 101.461]
 [ 96.751  27.583 102.062]
 [ 95.956  25.293 102.159]
 [ 98.346  28.263 106.314]
 [ 97.997  29.331 103.97 ]
 [ 96.174  24.24  104.028]
 [ 95.854  26.56  100.418]
 [ 96.912  28.512 101.514]
 [ 95.49   24.448 101.652]
 [ 97.723  28.36  104.223]]
环的质心：
96.92444444444443,26.76611111111111,103.53011111111111
环的法向量： 
0.7438199999999915,0.4804139999999987,2.7431909999999675

'''


