# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/8  11:02
import numpy as np
matter_number=int(input('��Ҫ�������������\n�����ش�ֵ�ֵ\n���ص�ʵ��ֵ\n'))
M=np.zeros((matter_number, 7))  # ��¼�����ʵ������
lst_name = ['����', '����', '�ܼ���', '����������', '������ԣ���', '����', '��ͨ�����������']
score = []
arr_1 = input("")  # ר�ҶԸ����ش�֣��Կո�ֿ�����
score = [float(n) for n in arr_1.split()]  # ��arr_1��Ԫ���Կո񣨰��� \n��Ϊ�ָ���������score�б���
F = np.zeros((7, 7))  # ����7��7�еľ��󣬳�ʼֵΪ0
for i in range(0, 7):
    for j in range(0, 7):
        if score[i] == score[j]:
            F[i, j] = 0.5  # �ӵ�i��j�п�ʼ����б�F
        elif score[i] > score[j]:
            F[i, j] = 1
        else:
            F[i, j] = 0  # �����0
R = np.zeros((7, 7))  # ����11��11�еľ��󣬳�ʼֵΪ0
'''����ϵ����F�����ģ��һ�¾���R'''
list1 = [0, 0, 0, 0, 0, 0, 0]
for x in range(0, 7):
    list1[x] = sum(F[x, :])  # ��F�����е�x��Ԫ�صĺ͸�list1[x]
for x in range(0, 7):
    for y in range(0, 7):
        R[x, y] = ((list1[x] - list1[y]) / 14) + 0.5  # �б任�Ľ��
'''ָ��Ȩ�ؼ���'''
list2 = [0, 0, 0, 0, 0, 0, 0]
w = [0, 0, 0, 0, 0, 0, 0]
for x in range(0, 7):
    list2[x] = sum(R[x, :]) - 0.5
for x in range(0, 7):
    w[x] = 2 * list2[x] / 42
for i in range(0,7):
    print('[{0}]��Ȩ��Ϊ:{1}'.format(lst_name[i],w[i]))
# ���ϴ�������ȷ
'''��׼����'''
for i in range(matter_number):
    arr_2 = input("")
    score_1 = [float(n) for n in arr_2.split()]  # ��arr_1��Ԫ���Կո񣨰��� \n��Ϊ�ָ���������score�б���
    M[i, :]=score_1
'''�������ݸ������׺͵����ʾ�����'''
lst_upper=[13.62,3.95,0.57,4,8.36,12,4]  # ������
lst_mid4=[]
lst_up=[11.17,3.19,1.36,3.5,12.73,9.84,3.5]  # �ɽ�������
lst_mid3=[]
lst_mid_up_down=[] # ��ſɽ��ܺͲ��ɽ��ܵ��м�ȼ�
lst_mid2=[]
lst_down=[6.72,1.67,2.94,2.5,21.45,5.52,2]  # �ɽ�������
lst_mid1=[]
lst_downer=[3.82,0.91,3.73,2,25.82,3.36,1]  # ������
for i in range(0,7):
    lst_mid_up_down.append((lst_up[i] + lst_down[i]) / 2)
# print(lst_mid_up_down)
for i in range(0,7):
    lst_mid1.append((lst_downer[i] + lst_down[i]) / 2)
    lst_mid2.append((lst_mid_up_down[i] + lst_down[i]) / 2)
    lst_mid3.append((lst_up[i] + lst_mid_up_down[i]) / 2)
    lst_mid4.append((lst_up[i] + lst_upper[i]) / 2)
for i in range(matter_number):  # �������ݵļ���ѭ��
    data = [0, 0, 0, 0]
    for k in range(4):
        sum = 0
        if k == 0:
            for j in range(0, 7):
                # print(M[i,j])
                sum += (((lst_mid1[j] - M[i, j]) ** 2) * w[j])
            data[k] = sum ** 0.5
        elif k == 1:
            for j in range(0, 7):
                sum += (((lst_mid2[j] - M[i, j]) ** 2) * w[j])
            data[k] = sum ** 0.5
        elif k == 2:
            for j in range(0, 7):
                sum += (((lst_mid3[j] - M[i, j]) ** 2) * w[j])
            data[k] = sum ** 0.5
        elif k == 3:
            for j in range(0, 7):
                sum += (((lst_mid4[j] - M[i, j]) ** 2) * w[j])
            data[k] = sum ** 0.5
    data_copy = data[:]
    # print(data_copy)
    data.sort()
    # print(data)
    if data_copy[0] == data[0]:
        print('��{0}�����ݵķ��յȼ�Ϊ1'.format(i+1))
    elif data_copy[1] == data[0]:
        print('��{0}�����ݵķ��յȼ�Ϊ2'.format(i+1))
    elif data_copy[2] == data[0]:
        print('��{0}�����ݵķ��յȼ�Ϊ3'.format(i+1))
    elif data_copy[3] == data[0]:
        print('��{0}�����ݵķ��յȼ�Ϊ4'.format(i+1))
'''�������ݣ�2
7 7 9 5 6 3 6 
9 15 300 6 10 16 9
2 7 5000 0 200 8 0


'''
# WG = np.zeros((15, 15))
# print(WG)




