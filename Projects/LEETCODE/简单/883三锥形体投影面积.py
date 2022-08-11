# grid = [[1,2],[3,4]]
# grid = [[2]]
grid = [[1,0],[0,2]]
# print(sum([True]))
sum_xy = sum(i>0 for j in grid for i in j) # sum将True看作1，将false看作0
sum_xz = sum(map(max,grid))
sum_yz = sum(map(max,zip(*grid)))
print(sum_xy,sum_xz,sum_yz)
print(sum_xy+sum_xz+sum_yz)