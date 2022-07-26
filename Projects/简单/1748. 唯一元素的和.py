from typing import Counter
# nums = [1,2,3,2]
nums = [1,1,1,1,1]

nums = dict(Counter(nums))
sum_out = 0
for i in nums:
    if nums.get(i)==1:
        sum_out+=i
print(sum_out)
# return sum_out