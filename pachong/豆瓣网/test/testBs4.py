# -*- encoding=utf-8 -*-
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/7/27  12:15
import re

from bs4 import BeautifulSoup

file = open('./baidu.html','rb')
html = file.read().decode('utf-8')
bs = BeautifulSoup(html,'html.parser')
# print(bs.title)
# print(bs.title.string)
# print(bs.a)
# print(bs.a.attrs)
# print(bs)
# print(bs.a.string)

# 文档遍历

# print(bs.head.contents) # 以列表形式存储

# 文档的搜索 #重要
# find_all()字符串过滤，会查找与字符串完全匹配的内容
# t_list = bs.find_all('a')
# print(t_list)


# # 正则表达式搜索
# t_list = bs.find_all(re.compile('a')) # 显示所有包含a的

# # 方法 ： 传入一个函数（方法）,根据函数的要求来搜索（了解）
# def name_is_exsist(tag):
#     return tag.has_attr('name')
# t_list = bs.find_all(name_is_exsist)

# # kwargs   参数
# # t_list = bs.find_all(id='head')
# t_list = bs.find_all(class_=True)
# for item in t_list:
#     print(item)

# # text 参数
# # t_list = bs.find_all(text = ['hao123','地图','贴吧'])
# t_list = bs.find_all(text = re.compile('\d'))  # 应用正则表达式来查找包含特定文本的内容
#
# t_list = bs.find_all('a',limit=3)
# for item in t_list:
#     print(item)

# css选择器
# t_list = bs.select('title')

# t_list = bs.select('.mnav') #.表示用类名查找

# t_list = bs.select('#u1')  # 通过id查找

# t_list = bs.select('a[class=bri]')  # 通过属性来查找

# t_list = bs.select('head > title') #通过子标签来查找

# t_list = bs.select('.mnav~.bri')
# print(t_list[0].get_text())




