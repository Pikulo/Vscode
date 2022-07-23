# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/7  18:51
def show_level():
    import numpy as np
    F = np.zeros((11, 11))  # 产生11行11列的矩阵，初始值为0
    try:
        lst_name = ['风速', '流速', '能见度', '船舶数量', '航道富裕宽度', '航道转向角度', '船速', '船龄', '交通流交叉会遇点', '助航设施完备率', 'VTS通航服务覆盖率']
        score = []
        print('给以下因素打分')
        for i in range(0, 11):
            score.append(int(input('{0}:'.format(lst_name[i]))))
    except ValueError:
        print('请重新输入整数值')
        for i in range(0, 11):
            score.append(int(input('{0}:'.format(lst_name[i]))))
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
    for i in range(0,10):
        print('[{0}]的权重为:{1}'.format(lst_name[i],w[i]))

show_level()






