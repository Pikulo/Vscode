# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/22  13:14
'''
#  ��ϰ49
''��Ŀ��ʹ��lambda����������������''
add=lambda x,y: x+y

print(add(1,2))
'''
'''
# ��ϰ50
'��Ŀ�����һ���������'
import random
print(random.uniform(0,10))  # uniform() ���������������һ��ʵ�������� [x, y] ��Χ�ڡ�
print(int(random.uniform(1,5)))
print(random.sample(range(0,10),10))  # ��sample���10��0��9�Ĳ���������
print(random.randint(0,10))
'''
# 56

# ת�þ���
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

