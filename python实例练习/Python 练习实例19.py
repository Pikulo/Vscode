# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/13  13:59
'''��Ŀ��һ�������ǡ�õ�����������֮�ͣ�
������ͳ�Ϊ"����"������6=1��2��3.����ҳ�1000���ڵ�����������'''
for j in range(1,1001):
    a = j
    list = []
    for i in range(1, a):
        if a % i == 0:
            list.append(i)
    sum = 0
    for i in range(len(list)):
        sum += list[i]
        if (sum) == a:
            print(list[:])
            print('{0}������'.format(a))
        # print(list[i])

    # print('---------------------')


