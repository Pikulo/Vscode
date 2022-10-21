# 目标函数值计算
import math
import time
from matplotlib import pyplot as plt
import numpy as np


def f(C):
    # return 1/(C[0]**2+C[1]**2+C[2]**2+C[3]**2+1)
    return C[0]*math.sin(C[0])*2
# 初始化种群 C=[[[x],[v]]]
def init(N):
    C = np.zeros((N,2,1))
    global pBest,gBest
    for i in range(N):
        for j in range(1):
            C[i][0][j] = np.random.uniform(min,max) # x取值范围
            C[i][1][j] = np.random.uniform(-1,1)
        pBest[i] = C[i][0]
    gBest = pBest[np.argmax(Eval(C,N))].copy() #最大值用argmax，最小值用argmin
    return C
# 判断更新后是否还在问题空间内
def whether_out(C):
    for i in range(len(C)):
        for j in range(1):
            if C[i][0][j] < min : # x取值范围
                C[i][0][j] = min
            elif C[i][0][j] > max: # x取值范围
                C[i][0][j] = max
    return C

# 更新粒子的速度和位置
def update_C(C,N,w,c1,c2):
    '''
    C:种群 [[[x],[v]]]
    N:种群规模 100
    w:惯量权重 初始0.9，递减到0.4
    c1、c2:加速系数
    pBest: 每个粒子的历史最优位置[[x]]
    gBest: 全局最优位置[x]
    '''
#     print(C.shape)
    for i in range(N):
        for j in range(1):
            rand1 = np.random.random()
            rand2 = np.random.random()
            C[i][1][j] = w*C[i][1][j]+c1*rand1*(pBest[i][j]-C[i][0][j]) \
                         +c2*rand2*(gBest[j]-C[i][0][j])
            C[i][0][j] +=  C[i][1][j]
    C = whether_out(C)
    return C
        
# 评估函数
def Eval(C,N):
    temp = np.array([])
    for i in range(N):
        temp = np.append(temp,f(C[i][0]))
    print(temp)
    return temp
# 更新粒子的历史最优和全局最优
def update_best(C,N,fitness):
    '''
    pBest: 每个粒子的历史最优位置,[[x]]
    gBest: 全局最优位置,[x]
    fitness: 粒子当前适应值,[f(x)]
    '''
    global pBest,gBest
    
    for i in range(N):
        if fitness[i] > f(pBest[i]): # <表示求函数最小值，>表示最大值
            pBest[i] = C[i][0] 
        if fitness[i] > f(gBest): # <表示求函数最小值，>表示最大值
            gBest = C[i][0].copy()
# w线性递减
def w_degression(w,N):
    w -= 0.5/N
    return w
def PSO(length,N,w,c1,c2):
    global pBest,gBest
    global min,max
    min,max = 1,9
    C = init(N)
    list_out = []
    plt.figure()
    x1 = np.arange(1, 9, 0.000001)
    y1 = [x1*math.sin(x1)*2 for x1 in x1]
    # plt.plot(x1,y1)
#     print('gBest:',gBest)
    for i in range(length):
        C = update_C(C,N,w,c1,c2)
        fitness = Eval(C,N)
        update_best(C,N,fitness)
        # w=w_degression(w,N)
        list_out.append(f(gBest))
        plt.scatter(gBest,f(gBest))
        plt.pause(0.1)
        # if f(gBest)==1.75:
        #     break    
    
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    
    # plt.ylabel('最优值')
    # plt.xlabel('迭代次数')
    # plt.title('迭代趋势')
    x_label = []
    for i in range(1,length+1):
        x_label.append(i)
    
    # for i in range(length):
    #     plt.plot(x_label[:i],list_out[:i])
    #     plt.pause(0.1) # 暂停时间，越小绘制速度越快
    plt.show()
    return [f(gBest),gBest,i]
start = time.time()
print(start)
c1,c2 = 2,2
# length:迭代次数，N:种群规模
length,N=60,20
w=0.5
pBest = np.zeros((N,1))
gBest = np.zeros(1)
# PSO(length,N,w,c1,c2)
print(PSO(length,N,w,c1,c2))
end = time.time()
print(end)
print('PSO运行时间: %.2f s'%(end-start))
