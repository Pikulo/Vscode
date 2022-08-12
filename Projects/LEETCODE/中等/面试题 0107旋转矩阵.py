matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
for i in range(len(matrix)):
    for j in range(i):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
for i in matrix:
    i.reverse()
print(matrix)
# return matrix

