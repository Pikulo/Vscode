from re import T
from typing import Counter


s = "abccbaacz"
res = Counter()
index = True
for i in s:
    res[i]+=1
    for j in list(res.values()):
        if j ==2:
            print(list(res.keys())[list(res.values()).index(2)])
            index = False
            break
    if not index:
        break