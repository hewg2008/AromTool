from aromtool.io.formatconv import FileConverter

# 将xyz文件转换对应的raw文件

sfpath = r'G:\pyabs\xyz\ja9b00936_si_002.xyz'  # Source file(in xyz format) path
subPath = r'G:\pyabs\xyz\raw'

FileConverter.xyz_to_raw(sfpath, subPath)
