# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/19  14:00
'''Python 练习实例34
    练习函数的使用'''
'''
def hello_runoob():
    for i in range(3):
        print('RUNOOB')

hello_runoob()
'''
'''Python 练习实例37
    对10个数进行排序。'''
'''
s=input('以空格分开，输入十个数\n')
lst=[int(n) for n in s.split()]
print(lst)
lst.sort()
for i in range(len(lst)):
    print(lst[i])
'''
'''Python 练习实例38
题目：求一个3*3矩阵主对角线元素之和。'''
import numpy
a=int(input('您要输入几*几的矩阵（输入一个数字即可）？\n'))
print('接着输入您的矩阵数据')
F=numpy.zeros((a,a))
print(F)
for i in range(a):
    for j in range(a):
        F[i][j]=int(input(''))
sum=0
for i in range(a):
    for j in range(a):
        print(F[i][j])
if a%2==0:
    for i in range(a):
        sum+=F[i][i]
    k=a
    for i in range(a):
        sum+=F[k-1][i]
        k-=1
else:
    minus=a//2
    for i in range(a):
        sum+=F[i][i]
    k=a
    for i in range(a):
        sum+=F[k-1][i]
        k-=1
    sum-=F[minus][minus]
print(sum)