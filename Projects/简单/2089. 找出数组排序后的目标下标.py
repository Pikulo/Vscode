# nums = [1,2,5,2,3]
# target = 2
nums = [1,2,5,2,3]
target = 3
nums.sort()
print(nums)
list_out = []
for i in range(len(nums)):
    if nums[i]==target:
        list_out.append(i)
# return list_out
print(list_out)