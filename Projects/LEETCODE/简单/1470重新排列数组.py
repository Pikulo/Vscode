nums = [1,2,3,4,4,3,2,1]
n = 4

new_num=nums[n:]
nums=nums[:n]
print(nums,new_num)
i=0
j=0
while(i<n-1):
    nums.insert(i+1+j,new_num[i])
    i+=1
    j+=1
nums.append(new_num[n-1])
print(nums)