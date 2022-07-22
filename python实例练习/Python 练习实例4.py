# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/10  12:41

'''题目：输入某年某月某日，判断这一天是这一年的第几天？'''
year=int(input('输入年'))
month=int(input('输入月'))
day=int(input('输入日'))

last_month=[31,28,31,30,31,30,31,31,30,31,30,31]
sum=0
for i in range(month-1):
    sum+=last_month[i]
sum+=day
if (year%4==0 and year%100!=0) or year%400==0:
    sum+=1
print(sum)