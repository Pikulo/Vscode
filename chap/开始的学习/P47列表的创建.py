# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/1/22  10:29

# '''创建列表的第一种方式，使用[]'''
#
# lst=['hello','world','98']
#
# '''第二种方式，使用内置函数list'''
#
# list(['hello','world','98'])
# print(lst)
# print(list(['hello','world','98']))
# lst=['hello','world','98','hello']
# # print(lst.index('hello'))
# # print(lst.index('666'))
# print(lst.index('98',0,4))#查指定元素的索引
# lst=['hello','world','98','hello','world']
# #获取索引为2的元素
# print(lst[-1])
# print(lst[-2])
# print(lst[-3])
# print(lst[-4])
# print(lst[-5])
# lst=[10,20,30,40,50,60,70,80,90]
# print(lst[1:5])
# print(lst[1:5:1])
# print(lst[1::2])
# print('原列表:',lst)
# print('\t',lst[::2])
# print('\t',lst[::-1])#'-1'表示把列表里面东西逆向输出
# print('\t',lst[7::-1])#start=7,stop省略
# print('\t',lst[6::-2])#start=6,stop省略，step=-2
# print('\t',lst[6:0:-2])#start=6,stop=0，step=-2

# '''列表元素的判断和遍历'''
# lst=[10,20,30,40,'hello','kiddy']
# print(10 in lst)#True
# print('hello' in lst)#True
# print('kiddy' not in lst)#False
# for item in lst:
#     print(item,end='\t')
#lst=[10,20,30,60,60,50]
'''print('添加元素之前',lst,id(lst))
lst.append(100)
lst.append(101)
print('添加元素之后',lst,id(lst))
lst2=['hello','world']
#lst.append(lst2)
lst.extend(lst2)
print(lst)'''
#在任意位置上添加一个元素

# lst1=['10','']
# lst.insert(1,90)
# lst.insert(1,80)
# print(lst)
lst=[10,20,30,60,60,50]
lst3=[True,'hello','world','3']
#lst[1:]=lst3
lst[1:4:]=lst3
print(lst)



