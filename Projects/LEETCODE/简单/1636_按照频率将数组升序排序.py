# 给你一个整数数组 nums ，
# 请你将数组按照每个值的频率 升序 排序。如果有多个值的频率相同，
# 请你按照数值本身将它们 降序 排序。 
# 请你返回排序后的数组。
from audioop import mul
import re
from traceback import print_tb
from typing import Counter

# nums = [1,1,2,2,2,3]
nums = [2,3,1,3,2]
# nums = [-1,1,-6,4,5,-6,1,4,1]
nums = Counter(nums)
nums=sorted(nums.items(),key=lambda x:x[1])

dic = {}
for i in nums:
    dic.setdefault(i[1],[])
    dic[i[1]].append(i[0])
print(dic)
res = []
for i in dic.items():
    print(i,i[0])
    k = sorted(i[1],reverse=True)
    for m in k:
        for p in range(i[0]):
            res.append(m)      
print(res)
# return res