from typing import Counter


target = [1,2,2,3]
arr = [1,1,2,3]
# print(set(target)==set(arr) and len(target)==len(arr)) #错误示例：[1,2,2,3] [1,1,2,3]
print(Counter(target)==Counter(arr))