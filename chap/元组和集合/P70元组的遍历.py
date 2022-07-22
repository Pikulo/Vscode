# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/1/25  10:43

# t=('python','world','88')
# '''第一种获取元组元素的方，使用索引'''
# print(t[0],t[1],t[2])
# #print(t[3]) 报错
# '''遍历元组'''
# for item in t:
#     print(item,'',end='')


###################P71###################
# print('——————————————————集合的创建——————————————————')
# '''第一种方式'''
# s={2,3,4,5,6,7,7}
# print(s)#集合中的元素不允许重复
# '''第二种方式，用set()'''
# a=set(range(6))
# print(a,type(a))
# a1=set([1,2,3,4,54,5,6,6,6,6,80])
# print(a1,type(a1))#去掉了列表里的重复元素,集合里的元素无序
# a2=set((1,1,2,3,3,5,99))
# print((a2,type(a2)))#去掉了元组里的重复元素,集合里的元素无序
# ######集合中的元素是无序的
# a3=set('python')
# print(a3,type(a3))#明显看出集合中元素是无序的
# a4=set({1,2,2,54,62,21})
# print(a4,type(a4))

# #定义一个空集合
# a={}
# print(a,type(a))#是空字典
# a1=set()
# print(a1,type(a1))

#in not in同样适用于集合

#集合元素的新增
a={1,21,30,'Python',10}
a.add(5)#一次添加一个元素
print(a)
a.update({'kiddy',66,88})#一次添加多个
print(a)
a.update(('hello','good'))
print(a)
'''集合元素的移除操作'''
a.remove('Python')#一次删除一个指定元素
print(a)
# a.remove(999)#KeyError: 999
# print(a)
a.discard('hello')
print(a)
a.discard(999)
print(a)#元素不存在不显示错误
a.pop()
print(a)#随机删除一个元素，不能指定参数
a.clear()
print(a)