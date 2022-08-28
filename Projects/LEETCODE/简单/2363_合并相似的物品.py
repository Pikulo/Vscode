from collections import Counter


items1 = [[28,3],[12,4],[29,8]]
items2 = [[28,6],[12,8],[29,9]]

# my idea
'''
item_all = items1+items2
item_all.sort()
# item_all.sort(key=lambda y:y[1]) # 以有y[1]排序
print(item_all)
index = list(set(y[0] for y in item_all))
index.sort()
dict_out = {}
print(index)
for i in index:
    dict_out[i]=0
print(dict_out)
for i in item_all:
    dict_out[i[0]]+=i[1]
res = [list(i) for i in dict_out.items()]
print(res)
# return res
'''

#other idea
print(dict(items1),dict(items2))
print(Counter(dict(items1))+Counter(dict(items2)))
print((Counter(dict(items1))+Counter(dict(items2))).items())
print(sorted((Counter(dict(items1)) + Counter(dict(items2))).items()))