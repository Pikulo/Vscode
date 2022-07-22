from typing import Counter


rectangles = rectangles = [[2,3],[3,7],[4,3],[3,7]]
list_data=[]
for i in rectangles:
    list_data.append(min(i))
print(list_data)
a=Counter(list_data)
print(a.get(max(a.keys())))