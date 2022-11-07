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
from matplotlib.pyplot import MultipleLocator

# 参考文章:https://mp.weixin.qq.com/s/afECb9fHOJBM6zNGHyYPQg

data_o = pd.read_excel('聚类大作业--41天数据.xls', header=None) 
index_1 = 41
# print(data_o)
'''行列互换'''
data_o = pd.DataFrame(data_o.values.T,columns = data_o.index,index = data_o.columns) 
index_1 = 288
# print(data_o)

'''降二维图像'''
# pca = PCA(n_components=2)
# X_r = pca.fit(data_o).transform(data_o)
# # print(X_r)
# data = pd.DataFrame(X_r)
# print(data)

'归一化处理'
scaler = StandardScaler().fit(data_o.values)
features = scaler.transform(data_o.values)
scaled_features = pd.DataFrame(features)
data = scaled_features
print(data)

'''TSNE降维处理'''
# tsne = TSNE(n_components = 3,perplexity =25,
#             early_exaggeration =3,random_state=123) 
# data = pd.DataFrame(tsne.fit_transform(data))
# print(data)

'''最佳聚类数'''
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False 
SSE = []
for cluster in range(1,10):
    kmeans = KMeans(n_init = 10, n_clusters = cluster, init='k-means++')
    kmeans.fit(data)
    SSE.append(kmeans.inertia_)
frame = pd.DataFrame({'Cluster':range(1,10), 'SSE':SSE})
plt.figure(figsize=(10,6))
plt.plot(frame['Cluster'], frame['SSE'], marker='o')
plt.xlabel('聚类数量')
plt.ylabel('簇内误差平方和')
plt.savefig('n_clusters.png',format='png')
plt.show()

'''轮廓分数'''
# random_state = 170
kmeans = KMeans(n_init = 10, n_clusters = 4, init='k-means++',algorithm='full') #n_init：用不同的初始化质心运行算法的次数，默认是10。
kmeans.fit(data)
# Now, print the silhouette score of this model
print(silhouette_score(data, kmeans.labels_, metric='euclidean')) # 0.42949213038731354

'''用KMeans进行聚类'''
clusters = kmeans.fit_predict(data.iloc[:,:]) #fit_predict方法计算聚类中心并且预测每个样本的聚类索引
print(clusters) # == print(kmeans.labels_) # 聚类标签/结果
data_o["label"] = clusters # 添加标签

'''聚类结果绘图'''
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
X = data.columns.values
for i in range(len(X)):
    X[i]+=1
print('X:',X)
colors = ['blue','red','green','yellow']
list_label = list(set(kmeans.labels_))
print(list_label)
for j in range(len(list_label)):
    df_0 = data_o[:][data_o.label == list_label[j]]
    Y = df_0.index.values
    for n in range(len(Y)):
        Y[n]=(Y[n]+1)*10
    print('Y:',Y)
    Z = data_o[:][data_o['label']==list_label[j]].iloc[:, 0:index_1].values
    for i in range(len(Y)):
        ax.scatter(X, Y[i], Z[i], c=colors[j], s=60)
#前3个参数用来调整各坐标轴的缩放比例
ax.view_init(30, 185)
plt.savefig('KMeans.png',format='png')
plt.show()