# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/1/23  10:58
# lst=[10,50,5,69,3]
# print('排序前的列表',lst,id(lst))
# #排序，调用sort，升序排序
# lst.sort()
# print('排序后的列表',lst,id(lst))
# #排序前和排序后id保持不变
# '''通过指定关键字参数，将列表中的元素降序排序'''
# lst.sort(reverse=True)
# print(lst)
# lst.sort(reverse=False)
# print(lst)
# '''使用内置函数sorted对列表进行排序，将产生一个信新列表'''
lst2=[10,50,5,69,3]
new_lst=sorted(lst2)#升序排序
print('新列表',new_lst)
print('原列表',lst2)
lst3=sorted(lst2,reverse=True)
print(lst3)