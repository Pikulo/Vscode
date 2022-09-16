from random import random
import numpy as np
# idea1
def roulette(select_list):
    sum_val = sum(select_list)
    random_val = random()
    probability = 0  # 累计概率
    for i in range(len(select_list)):
        probability += select_list[i] / sum_val  # 加上该个体的选中概率
        if probability >= random_val:
            return i  # 返回被选中的下标
        else:
            continue

# 适应度值
select_list = [0.23, 0.65, 0.38, 0.05, 0.14, 0.76, 0.99, 0.76, 0.56, 0.77]
for j in range(3):
    res = [0]*len(select_list)
    for i in range(100):
        re = roulette(select_list)
        res[re] += 1  # 选中坐标加1
    print(res)

 # idea2
res = []
for i in range(10):
    x=np.random.choice(a=[1,2,3,4],size=1,replace=True,p=[0.1,0.2,0.1,0.6]) # p表示概率，和为1
    res.append(int(x))
print(res)
