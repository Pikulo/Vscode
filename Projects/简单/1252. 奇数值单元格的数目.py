#法1
# m = 1
# n = 1
# indices = [[0,0],[0,0]]
m = 2
n = 2
indices = [[1,1],[0,0]]

#构造0矩阵

# list_nums = []
# for i in range(m):
#     list_nums.append([0]*n)
'''优化上述代码'''
list_nums = [[0]*n for _ in range(m)]#构造矩阵
print(list_nums)

# for i in range(len(indices)):
#     a=list_nums[indices[i][0]]
#     print(a)
#     a=[a[j]+1 for j in range(len(a))]
#     list_nums[indices[i][0]]=a
#     for k in range(m):
#         list_nums[k][indices[i][1]]+=1
    # print(list_nums)
'''优化上述代码'''
for i,j in indices:
    for a in range(n):
        list_nums[i][a]+=1
    for a in list_nums:
        a[j]+=1
print(list_nums)

# list_out = []
# for i in list_nums:
#     list_out+=i
# print(list_out)
# sum_out = 0
# for i in list_out:
#     if i%2!=0:
#         sum_out+=1
'''优化上述注释代码'''
sum_out = sum(j%2 for i in list_nums for j in i)
print(sum_out)

#力扣解法