# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/10  13:56
'''��Ŀ���ж�101-200֮���ж��ٸ����������������������'''
for i in range(101,201):
    spot = 0
    for j in range(2,i):
        if i%j==0:
            spot+=1
    if spot==0:
        print('{0}������'.format(i))





