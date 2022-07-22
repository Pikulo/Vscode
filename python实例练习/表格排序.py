# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/10  17:52

import pandas as pd
import xlwings as xw
# import openpyxl
# #读取Excel文件
# wb= openpyxl.load_workbook('C:\\Users\\15808\\Desktop\\新建文件夹\\海事1801大三上成绩单.xlsx',data_only=True)
# # books = pd.read_excel('C:\\Users\\15808\\Desktop\\新建文件夹\\海事1801大三上成绩单.xlsx',data_only=True)
# # ,sheet_name='工作表 1 - 海事1801成绩单'
# ws=wb.worksheets[1]
# for row in ws.rows:
#   for cell in row:
#     print(cell.value)
import pandas as pd
scores_exl=pd.read_excel('C:\\Users\\15808\\Desktop\\新建文件夹\\海事1801大三上成绩单.xlsx',sheet_name='工作表 1 - 海事1801成绩单',keep_default_na=False)# 这个会直接默认读取到这个Excel的第一个表单
# data=df.head()  # 默认读取前5行的数据
# data=scores_exl.values  # 获取所有的数据
# data=scores_exl.iloc[0].values  # 0表示第一行 这里读取数据并不包含表头
# iloc[-1]表示最后一行数据
# data=scores_exl.iloc[[1,2]].values
# 解决pandas读取Excel里空格显示nan的办法 在read时加上keep_default_na=False
# 读取指定的行列
# data=scores_exl.iloc[1,2]
# 读取指定的多行多列值：
# data=scores_exl.iloc[[0,1,2,3],[1,2,3]].values  # 0——4行 1——3列
# data=scores_exl.iloc[:,[2]].values  # 读所有行的2列的值，这里需要嵌套列表
# 获取行号并打印输出
# print(scores_exl.index.values)  # 表头除外
# print(scores_exl.columns.values)
# 获取指定行数的值：
# print(scores_exl.sample(1).values)  # 随机抽取 DataFrame.sample（）
# 获取指定列的值：
print(scores_exl['11'].values)
# print("{0}".format(data))  # 格式化输出
