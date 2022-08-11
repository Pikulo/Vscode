# nums = [4,3,10,9,8]
# nums = [4,4,7,6,7]
nums = [6]
# sort默认升序，reverse=True表示降序。
nums.sort(reverse=True)
sum_stop = 0
sum_all_list = sum(nums)
res = []
index = 0
while sum_stop <= sum_all_list:
    res.append(nums[index])
    sum_stop+=nums[index]
    sum_all_list-=nums[index]
    index+=1
# print(res)
# return res