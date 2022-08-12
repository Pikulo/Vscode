matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]

# my idea
'''
list_row = []
list_col = []
for i in range(len(matrix)):
    index = False
    for j in matrix[i]:
       if j == 0:
        index = True
    if index:
        list_row.append(i)
print(list_row)
count_f = 0
for i in zip(*matrix):
    i = list(i)
    index = False
    for j in i:
       if j == 0:
        index = True
    if index:
        list_col.append(count_f)
    count_f+=1
print(list_col)
if len(list_row)!=0:
    for i in list_row:
        for j in range(len(matrix[i])):
            matrix[i][j] = 0
if len(list_col)!=0:
    for i in list_col:
        for j in range(len(matrix)):
            matrix[j][i]=0
print(matrix)
'''
# idea 2
m, n = len(matrix), len(matrix[0])
row = set()
col = set()
for i in range(m):
    for j in range(n):
        if not matrix[i][j]:
            row.add(i)
            col.add(j)
print(row,col) 
# 遍历修改矩阵值为零
for r in row:
    for j in range(n):
        matrix[r][j] = 0
for c in col:
    for i in range(m):
        matrix[i][c] = 0
print(matrix)