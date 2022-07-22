from numpy import sort


nums=[8,1,2,2,3]
# nums = [6,5,4,8]
# nums = [7,7,7,7]
list_out=[]
for i in nums:
    sum=0
    for j in nums:
        if i>j:
            sum+=1
    list_out.append(sum)
print(list_out)
# return list_out
#法2：利用哈希表
hashmap={}
arr=sorted(nums)
print(arr)
for j in range(len(arr)):
    if arr[j] not in hashmap:
        hashmap[arr[j]]=j
print(hashmap)
print(map(lambda x: hashmap[x],nums))
#<map object at 0x0000022E0501BAF0>
print(list(map(lambda x: hashmap[x],nums)))