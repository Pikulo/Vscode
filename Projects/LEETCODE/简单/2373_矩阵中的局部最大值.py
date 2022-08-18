'''other idea'''
grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
n = len(grid)
for i in range(n-2):
    for j in range(n-2):
        grid[i][j] = max(max(row[j:j+3]) for row in grid[i:i+3])
    del grid[i][-2:]
del grid[-2:]
print(grid)