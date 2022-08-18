mat = [[1,2,3],[4,5,6],[7,8,9]]
'''other idea'''
# m, n, ans = len(mat), len(mat[0]), []
# for k in range(m + n - 1):
#     if not k % 2:
#         ans += [mat[x][k-x] for x in range(min(m - 1, k), max(-1, k - n),-1)]
#     else:
#         ans += [mat[x][k-x] for x in range(max(0, k - n + 1), min(k + 1, m))]
# # return ans
# print(ans)

'''my idea'''
# 分析
# 对角线数量：m+n-1 \ 以右上对角线为正的话，对角线方向顺序为：+/-/+/-......
# 右上角对角线特点：元素的m、n索引之和为定值（补充，左上角对角线之差为定值）

res =[]
n = len(mat) + len(mat[0]) -1
# for i in range(n):
for i in range(2,-1,-1):
    print(i)

          