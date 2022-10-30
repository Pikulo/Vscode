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
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.metrics.cluster import v_measure_score
# 参考文章:https://mp.weixin.qq.com/s/afECb9fHOJBM6zNGHyYPQg

data_o = pd.read_excel('聚类大作业--41天数据.xls', header=None) 
print(data_o)
'''行列互换'''
# data_o = pd.DataFrame(data_o.values.T,columns = data_o.index,index = data_o.columns) 
# print(data_o)
'归一化处理'
scaler = StandardScaler().fit(data_o.values)
features = scaler.transform(data_o.values)
scaled_features = pd.DataFrame(features)
data = scaled_features
print(data)


'''调参'''
# label_eps = []
# fig = plt.figure(figsize=(8,8))
# for eps in np.arange(0.05,1,0.05):
#     # 迭代不同的min_samples值
#     x_sam = []
#     num_typ = []
#     for min_samples in range(1,8):
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
#     plt.plot(x_sam, num_typ, linestyle='-', label='{0}'.format(eps))
# plt.legend()
# fig.tight_layout()
# plt.show()




'''聚类'''
db = DBSCAN(eps=0.1,min_samples = 10)
db.fit(data.values)
print( db.labels_)
data_o["label"] = db.labels_ # 添加标签
print(data_o)
# print(data.shape)

'''聚类结果绘图'''
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
X = data.columns.values
colors = ['blue','red','green','yellow']
list_label = list(set(db.labels_))
print(list_label)
for j in range(len(list_label)):
    df_0 = data_o[:][data_o.label == list_label[j]]
    Y = df_0.index.values
    Z = data_o[:][data_o['label'] == list_label[j]].iloc[:, 0:41].values
    for i in range(len(Y)):
        ax.scatter(X, Y[i], Z[i], c=colors[j], s=60)
ax.view_init(30, 185)
# plt.savefig('KM.svg',format='svg')
plt.show()