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
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# 参考文章:https://mp.weixin.qq.com/s/afECb9fHOJBM6zNGHyYPQg

data_o = pd.read_excel('聚类大作业--41天数据.xls', header=None) 
index_1 = 41
# print(data_o)



'''行列互换'''
# data_o = pd.DataFrame(data_o.values.T,columns = data_o.index,index = data_o.columns) 
# index_1 = 288
# # print(data_o)

'归一化处理'
scaler = StandardScaler().fit(data_o.values)
features = scaler.transform(data_o.values)
scaled_features = pd.DataFrame(features)
data = scaled_features



'''降二维图像'''
# pca = PCA(n_components=2)
# X_r = pca.fit(data).transform(data)
# # print(X_r)
# data = pd.DataFrame(X_r)

# # tsne = TSNE(n_components = 2,perplexity =25,
# #             early_exaggeration =3,random_state=123) 
# # data = pd.DataFrame(tsne.fit_transform(X_r))
# print(data)

# kmeans = KMeans(n_init = 10, n_clusters = 3, init='k-means++',algorithm='lloyd')
# clusters = kmeans.fit_predict(data.iloc[:,:]) #fit_predict方法计算聚类中心并且预测每个样本的聚类索引
# print(clusters) # == print(kmeans.labels_) # 聚类标签/结果
# data["label"] = clusters # 添加标签

# colors = ['blue','red','green','yellow']
# list_label = list(set(kmeans.labels_))
# print(list_label)
# plt.figure()
# for j in range(len(list_label)):
#     Z = data[:][data['label']==list_label[j]].iloc[:, 0:2].values
#     print(Z)
#     for i in range(len(Z)):
#         plt.scatter(Z[i][0], Z[i][1],c=colors[j], s=60)
# plt.show()




'''降维处理'''
# tsne = TSNE(n_components = 3,perplexity =25,
#             early_exaggeration =3,random_state=123) 
# data = pd.DataFrame(tsne.fit_transform(data))
# print(data)

'''最佳聚类数'''
SSE = []
for cluster in range(1,10):
    kmeans = KMeans(n_init = 10, n_clusters = cluster, init='k-means++')
    kmeans.fit(data)
    SSE.append(kmeans.inertia_)


frame = pd.DataFrame({'Cluster':range(1,10), 'SSE':SSE})
plt.figure(figsize=(12,6))
plt.plot(frame['Cluster'], frame['SSE'], marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

'''轮廓分数'''
# random_state = 170
kmeans = KMeans(n_init = 10, n_clusters = 3, init='k-means++',algorithm='full') #n_init：用不同的初始化质心运行算法的次数，默认是10。
kmeans.fit(data)
# Now, print the silhouette score of this model
print(silhouette_score(data, kmeans.labels_, metric='euclidean')) # 0.42949213038731354

'''用KMeans进行聚类'''
clusters = kmeans.fit_predict(data.iloc[:,:]) #fit_predict方法计算聚类中心并且预测每个样本的聚类索引
print(clusters) # == print(kmeans.labels_) # 聚类标签/结果
data_o["label"] = clusters # 添加标签

# print(data.shape)

'''聚类结果绘图'''
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
X = data.columns.values
colors = ['blue','red','green','yellow']
list_label = list(set(kmeans.labels_))
print(list_label)
for j in range(len(list_label)):
    df_0 = data_o[:][data_o.label == list_label[j]]
    Y = df_0.index.values
    Z = data_o[:][data_o['label']==list_label[j]].iloc[:, 0:index_1].values
    for i in range(len(Y)):
        ax.scatter(X, Y[i], Z[i], c=colors[j], s=60)
ax.view_init(30, 185)
# plt.savefig('KM.svg',format='svg')
plt.show()
