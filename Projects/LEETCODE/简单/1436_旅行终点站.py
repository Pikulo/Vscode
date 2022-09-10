paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
list_left = []
list_right = []
for i in paths:
    list_left.append(i[0])
    list_right.append(i[1])
print(list_left,list_right)
print(set(list_right)-set(list_left))
res = list(set(list_right)-set(list_left))
print(res[0]) 

print(list(map(lambda x :x[0],paths)))

dict1 = dict.fromkeys([1,2,3])
print(dict1)
dict1 = dict.fromkeys((1,2,3))
print(dict1)
dict2 = dict.fromkeys([1,2,3],'test')
print(dict2)
dict3 = dict.fromkeys([1,2,3],['one','two','three'])
print(dict3)

hashmap = dict.fromkeys(list(map(lambda x:x[0], paths)), 0)
print(hashmap)
 