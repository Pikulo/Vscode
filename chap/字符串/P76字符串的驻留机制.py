# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/1/25  16:09
# a='Python'
# b="Python"
# c='''Python'''
# print(a,id(a))
# print(b,id(b))
# print(c,id(c))
# print(a is b)
# print(a is c)
# print(b is c)
# # id都一致
# '''驻留机制'''
# s1=''
# s2=''
# print(s1 is s2)
# a1='abc%'
# a2='abc%'
# print(a1==a2,id(a1),id(a2),a1 is a2)
'''字符串的查询操作'''

a='hello,hello'
print(a.index('lo'))  # 3
print(a.find('lo'))  # 3
print(a.rindex('lo'))  # 9
print(a.rfind('lo'))  # 9
# print(a.index('k'))  # print(a.index('k'))ValueError: substring not found
print(a.find('k'))  # 返回值-1


