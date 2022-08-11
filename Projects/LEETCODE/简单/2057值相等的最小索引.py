# nums = [0,1,2]
# nums = [4,3,2,1]
# nums = [1,2,3,4,5,6,7,8,9,0]
# nums = [2,1,3,5,2]
nums = [1,1]
list_out = []
for i in range(len(nums)):
    if i%10 == nums[i]:
        list_out.append(i)
if list_out == []:
    # return -1
    print(-1)
else:
    # return min(list_out)
    print(min(list_out))