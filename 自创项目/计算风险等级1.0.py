# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/8  11:02
import numpy as np
matter_number=int(input('你要输入多少组数据\n给因素打分的值\n因素的实际值\n'))
M=np.zeros((matter_number, 7))  # 记录键入的实际数据
lst_name = ['风速', '流速', '能见度', '允许船舶数量', '航道富裕宽度', '船速', '交通流交叉会遇点']
score = []
arr_1 = input("")  # 专家对各因素打分（以空格分开）：
score = [float(n) for n in arr_1.split()]  # 把arr_1内元素以空格（包含 \n）为分隔符，放入score列表里
F = np.zeros((7, 7))  # 产生7行7列的矩阵，初始值为0
for i in range(0, 7):
    for j in range(0, 7):
        if score[i] == score[j]:
            F[i, j] = 0.5  # 从第i行j列开始填充列表F
        elif score[i] > score[j]:
            F[i, j] = 1
        else:
            F[i, j] = 0  # 这儿是0
R = np.zeros((7, 7))  # 产生11行11列的矩阵，初始值为0
'''将关系矩阵F改造成模糊一致矩阵R'''
list1 = [0, 0, 0, 0, 0, 0, 0]
for x in range(0, 7):
    list1[x] = sum(F[x, :])  # 把F矩阵中第x行元素的和给list1[x]
for x in range(0, 7):
    for y in range(0, 7):
        R[x, y] = ((list1[x] - list1[y]) / 14) + 0.5  # 行变换的结果
'''指标权重计算'''
list2 = [0, 0, 0, 0, 0, 0, 0]
w = [0, 0, 0, 0, 0, 0, 0]
for x in range(0, 7):
    list2[x] = sum(R[x, :]) - 0.5
for x in range(0, 7):
    w[x] = 2 * list2[x] / 42
for i in range(0,7):
    print('[{0}]的权重为:{1}'.format(lst_name[i],w[i]))
# 以上代码检查正确
'''标准矩阵'''
for i in range(matter_number):
    arr_2 = input("")
    score_1 = [float(n) for n in arr_2.split()]  # 把arr_1内元素以空格（包含 \n）为分隔符，放入score列表里
    M[i, :]=score_1
'''以下数据根据文献和调查问卷填入'''
lst_upper=[13.62,3.95,0.57,4,8.36,12,4]  # 最上限
lst_mid4=[]
lst_up=[11.17,3.19,1.36,3.5,12.73,9.84,3.5]  # 可接受上限
lst_mid3=[]
lst_mid_up_down=[] # 存放可接受和不可接受的中间等级
lst_mid2=[]
lst_down=[6.72,1.67,2.94,2.5,21.45,5.52,2]  # 可接受下限
lst_mid1=[]
lst_downer=[3.82,0.91,3.73,2,25.82,3.36,1]  # 最下限
for i in range(0,7):
    lst_mid_up_down.append((lst_up[i] + lst_down[i]) / 2)
# print(lst_mid_up_down)
for i in range(0,7):
    lst_mid1.append((lst_downer[i] + lst_down[i]) / 2)
    lst_mid2.append((lst_mid_up_down[i] + lst_down[i]) / 2)
    lst_mid3.append((lst_up[i] + lst_mid_up_down[i]) / 2)
    lst_mid4.append((lst_up[i] + lst_upper[i]) / 2)
for i in range(matter_number):  # 几组数据的几次循环
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
        print('第{0}组数据的风险等级为1'.format(i+1))
    elif data_copy[1] == data[0]:
        print('第{0}组数据的风险等级为2'.format(i+1))
    elif data_copy[2] == data[0]:
        print('第{0}组数据的风险等级为3'.format(i+1))
    elif data_copy[3] == data[0]:
        print('第{0}组数据的风险等级为4'.format(i+1))
'''测试数据：2
7 7 9 5 6 3 6 
9 15 300 6 10 16 9
2 7 5000 0 200 8 0


'''
# WG = np.zeros((15, 15))
# print(WG)




