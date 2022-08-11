import numpy as np

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# idea1
# res = []
# matrix = np.rot90(matrix,3)
# for i in matrix:
#     print(i)
#     res.append(list(i))
# print(res)

# idea2
# res  = []
# matrix = matrix[::-1]
# print(matrix)
# for i in zip(*matrix):
#     print(i)
#     res.append(list(i))
# print(res)

'''上述方法虽然行，但都不是在原数组上进行的操作'''
# idea3
for i in range(len(matrix)):
    for j in range(i):
        print(i, j)
        print(matrix[i][j])
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
print(matrix)
for i in matrix:
    i.reverse()
print(matrix)
# return matrix
