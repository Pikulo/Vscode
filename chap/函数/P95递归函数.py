# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/1/29  17:11
# def fac(n):
#     if n==1:
#         return  1
#     else:
#         res=n*fac(n-1)
#         return res
# print(fac(6))
'''斐波拉契数列：后一项等于前两项之和如 1 1 2 3 5 8'''
def fib(a):
    if a==1:
        return 1
    elif a==2:
        return 1
    else:
        return fib(a-1)+fib(a-2)

print(fib(6))  # 斐波拉契函数第8位位8
# 输出数列前六位的数字
for i in range(1,7):
    print(fib(i),end='\t')





