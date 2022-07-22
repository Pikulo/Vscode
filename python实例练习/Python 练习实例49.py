# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/22  13:14
'''
#  练习49
''题目：使用lambda来创建匿名函数。''
add=lambda x,y: x+y

print(add(1,2))
'''
'''
# 练习50
'题目：输出一个随机数。'
import random
print(random.uniform(0,10))  # uniform() 方法将随机生成下一个实数，它在 [x, y] 范围内。
print(int(random.uniform(1,5)))
print(random.sample(range(0,10),10))  # 用sample输出10个0到9的不相等随机数
print(random.randint(0,10))
'''
# 56

# 转置矩阵
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(len(matrix[0]))
a=len(matrix)
b=len(matrix[0])
print(matrix)
import numpy
matrix_copy=numpy.zeros((b,a),dtype=int)
# print(matrix_copy)
for i in range(a):
    for j in range(b):
        matrix_copy[j][i]=matrix[i][j]
print(matrix_copy.tolist())

