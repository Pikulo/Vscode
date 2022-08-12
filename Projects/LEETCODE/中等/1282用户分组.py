from ast import keyword
from typing import Counter


# groupSizes = [2, 1, 3, 3, 3, 2]
# groupSizes = [3,3,3,3,3,1,3]
groupSizes = [1,1]
res = []
couter_gropus = dict(Counter(groupSizes))

dict_index_num = {} #存放数字对应的索引
list_set_groups = list(set(groupSizes))
for i in list_set_groups:
    index_i = [m for m in range(len(groupSizes)) if groupSizes[m]==i]
    dict_index_num[i] = index_i
# print(dict_index_num.get(3))

for i in couter_gropus.items():
    add_length = i[0] # 表示列表长度范围
    add_number = i[1]//i[0] # 表示要添加索引的列表数量
    # print(add_length,add_number)
    m = 0
    n = add_length
    for j in range(add_number):
        res.append(dict_index_num.get(i[0])[m:n])
        m+=add_length
        n+=add_length
print(res)



# dic_groups = {}
# for index,i in enumerate(groupSizes): # 获取索引和对应元素
#     dic_groups[index] = i
# print(dic_groups)

