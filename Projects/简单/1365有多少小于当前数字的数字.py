# nums=[8,1,2,2,3]
# nums = [6,5,4,8]
nums = [7,7,7,7]
list_out=[]
for i in nums:
    sum=0
    for j in nums:
        if i>j:
            sum+=1
    list_out.append(sum)
print(list_out)
# return list_out
