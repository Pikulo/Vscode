# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/8  11:02
try:
    lst_name = ['����', '����', '�ܼ���', '��������', '������ԣ���', '����ת��Ƕ�', '����', '����', '��ͨ�����������', '������ʩ�걸��', 'VTSͨ�����񸲸���']
    score = []
    print('���������ش��')
    for i in range(0, 11):
        score.append(int(input('{0}:'.format(lst_name[i]))))
except ValueError:
    print('��������������ֵ')
    lst_name = ['����', '����', '�ܼ���', '��������', '������ԣ���', '����ת��Ƕ�', '����', '����', '��ͨ�����������', '������ʩ�걸��', 'VTSͨ�����񸲸���']
    score = []
    print('���������ش��')
    for i in range(0, 11):
        score.append(int(input('{0}:'.format(lst_name[i]))))
    # for i in range(0, 11):
    #     score.append(int(input('{0}:'.format(lst_name[i]))))
import numpy as np
F = np.zeros((11, 11))  # ����11��11�еľ��󣬳�ʼֵΪ0
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
for i in range(0,11):
    print('[{0}]��Ȩ��Ϊ:{1}'.format(lst_name[i],w[i]))
# ���ϴ�������ȷ

'''��׼����'''
matter_number=int(input('��Ҫ������������ݣ�exmple:3\n'))
M=np.zeros((matter_number, 11))  # ��¼�����ʵ������
for i in range(matter_number):
    print('�����{0}���������ص�ʵ��ֵ'.format(i+1))
    for j in range(0, 11):
            lst_name = ['����', '����', '�ܼ���', '��������', '������ԣ���', '����ת��Ƕ�', '����', '����', '��ͨ�����������', '������ʩ�걸��', 'VTSͨ�����񸲸���']
            M[i,j]=(float(input('{0}:'.format(lst_name[j]))))
print('----------------------------�������--------------------------')
print(M)
print('------------------------------------------------------')
'''�������ݸ������׺͵����ʾ�����'''
lst_upper=[10,16,4000,9,3.6,20,50,20,9,0.93,0.94]  # ������
lst_mid4=[]
lst_up=[8,13,2000,6,2.6,19.7,45,19,8,0.90,0.84]  # �ɽ�������
lst_mid3=[]
lst_mid_up_down=[] # ��ſɽ��ܺͲ��ɽ��ܵ��м�ȼ�
lst_mid2=[]
lst_down=[4,10,1000,5,2.3,16.3,20,10,5,0.75,0.64]  # �ɽ�������
lst_mid1=[]
lst_downer=[2,6,500,3,1.3,12.3,10,6,2,0.55,0.44]  # ������
for i in range(0,11):
    lst_mid_up_down.append((lst_up[i] + lst_down[i]) / 2)
for i in range(0,11):
    lst_mid1.append((lst_downer[i] + lst_down[i]) / 2)
    lst_mid2.append((lst_mid_up_down[i] + lst_down[i]) / 2)
    lst_mid3.append((lst_up[i] + lst_mid_up_down[i]) / 2)
    lst_mid4.append((lst_up[i] + lst_upper[i]) / 2)
print('------------------------�������------------------------------')
print(lst_mid1)
print(lst_mid2)
print(lst_mid3)
print(lst_mid4)

print('------------------------------------------------------')
for i in range(matter_number):  # �������ݵļ���ѭ��
    data = [0, 0, 0, 0]
    for k in range(4):
        sum = 0
        if k == 0:
            for j in range(0, 11):
                sum += (((lst_mid1[j] - M[i, j]) ** 2) * w[j])
            data[k] = sum ** 0.5
            print('--------------------------�������----------------------------')
            print(data)
            print('------------------------------------------------------')
        elif k == 1:
            for j in range(0, 11):
                sum += (((lst_mid2[j] - M[i, j]) ** 2) * w[j])
            data[k] = sum ** 0.5
            print('---------------------------�������---------------------------')
            print(data)
            print('------------------------------------------------------')
        elif k == 2:
            for j in range(0, 11):
                sum += (((lst_mid3[j] - M[i, j]) ** 2) * w[j])
            data[k] = sum ** 0.5
            print('--------------------------�������----------------------------')
            print(data)
            print('------------------------------------------------------')
        elif k == 3:
            for j in range(0, 11):
                sum += (((lst_mid4[j] - M[i, j]) ** 2) * w[j])
            data[k] = sum ** 0.5
            print('----------------------------�������--------------------------')
            print(data)
            print('------------------------------------------------------')
    data_copy = data[:]
    print('----------------------------�������--------------------------')
    print(data_copy)
    print('------------------------------------------------------')
    data.sort()
    print('-----------------------------�������-------------------------')
    print(data)
    print('------------------------------------------------------')
    for i in range(matter_number):
        if data_copy[0] == data[0]:
            print('��{0}�����ݵķ��յȼ�Ϊ1'.format(i+1))
        elif data_copy[1] == data[0]:
            print('��{0}�����ݵķ��յȼ�Ϊ2'.format(i+1))
        elif data_copy[2] == data[0]:
            print('��{0}�����ݵķ��յȼ�Ϊ3'.format(i+1))
        elif data_copy[3] == data[0]:
            print('��{0}�����ݵķ��յȼ�Ϊ4'.format(i+1))






