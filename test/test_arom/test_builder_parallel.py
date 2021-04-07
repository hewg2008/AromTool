
from aromtool.reporter import ReportManager
from aromtool.builder_parallel import ContactBuilder, BatchBuilder
from aromtool.calculator import  EnergyCalculator
import multiprocessing
import time

# 假设用户希望从PDBBind的refined set数据集中构建芳香接触的数据集。
# src_dataset= r"E:\paper\thesis\application\16wj\f2f\after\16wj" #源数据集路径。
# dst_dataset= r'E:\paper\thesis\application\16wj\f2f\after\aromatic_set' # 目标数据集路径。
# # reportPath = r'E:\paper\thesis\application\16wj\f2f\after\report.xlsx' # 报表输出路径
# energyCalculator = EnergyCalculator(r'pi_below_0_4000.pb') # 能量计算器对象。


if __name__ == '__main__':
    multiprocessing.freeze_support()
    src_dataset = r"E:\paper\thesis\application\16wj\md_all_5000\after\test3\16wj"  # 源数据集路径。
    dst_dataset = r'E:\paper\thesis\application\16wj\md_all_5000\after\test3\aromatic_set'
    reportPath = r'E:\paper\thesis\application\16wj\md_all_5000\after\test3\report.xlsx'

    s_time = time.time()

    calculator = EnergyCalculator(r'pi_below_0_4000.pb')

    # MyManager.register('EnergyCalculator', EnergyCalculator)
    # manager = MyManager()
    # calculator = manager.EnergyCalculator('EnergyCalculator', r'G:\python\aromtool\aromkit\test\test_arom\pi_below_0_4000.pb')

    BatchBuilder.build_dataset( src_dataset, dst_dataset, reportPath, r'pi_below_0_4000.pb', ['PHE'], threshold=6.0)  #单线程
        # BatchBuilder.build_fast_batch(data_src_path, result_path, ['PHE', 'TYR', 'TRP'],calculator) #多线程
    e_time = time.time()

    print("use {:.5}s".format(e_time-s_time))
    print('完成')
