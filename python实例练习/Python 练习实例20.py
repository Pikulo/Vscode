# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/13  14:57
'''题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？'''

for i in range(10):
    if i==0:
        clim_up = 50
        sum =100
    else:
        sum += clim_up * 2
        clim_up = clim_up / 2
print(sum,clim_up)






