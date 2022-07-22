from collections import defaultdict
from functools import reduce
from itertools import combinations

#给你一个整数数组 nums 。
# 如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。
# 返回好数对的数目。
'''
#1.我自己的方法
nums = [1,2,3,1,1,3]
sum=0
for i in combinations(nums,2):
    if i[0]==i[1]:
        sum+=1 
print(sum)
'''
#2.法2
nums = [1,2,3,1,1,3]
ret, dct = 0, defaultdict(int)
for i in nums:
    print(dct[i])
    ret, dct[i] = ret+dct[i], dct[i]+1
print(ret,dct)