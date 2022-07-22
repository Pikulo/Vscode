from numpy import insert


nums = [1,2,3,4,0]
index = [0,1,2,3,0]
target=[]
for i in range(len(index)):
    target.insert(index[i],nums[i])
print(target)