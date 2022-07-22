# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/1/28  11:17

# def fun(num):
#     odd=[]  # 存奇数
#     evem=[]  # 存偶数
#     for i in num:
#         if i%2:
#             odd.append(i)
#         else:
#             evem.append(i)
#     return odd,evem
# # 函数的调用
# lst=[10,29,36,53,55,20]
# print(fun(lst))
# def fun(a,b=10):  # b为默认参数
#     print(a,b)
#
#
# # 函数的调用
# fun(100)
# fun(20,30)  # 30把b的默认值替代了
#
# print('hello',end='\t')
# print('world')
'''
    #个数可变的位置参数
def fun(*args):
    print(args,end=' ')
    print('索引0为：',args[0])

fun(10)
fun(25,30)
fun(60,30,88)
'''
'''
def fun(**args):
    print(args,end=' ')

fun(a=10)
fun(a=10,b=20,c=30)
'''
def fun(a,b,c):
    print('a=',a)
    print('b=', b)
    print('c=', c)
'''
# 函数的调用
fun(10,20,30)
lst=[11,22,33]
fun(*lst)
dict={'a':111,'b':222,'c':333}
fun(**dict)
'''






