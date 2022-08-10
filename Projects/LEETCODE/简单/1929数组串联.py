nums=[1,3,2,1]
ans=[0]*len(nums)*2
print(ans)
for i in range(len(nums)):
    ans[i]=nums[i]
    ans[i+len(nums)]=nums[i]
print(ans)
