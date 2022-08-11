nums = [8]
sum_out = 0
index = 0
while index < len(nums):
    if index+1<len(nums):
        while nums[index]>=nums[index+1]:
            nums[index+1]+=1
            sum_out+=1
    index+=1
print(nums)
print(sum_out)