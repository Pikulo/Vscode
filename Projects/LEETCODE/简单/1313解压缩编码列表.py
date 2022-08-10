nums = [1,1,2,3]
left=0
right=1
list_out=[]
while(right<len(nums)):
    for i in range(nums[left]):
        list_out.append(nums[right])
    left+=2
    right+=2
print(list_out)