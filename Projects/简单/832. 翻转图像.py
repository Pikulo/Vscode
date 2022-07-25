image = [[1,1,0],[1,0,1],[0,0,0]]
image = [i[::-1] for i in image]
print(image)
# image = [j^1 for i in image for j in i]
image = [list(map(lambda x: x^1,image[i])) for i in range(len(image))]
print(image)