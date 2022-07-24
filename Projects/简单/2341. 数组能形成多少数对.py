nums = [0]
nums.sort()
print(nums)
sum_data = 0
def delist(sum_data,nums):
    for i in range(len(nums)):
        if i+1<len(nums):
            if nums[i]==nums[i+1]:
                sum_data+=1
                del nums[i+1]
                del nums[i]
                print(nums)
                return delist(sum_data,nums)
    return [sum_data,len(nums)]
print(delist(sum_data,nums))
