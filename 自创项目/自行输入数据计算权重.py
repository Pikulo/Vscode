# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/7  18:51
def show_level():
    import numpy as np
    F = np.zeros((11, 11))  # ����11��11�еľ��󣬳�ʼֵΪ0
    try:
        lst_name = ['����', '����', '�ܼ���', '��������', '������ԣ���', '����ת��Ƕ�', '����', '����', '��ͨ�����������', '������ʩ�걸��', 'VTSͨ�����񸲸���']
        score = []
        print('���������ش��')
        for i in range(0, 11):
            score.append(int(input('{0}:'.format(lst_name[i]))))
    except ValueError:
        print('��������������ֵ')
        for i in range(0, 11):
            score.append(int(input('{0}:'.format(lst_name[i]))))
    # arr_1 = input("ר�ҶԸ����ش�֣��Կո�ֿ�����\n")
    # score = [int(n) for n in arr_1.split()]  # ��arr_1��Ԫ���Կո񣨰��� \n��Ϊ�ָ���������score�б���
    for i in range(0, 11):
        for j in range(0, 11):
            if score[i] == score[j]:
                F[i, j] = 0.5  # �ӵ�i��j�п�ʼ����б�F
            elif score[i] > score[j]:
                F[i, j] = 1
            else:
                F[i, j] = 0  # ���������0��

    R = np.zeros((11, 11))  # ����11��11�еľ��󣬳�ʼֵΪ0
    '''����ϵ����F�����ģ��һ�¾���R'''
    list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(0, 11):
        list1[x] = sum(F[x, :])  # ��F�����е�x��Ԫ�صĺ͸�list1[x]

    for x in range(0, 11):
        for y in range(0, 11):
            R[x, y] = ((list1[x] - list1[y]) / 22) + 0.5  # �б任�Ľ��
    '''ָ��Ȩ�ؼ���'''
    list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    w = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(0, 11):
        list2[x] = sum(R[x, :]) - 0.5 - R[x, x]
    for x in range(0, 11):
        w[x] = 2 * list2[x] / 110
    for i in range(0,10):
        print('[{0}]��Ȩ��Ϊ:{1}'.format(lst_name[i],w[i]))

show_level()






