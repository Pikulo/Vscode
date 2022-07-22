# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/7  19:58
'''题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？'''
for i in range(1,5):
    for j in range(1,5):
        for m in range(1,5):
            if (i!=j) and (i!=m) and (j!=m):
                print(i,j,m)




