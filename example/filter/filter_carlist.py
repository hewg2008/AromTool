import argparse

from aromtool.filter.screen import Filter


# 批量 过滤 包含6个 C.ar 文件
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="filter c.ar ")
    parser.add_argument("src_path")
    parser.add_argument("car_num", type=int, help='C.ar number')
    args = parser.parse_args()  # 返回一个命名空间
    print(args)
    print('脚本正在启动')
    params = vars(args)  # 返回 args 的属性和属性值的字典
    src_path = params['src_path']
    filter = Filter(src_path)
    car_list = filter.car_list(car_number=params['car_num'])

    print('过滤文件得到结果：' + str(len(car_list)))
    print(car_list)