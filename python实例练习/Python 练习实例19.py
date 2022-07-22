# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/13  13:59
'''题目：一个数如果恰好等于它的因子之和，
这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。'''
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
            print('{0}是完数'.format(a))
        # print(list[i])

    # print('---------------------')


