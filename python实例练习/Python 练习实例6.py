# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/10  13:16
'''题目：斐波那契数列。'''

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(10))

lst=[]
for i in range(11):
    lst.append(fib(i))
print(lst)


