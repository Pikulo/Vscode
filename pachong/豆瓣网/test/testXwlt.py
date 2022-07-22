# -*- encoding=utf-8 -*-
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/7/28  11:18

import xlwt
'''
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet1')
worksheet.write(0,0,'hello')
workbook.save('student.xls')
'''
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet1')
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,'%d × %d = %d'%(i+1,j+1,(i+1)*(j+1)))

workbook.save('student.xls')











