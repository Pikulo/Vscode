# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/10  13:11
'''题目：输入三个整数x,y,z，请把这三个数由小到大输出。'''
list=[]
for i in range(3):
    list.append(int(input('输入整数')))

list.sort()
for i in range(3):
    print(list[i])