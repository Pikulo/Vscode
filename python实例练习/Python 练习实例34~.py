# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/19  14:00
'''Python ��ϰʵ��34
    ��ϰ������ʹ��'''
'''
def hello_runoob():
    for i in range(3):
        print('RUNOOB')

hello_runoob()
'''
'''Python ��ϰʵ��37
    ��10������������'''
'''
s=input('�Կո�ֿ�������ʮ����\n')
lst=[int(n) for n in s.split()]
print(lst)
lst.sort()
for i in range(len(lst)):
    print(lst[i])
'''
'''Python ��ϰʵ��38
��Ŀ����һ��3*3�������Խ���Ԫ��֮�͡�'''
import numpy
a=int(input('��Ҫ���뼸*���ľ�������һ�����ּ��ɣ���\n'))
print('�����������ľ�������')
F=numpy.zeros((a,a))
print(F)
for i in range(a):
    for j in range(a):
        F[i][j]=int(input(''))
sum=0
for i in range(a):
    for j in range(a):
        print(F[i][j])
if a%2==0:
    for i in range(a):
        sum+=F[i][i]
    k=a
    for i in range(a):
        sum+=F[k-1][i]
        k-=1
else:
    minus=a//2
    for i in range(a):
        sum+=F[i][i]
    k=a
    for i in range(a):
        sum+=F[k-1][i]
        k-=1
    sum-=F[minus][minus]
print(sum)