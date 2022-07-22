# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/10  13:56
'''题目：判断101-200之间有多少个素数，并输出所有素数。'''
for i in range(101,201):
    spot = 0
    for j in range(2,i):
        if i%j==0:
            spot+=1
    if spot==0:
        print('{0}是素数'.format(i))





