from multiprocessing.dummy import Array
import random
import numpy as np
from numpy import unique
from numpy import where
from sklearn.datasets import make_classification
from sklearn.cluster import DBSCAN
from matplotlib import pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
data_o = pd.read_excel('聚类大作业--41天数据.xls',header = None) 
for eps in np.arange(0.1,4.1,1):
    print(eps)
def Colourlist_Generator(n):
    Rangelist = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    n = int(n)
    Colours = []   #空列表，用于插入n个表示颜色的字符串
    j = 1
    while j <= n:            #循环n次，每次在0到14间随机生成6个数，在加“#”符号，次次插入列表
        colour = ""    #空字符串，用于插入字符组成一个7位的表示颜色的字符串（第一位为#，可最后添加）
        for i in range(6):
            colour += Rangelist[random.randint(0,14)]    #用randint生成0到14的随机整数作为索引
        colour = "#"+colour               #最后加上不变的部分“#”
        Colours.append(colour)
        j = j+1
    return Colours
print(Colourlist_Generator(41))