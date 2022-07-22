# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/1/23  14:38
# '''获取字典中的元素'''
# scores={'张三':100,'李四':95,'王五':76}
# '''第一种方式，使用方括号'''
# print(scores['张三'])
# # print(scores['kiddy'])
# '''第二种方式，使用get()方法'''
# print(scores.get('张三'))
# print(scores.get('kiddy'))
# print(scores.get('kiddo',35))
# scores={'张三':100,'李四':95,'王五':76}
# print('张三' in scores)
# print('kiddy' in scores)
# print('张三' not in scores)
# del scores['张三']
# print(scores)
# scores['kiddy']=21
# print(scores)
# scores.clear()
# print(scores)

scores={'张三':100,'李四':95,'王五':76}
#获取所有的键
a=scores.keys()
print(a)
print(type(a))
print(list(a))#把建组合到列表里

#获取所有的value
b=scores.values()
print(b)
print(type(b))
print(list(b))#把values组合到列表里

#获取所有的key、value对
c=scores.items()
print(c)
print(type(c))
print(list(c))#元组()





