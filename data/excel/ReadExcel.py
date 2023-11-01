import os
from openpyxl import load_workbook
from utils.ExcellUtils import ExcelUtil

# 1.获取excel路径
excel_proj=os.path.dirname(__file__)
# print(excel_proj)
excelfile=excel_proj+os.sep+"excel_data.xlsx"
# print("excel文件路径为",excelfile)

# 2.定义一个类
class ExcelData:
    # 初始化excel文件
    def __init__(self):
        self.ExcelReader=ExcelUtil(excelfile)
    # 定义一个方法，获取excel数据
    def GetExcelData(self):
        return self.ExcelReader.data()

ExcDt=ExcelData()

if __name__ == '__main__':
    print(ExcDt.GetExcelData())






