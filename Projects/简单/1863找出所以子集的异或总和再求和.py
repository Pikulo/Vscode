from functools import reduce
from itertools import combinations
from operator import xor


nums = [3,4,5,6,7,8]
#分三部分：
#1.单个元素2.组合3.
sum=0
for i in range(1,len(nums)+1):
    for j in combinations(nums,i):
        sum+=reduce(xor,j)
print(sum)
# print(list(map(lambda x: x**2,[2,4,16])))
