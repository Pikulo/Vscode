
import numpy as np
from sklearn.datasets import make_classification
from sklearn.cluster import Birch
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler


data_o = pd.read_excel('聚类大作业--41天数据.xls', header=None) 
index_1 = 41
# print(data_o)

'''行列互换'''
data_o = pd.DataFrame(data_o.values.T,columns = data_o.index,index = data_o.columns) 
index_1 = 288
# print(data_o)

'归一化处理'
scaler = StandardScaler().fit(data_o.values)
features = scaler.transform(data_o.values)
scaled_features = pd.DataFrame(features)
data = scaled_features
# print(data)

# # data = data_o.copy()

'''绘图颜色'''
colors = ['#9D18D2', '#E1CD6D', '#56A2B5', '#5638F1', '#1331E5', '#888F7F', '#5D4EC9', '#2BABFA', '#8F83A9', '#4EF6E3', '#E6991A', '#669D8D', '#F45E3C', '#424D92', '#729BD5', '#9E65CD', '#7664CB', '#F81B15', '#1D98AC', '#C74B18', '#8DA429', '#9538AA', '#77F5E6', '#6EAE92', '#1FCD46', '#985CAA', '#73BBC6', '#D1E895', '#F2F244', '#4AE446', '#5338C3', '#441D55', '#5B7D69', '#D9DFE1', '#A3D74D', '#39B7B5', '#5FB888', '#E59E23', '#59D675', '#3C3D78', '#89B1ED']
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False 

'''调参'''
# vm = []
# n_cluster = 10
# for cluster in range(1,n_cluster):
#     birch = Birch(threshold = 0.5,branching_factor = 20,n_clusters=cluster)
#     birch.fit(data)  # 拟合模型
#     print(birch.labels_)
#     plt.plot(cluster,len(set(birch.labels_)),"r-o")
# plt.xlabel("n_cluster")
# plt.ylabel("聚类数目")
# plt.title("BIRCH聚类")
# plt.show()


'''聚类'''


'''聚类结果绘图'''
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X(天)')
ax.set_ylabel('Y(分钟)')
ax.set_zlabel('Z(值)')

'''row'''
if index_1 == 41:
    birch = Birch(threshold = 2,branching_factor = 20,n_clusters=3)
    birch.fit(data)  # 拟合模型
    data_o["label"] = birch.labels_ # 添加标签
    print(data_o)
    X = data.columns.values
    for i in range(len(X)):
        X[i]+=1
    print(X)
    list_label = list(set(birch.labels_))
    # print(list_label)
    for j in range(len(list_label)):
        df_0 = data_o[:][data_o.label == list_label[j]]
        Y = df_0.index.values
        print(Y)
        for n in range(len(Y)):
            Y[n]=(Y[n]+1)*5
        print(Y)
        Z = data_o[:][data_o['label'] == list_label[j]].iloc[:, 0:index_1].values
        print(Z)
        for i in range(len(Y)):
            ax.scatter(X, Y[i], Z[i], c=colors[j], s=60)
    ax.view_init(30, 185)
    plt.savefig('Birch_row_cluster{0}.svg'.format(len(set(birch.labels_))),format='svg')
    plt.savefig('Birch_row_cluster{0}.png'.format(len(set(birch.labels_))),format='png')
    plt.show()

'''columns''' # 更改
if index_1 == 288:
    birch = Birch(threshold = 2,branching_factor = 20,n_clusters=4)
    birch.fit(data)  # 拟合模型
    data_o["label"] = birch.labels_ # 添加标签
    print(data_o)
    X = data.columns.values
    for i in range(len(X)):
        X[i]=(X[i]+1)*5
    print(X)
    list_label = list(set(birch.labels_))
    # print(list_label)
    for j in range(len(list_label)):
        df_0 = data_o[:][data_o.label == list_label[j]]
        Y = df_0.index.values
        print(Y)
        Z = data_o[:][data_o['label'] == list_label[j]].iloc[:, 0:index_1].values
        print(Z)
        for i in range(len(Y)):
            ax.scatter(Y[i], X, Z[i], c=colors[j], s=60)
    print(set(birch.labels_))
    ax.view_init(30, 220)
    plt.savefig('Birch_row_col_clusters{0}.svg'.format(len(set(birch.labels_))),format='svg')
    plt.savefig('Birch_row_col_clusters{0}.png'.format(len(set(birch.labels_))),format='png')
    plt.show()




