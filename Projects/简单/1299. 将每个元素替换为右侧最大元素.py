#题目：
# 给你一个数组 arr ，请你将每个元素用它右边最大的元素替换，如果是最后一个元素，用 -1 替换。
# 完成所有替换操作后，请你返回这个数组。
import time
start = time.time()
arr = [17,18,5,4,6,1]
# arr = [400]
for i in range(len(arr)):
    if i+1<len(arr):
        arr[i]=max(arr[i+1:])
    else:
        arr[i]=-1
print(arr)
# return arr
end = time.time()
print(end-start)

for i in range(len(arr)-2, -1,-1):#[arr)-2, -1],-1表示逆序输出。
    print(i)
    print(arr[i])