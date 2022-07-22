#奇数、连续
from functools import reduce


arr = [10]
list_num=[]
k=1
while(k<=len(arr)):
    list_num.append(k)
    k+=2
print(list_num)
sum=0
for j in list_num:
    i=0
    while(i+j<len(arr)+1):
        print(arr[i:i+j],type(arr[i:i+j]))
        # sum+=sum(arr[i:i+j])
        a=reduce(lambda x,y: x+y,arr[i:i+j])
        sum+=a
        i+=1
print(sum)
