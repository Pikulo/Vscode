# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/8  11:02
try:
    lst_name = ['风速', '流速', '能见度', '船舶数量', '航道富裕宽度', '航道转向角度', '船速', '船龄', '交通流交叉会遇点', '助航设施完备率', 'VTS通航服务覆盖率']
    score = []
    print('给以下因素打分')
    for i in range(0, 11):
        score.append(int(input('{0}:'.format(lst_name[i]))))
except ValueError:
    print('请重新输入整数值')
    lst_name = ['风速', '流速', '能见度', '船舶数量', '航道富裕宽度', '航道转向角度', '船速', '船龄', '交通流交叉会遇点', '助航设施完备率', 'VTS通航服务覆盖率']
    score = []
    print('给以下因素打分')
    for i in range(0, 11):
        score.append(int(input('{0}:'.format(lst_name[i]))))
    # for i in range(0, 11):
    #     score.append(int(input('{0}:'.format(lst_name[i]))))
import numpy as np
F = np.zeros((11, 11))  # 产生11行11列的矩阵，初始值为0
# arr_1 = input("专家对各因素打分（以空格分开）：\n")
# score = [int(n) for n in arr_1.split()]  # 把arr_1内元素以空格（包含 \n）为分隔符，放入score列表里
for i in range(0, 11):
    for j in range(0, 11):
        if score[i] == score[j]:
            F[i, j] = 0.5  # 从第i行j列开始填充列表F
        elif score[i] > score[j]:
            F[i, j] = 1
        else:
            F[i, j] = 0  # 这儿不该是0吗？

R = np.zeros((11, 11))  # 产生11行11列的矩阵，初始值为0
'''将关系矩阵F改造成模糊一致矩阵R'''
list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in range(0, 11):
    list1[x] = sum(F[x, :])  # 把F矩阵中第x行元素的和给list1[x]

for x in range(0, 11):
    for y in range(0, 11):
        R[x, y] = ((list1[x] - list1[y]) / 22) + 0.5  # 行变换的结果
'''指标权重计算'''
list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
w = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in range(0, 11):
    list2[x] = sum(R[x, :]) - 0.5 - R[x, x]
for x in range(0, 11):
    w[x] = 2 * list2[x] / 110
for i in range(0,11):
    print('[{0}]的权重为:{1}'.format(lst_name[i],w[i]))
# 以上代码检查正确

'''标准矩阵'''
matter_number=int(input('你要输入多少组数据？example:3\n'))
M=np.zeros((matter_number, 11))  # 记录键入的实际数据
for i in range(matter_number):
    print('输入第{0}次以下因素的实际值'.format(i+1))
    for j in range(0, 11):
            lst_name = ['风速', '流速', '能见度', '船舶数量', '航道富裕宽度', '航道转向角度', '船速', '船龄', '交通流交叉会遇点', '助航设施完备率', 'VTS通航服务覆盖率']
            M[i,j]=(float(input('{0}:'.format(lst_name[j]))))
print('----------------------------检查数据--------------------------')
print(M)
print('------------------------------------------------------')
'''以下数据根据文献和调查问卷填入'''
lst_upper=[10,16,4000,9,3.6,20,50,20,9,0.93,0.94]  # 最上限
lst_mid4=[]
lst_up=[8,13,2000,6,2.6,19.7,45,19,8,0.90,0.84]  # 可接受下限
lst_mid3=[]
lst_mid_up_down=[] # 存放可接受和不可接受的中间等级
lst_mid2=[]
lst_down=[4,10,1000,5,2.3,16.3,20,10,5,0.75,0.64]  # 可接受上限
lst_mid1=[]
lst_downer=[2,6,500,3,1.3,12.3,10,6,2,0.55,0.44]  # 最下限
for i in range(0,11):
    lst_mid_up_down.append((lst_up[i] + lst_down[i]) / 2)
for i in range(0,11):
    lst_mid1.append((lst_downer[i] + lst_down[i]) / 2)
    lst_mid2.append((lst_mid_up_down[i] + lst_down[i]) / 2)
    lst_mid3.append((lst_up[i] + lst_mid_up_down[i]) / 2)
    lst_mid4.append((lst_up[i] + lst_upper[i]) / 2)
print('------------------------检查数据------------------------------')
print(lst_mid1)
print(lst_mid2)
print(lst_mid3)
print(lst_mid4)

print('------------------------------------------------------')
for i in range(matter_number):  # 几组数据的几次循环
    data = [0, 0, 0, 0]
    for k in range(4):
        sum = 0
        if k == 0:
            for j in range(0, 11):
                sum += (((lst_mid1[j] - M[i, j]) ** 2) * w[j])
            data[k] = sum ** 0.5
            print('--------------------------检查数据----------------------------')
            print(data)
            print('------------------------------------------------------')
        elif k == 1:
            for j in range(0, 11):
                sum += (((lst_mid2[j] - M[i, j]) ** 2) * w[j])
            data[k] = sum ** 0.5
            print('---------------------------检查数据---------------------------')
            print(data)
            print('------------------------------------------------------')
        elif k == 2:
            for j in range(0, 11):
                sum += (((lst_mid3[j] - M[i, j]) ** 2) * w[j])
            data[k] = sum ** 0.5
            print('--------------------------检查数据----------------------------')
            print(data)
            print('------------------------------------------------------')
        elif k == 3:
            for j in range(0, 11):
                sum += (((lst_mid4[j] - M[i, j]) ** 2) * w[j])
            data[k] = sum ** 0.5
            print('----------------------------检查数据--------------------------')
            print(data)
            print('------------------------------------------------------')
    data_copy = data[:]
    print('----------------------------检查数据--------------------------')
    print(data_copy)
    print('------------------------------------------------------')
    data.sort()
    print('-----------------------------检查数据-------------------------')
    print(data)
    print('------------------------------------------------------')
    for i in range(matter_number):
        if data_copy[0] == data[0]:
            print('第{0}组数据的风险等级为1'.format(i+1))
        elif data_copy[1] == data[0]:
            print('第{0}组数据的风险等级为2'.format(i+1))
        elif data_copy[2] == data[0]:
            print('第{0}组数据的风险等级为3'.format(i+1))
        elif data_copy[3] == data[0]:
            print('第{0}组数据的风险等级为4'.format(i+1))






