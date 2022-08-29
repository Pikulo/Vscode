nums = [2, 5, 1, 3, 4, 7]
n = 3
nums = [1, 2, 3, 4, 4, 3, 2, 1]
n = 4

# my idea
res = []
i = 0
while i < n:
    res.append(nums[i])
    res.append(nums[i+n])
    i += 1
print(res)
# return res

# other idea
nums[::2], nums[1::2] = nums[:n], nums[n:]
print(nums)
# return nums