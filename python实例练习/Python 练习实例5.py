# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/10  13:11
'''��Ŀ��������������x,y,z���������������С���������'''
list=[]
for i in range(3):
    list.append(int(input('��������')))

list.sort()
for i in range(3):
    print(list[i])