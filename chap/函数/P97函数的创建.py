# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/1/27  15:01
# def calc(a,b):#形参在函数的定义处
#     c=a+b
#     return c
# '''位置实参'''
# r=calc(10,20)#实参在函数的调用处
# print(r)
# '''关键字实参'''
# r2=calc(b=10,a=20)#区别上，根据等号左侧变量名字来传递实参值
# print(r2)
def fun(arg1,arg2):
    print('arg1',arg1)
    print('arg2', arg2)
    arg1=100
    arg2.append(10)
    print('arg1', arg1)
    print('arg2', arg2)
n1=11
n2=[22,33,44]
print('n1',n1)
print('n2',n2)
fun(n1,n2)
print('n1',n1)
print('n2',n2)

