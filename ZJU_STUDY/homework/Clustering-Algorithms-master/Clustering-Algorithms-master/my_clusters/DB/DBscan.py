from multiprocessing.dummy import Array
import numpy as np
from numpy import unique
from numpy import where
from sklearn.datasets import make_classification
from sklearn.cluster import DBSCAN
from matplotlib import pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.metrics.cluster import v_measure_score
# 参考文章:https://mp.weixin.qq.com/s/afECb9fHOJBM6zNGHyYPQg

data_o = pd.read_excel('聚类大作业--41天数据.xls', header=None) 
index_1 = 41 # 列数
print(data_o) #288行（以分钟分组）
'''行列互换'''
data_o = pd.DataFrame(data_o.values.T,columns = data_o.index,index = data_o.columns) 
index_1 = 288 # 列数
print(data_o) # 41行（以天分组）
'归一化处理'
scaler = StandardScaler().fit(data_o.values)
features = scaler.transform(data_o.values)
scaled_features = pd.DataFrame(features)
data = scaled_features
print(data)

# data = data_o.copy()
# print(data)

'''绘图颜色'''
colors = ['#9D18D2', '#E1CD6D', '#56A2B5', '#5638F1', '#1331E5', '#888F7F', '#5D4EC9', '#2BABFA', '#8F83A9', '#4EF6E3', '#E6991A', '#669D8D', '#F45E3C', '#424D92', '#729BD5', '#9E65CD', '#7664CB', '#F81B15', '#1D98AC', '#C74B18', '#8DA429', '#9538AA', '#77F5E6', '#6EAE92', '#1FCD46', '#985CAA', '#73BBC6', '#D1E895', '#F2F244', '#4AE446', '#5338C3', '#441D55', '#5B7D69', '#D9DFE1', '#A3D74D', '#39B7B5', '#5FB888', '#E59E23', '#59D675', '#3C3D78', '#89B1ED']


'''调参'''
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False 
# label_eps = []
# # fig = plt.subplots(3,3)
# fig = plt.figure(figsize=(10,10))
# num_plt = 1
# for eps in np.arange(0.1,2.8,0.3):
#     # 迭代不同的min_samples值
#     plt.subplot(3,3,num_plt)
#     x_sam = []
#     num_typ = []
#     for min_samples in range(1,10):
#         x_sam.append(min_samples)
#         db = DBSCAN(eps=eps,min_samples = min_samples)
#         db.fit(data.values)
#         data_o["label"] = db.labels_
#         ## 获取聚类后的类别标签
#         db_pre_lab = db.labels_
#         num_typ.append(len(set(db.labels_)))
#         # plt.plot(min_samples,num)
#         # print(db_pre_lab)
#         print("参数eps取值为:",eps,"参数min_samples取值为:",min_samples)
#         print("每簇包含的样本数量:",np.unique(db_pre_lab,return_counts = True))
#         # print("聚类效果V测度: %.4f"%v_measure_score(data_o[:]['label'],db_pre_lab)) # 数据不包含类比
#         print("============================")
#     plt.plot(x_sam, num_typ, linestyle='-', label='eps:{0}'.format(round(eps,2)),color=colors[num_plt-1])
#     plt.xlabel('Min_samples')
#     plt.ylabel('Number of clusters')
#     plt.legend()
#     fig.tight_layout()
#     num_plt+=1
# plt.savefig('compare_eps_minsamples.svg',format='svg')
# plt.savefig('compare_eps_minsamples.png',format='png')
# plt.show()




'''聚类'''
db = DBSCAN(eps=1,min_samples = 5)
db.fit(data.values)
print( db.labels_)
data_o["label"] = db.labels_ # 添加标签
print(data_o)
# print(data.shape)

'''聚类结果绘图'''
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

'''row'''
# X = data.columns.values
# for i in range(len(X)):
#     X[i]+=1
# print(X)
# list_label = list(set(db.labels_))
# # print(list_label)
# for j in range(len(list_label)):
#     df_0 = data_o[:][data_o.label == list_label[j]]
#     Y = df_0.index.values
#     print(Y)
#     for n in range(len(Y)):
#         Y[n]=(Y[n]+1)*5
#     print(Y)
#     Z = data_o[:][data_o['label'] == list_label[j]].iloc[:, 0:index_1].values
#     print(Z)
#     for i in range(len(Y)):
#         ax.scatter(X, Y[i], Z[i], c=colors[j], s=60)

'''columns''' # 更改
X = data.index.values
for i in range(len(X)):
    X[i]+=1
print(X)
list_label = list(set(db.labels_))
# print(list_label)
for j in range(len(list_label)):
    Y = data.columns.values
    for n in range(len(Y)):
        Y[n]=(Y[n]+1)*5
    print(Y)
    Z = data_o[:][data_o['label'] == list_label[j]].iloc[:, 0:index_1].values
    print(Z)
    for i in range(len(Y)):
        ax.scatter(X, Y[i], Z[i], c=colors[j], s=60)

# ax.view_init(30, 220)
# plt.savefig('DB_eps1_minsamples5.svg',format='svg')
# plt.savefig('DB_eps1_minsamples5.png',format='png')
# plt.show()