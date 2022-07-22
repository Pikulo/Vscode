# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/1/24  10:58
# '''可变序列 列表，字典'''
# lst=[10,20,44]
# print(id(lst))
# lst.append(300)
# print(id(lst))#内存地址没有更改
# '''不可变序列 字符串，元组'''
# s='hello'
# print(id(s))
# s=s+'world'
# print(id(s))#内存地址发生了更改
# print(s)
# '''元组的创建方式'''
# '''第一种，使用（）'''
# t=('kiddy','hello','18')
# print(t,type(t))
# t2='kiddy','hello','18'#省略小括号
# print(t2,type(t2))
# t3=('kiddy')#只包含一个元素不加逗号表示字符串
# print(t3,type(t3))
# t4=('kiddy',)#只包含一个元素加逗号表示元组
# print(t4,type(t4))
# '''第二种，使用内置函数tuple'''
# a=tuple(('kiddy','hello','18'))
# print(a,type(a))
# print('###################分割线###################')
# lst=[]
# lst1=list()
# print(lst,type(lst))
# print(lst1,type(lst1))
# d={}
# d1=dict()
# print(d,type(d))
# print(d1,type(d1))
# a=()
# a1=tuple()
# print(a,type(a))
# print(a1,type(a1))

t=(10,[20,30],'hello',True)
print(t,type(t))
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))
print(t[3],type(t[3]),id(t[3]))
'''尝试把t[1]修改为100'''
# t[1]=100      #元组不允许修改元素
'''由于[20,30]列表，列表是可变序列，可以向列表中添加元素'''
t[1].append(100)
print(t,id(t[1]))




