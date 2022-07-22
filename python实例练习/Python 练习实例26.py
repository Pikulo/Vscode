# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/18  15:51
'''题目：利用递归方法求5!。'''
def multipile(n):
    sum=1
    if n==0:
        return 1
    else:
        sum=n*multipile(n-1)
    return sum

print(multipile(5))