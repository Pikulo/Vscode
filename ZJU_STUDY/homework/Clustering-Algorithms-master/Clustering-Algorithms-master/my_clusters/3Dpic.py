# dbscan 聚类
from multiprocessing.dummy import Array
import numpy as np
from numpy import unique
from numpy import where
from sklearn.datasets import make_classification
from sklearn.cluster import DBSCAN
from matplotlib import pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
# 定义数据集
# X, _ = make_classification(
#    n_samples=1000, 
#     n_features=2, 
#     n_informative=2, 
#     n_redundant=0,
#     n_clusters_per_class=1, 
#     random_state=4)
# print(type(X))
data = pd.read_excel('聚类大作业--41天数据.xls', header=None) 
columns = data.columns
dataset = []
for c in columns:
    d = data[c].values.tolist()
    dataset.append(d)
Z = []
for i in range(41):
    for j in dataset[i]:
        Z.append(j)
Y = []
for i in range(41):
    for j in range(1,289):
        Y.append(j)
X = []
for i in range(41):
    for j in range(288):
        X.append(i)
# print(X)
# data_array = np.arange(5,3,0)
# print(data_array)
lis = []
for i in range(10*288):
    lis.append(X[i])
    lis.append(Y[i])
    lis.append(Z[i])
data_array = np.reshape(lis,(10*288,3))

'''绘制3D图片'''
# columns = data.columns
# dataset = []
# for c in columns:
#     d = data[c].values.tolist()
#     dataset.append(d)
# # print(dataset[0])
# n = 15
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# k = 1
# for j in range(n):
#     Z = dataset[j]
#     print(Z)
#     X= []
#     for i in range(k+j,k+1+j):
#         X.append(i)
#         print(X)
#     Y= []
#     for i in range(1,289):
#         Y.append(i)
#         print(Y)
#     ax.scatter(X,Y,Z)
# plt.show()

# # 定义模型
model = DBSCAN(eps=2000, min_samples=9)
# 模型拟合与聚类预测
yhat = model.fit_predict(data_array)
print(yhat)
# 检索唯一群集
clusters = unique(yhat)
# 为每个群集的样本创建散点图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for cluster in clusters:
  # 获取此群集的示例的行索引
  row_ix = where(yhat == cluster)
  # 创建这些样本的散点图
  ax.scatter(data_array[row_ix, 0], data_array[row_ix, 1],data_array[row_ix, 2])
  # 绘制散点图
plt.show()