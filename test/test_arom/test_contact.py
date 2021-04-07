from aromtool.builder import ContactBuilder



# 从数据中构建接触



# 从文件中构建接触
mol2path = '1a52_ligand.mol2'
pdbpath = '1a52_protein.pdb'

# 获取接触列表
builder=ContactBuilder(mol2path, pdbpath)
contacts=builder.get_contacts()
print('接触对象列表：')
print(contacts)

# 获取接触的数目
contact_numbers=len(contacts)
print('接触的总数：')
print(contact_numbers)

# 获取第一个接触
contact=contacts[0]
print('第一个接触：')
print(contact)

#获取第一个接触的角度
angle=contact.angle
print('接触角度：')
print(angle)

# 获取第一个环的元素
distance=contact.distance
print('接触距离： ')
print(distance)

print(contact.mol_ring.positions)
print(contact.pdb_code)
print(contact.contact_type)

