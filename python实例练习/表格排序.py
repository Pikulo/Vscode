# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/10  17:52

import pandas as pd
import xlwings as xw
# import openpyxl
# #��ȡExcel�ļ�
# wb= openpyxl.load_workbook('C:\\Users\\15808\\Desktop\\�½��ļ���\\����1801�����ϳɼ���.xlsx',data_only=True)
# # books = pd.read_excel('C:\\Users\\15808\\Desktop\\�½��ļ���\\����1801�����ϳɼ���.xlsx',data_only=True)
# # ,sheet_name='������ 1 - ����1801�ɼ���'
# ws=wb.worksheets[1]
# for row in ws.rows:
#   for cell in row:
#     print(cell.value)
import pandas as pd
scores_exl=pd.read_excel('C:\\Users\\15808\\Desktop\\�½��ļ���\\����1801�����ϳɼ���.xlsx',sheet_name='������ 1 - ����1801�ɼ���',keep_default_na=False)# �����ֱ��Ĭ�϶�ȡ�����Excel�ĵ�һ����
# data=df.head()  # Ĭ�϶�ȡǰ5�е�����
# data=scores_exl.values  # ��ȡ���е�����
# data=scores_exl.iloc[0].values  # 0��ʾ��һ�� �����ȡ���ݲ���������ͷ
# iloc[-1]��ʾ���һ������
# data=scores_exl.iloc[[1,2]].values
# ���pandas��ȡExcel��ո���ʾnan�İ취 ��readʱ����keep_default_na=False
# ��ȡָ��������
# data=scores_exl.iloc[1,2]
# ��ȡָ���Ķ��ж���ֵ��
# data=scores_exl.iloc[[0,1,2,3],[1,2,3]].values  # 0����4�� 1����3��
# data=scores_exl.iloc[:,[2]].values  # �������е�2�е�ֵ��������ҪǶ���б�
# ��ȡ�кŲ���ӡ���
# print(scores_exl.index.values)  # ��ͷ����
# print(scores_exl.columns.values)
# ��ȡָ��������ֵ��
# print(scores_exl.sample(1).values)  # �����ȡ DataFrame.sample����
# ��ȡָ���е�ֵ��
print(scores_exl['11'].values)
# print("{0}".format(data))  # ��ʽ�����
