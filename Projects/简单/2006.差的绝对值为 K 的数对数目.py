from functools import reduce
from itertools import combinations


nums = [2]
k = 2
sum=0
for i in combinations(nums,2):
    print(i)
    r=reduce(lambda x,y: abs(x-y),i)
    if r==k:
        sum+=1
print(sum)
print(help(combinations))


