# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/10  17:16
'''题目：输出指定格式的日期。'''

import datetime

if __name__ =='__main__':
    print(datetime.date.today().strftime('%d/%m/%Y'))
# 创建日期对象
miyazakiBirthDate = datetime.date(1941, 1, 5)
print(miyazakiBirthDate.strftime('%d/%m/%Y'))
# 日期算术运算
miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=3)
print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))


# 日期替换
miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 2)
print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))