# nums = [3,1,2,2,2,1,3]
# k = 2
nums = [1,2,3,4]
k = 1
sum_out = 0
i=0
while(i<len(nums)):
    j=i+1
    while(j<len(nums)):
        print(nums[i],nums[j])
        if nums[i]==nums[j] and (i*j)%k==0:
            sum_out+=1
        j+=1
    i+=1
print(sum_out)
# return sum_out
    
