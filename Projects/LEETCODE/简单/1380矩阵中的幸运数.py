# 在同一行的所有元素中最小，在同一列的所有元素中最大
# matrix = [[3,7,8],[9,11,13],[15,16,17]]
# matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# matrix = [[7,8],[1,2]]
matrix = [[3,6],[7,1],[5,2],[4,8]]
# my idea
# 先取出每一行最小的数，再看这组数里最大的数。
min_num = []
for i in matrix:
    # print(min(i))
    min_num.append(min(i))
print(max(min_num))
# return max(min_num)
'''结果错误'''

'''大佬的思路'''
min_row = [min(i) for i in matrix]
max_col = [max(i) for i in zip(*matrix)] # 获得每列的值
print(min_row, max_col)
print([i for i in min_row if i in max_col])
# return [i for i in min_row if i in max_col]
