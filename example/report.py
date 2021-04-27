from aromtool.builder import BatchBuilder
from aromtool.calculator import EnergyCalculator
from aromtool.reporter import ReportManager

# access the stacking interaction from refined set of PDBBind
# Define the directory of input files.
src_dataset = r'.\dataset'
# Define the directory of output xyz files
dst_dataset = r'.\dataset\AS'
# Define the report's path
reportPath = r'.\dataset\report.xlsx'
# Define calculator
energycalculator = 'AromNN-PiBPTT.pb'

# Put the above variables to BatchBuilder
batchbuilder = BatchBuilder.build_dataset(src_dataset, dst_dataset, reportPath, energycalculator)

# Exportation of report
ReportManager.export(reportPath, batchbuilder)