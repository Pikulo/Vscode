# 给你一个整数数组 nums ，
# 请你将数组按照每个值的频率 升序 排序。如果有多个值的频率相同，
# 请你按照数值本身将它们 降序 排序。 
# 请你返回排序后的数组。
from audioop import mul
from traceback import print_tb
from typing import Counter

nums = [1,1,2,2,2,3]
nums = [2,3,1,3,2]
nums = Counter(nums)
nums=sorted(nums.items(),key=lambda x:x[1])
# print(nums)
# for i in nums:
    # print(i[0],i[1])
dic = {}
for i in nums:
    dic.setdefault(i[1],[])
    dic[i[1]].append(i[0])
print(dic)
res = []
for i in dic.items():
    if len(i[1])>1:
        k = sorted(i[1],key=True)
        print(k)
    else:

        
    
