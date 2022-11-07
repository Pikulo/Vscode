from multiprocessing.dummy import Array
import numpy as np
from sklearn.datasets import make_classification
from sklearn.cluster import AffinityPropagation
from matplotlib import pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler



data_o = pd.read_excel('聚类大作业--41天数据.xls', header=None) 
# print(data_o)
'''行列互换'''
# data_o = pd.DataFrame(data_o.values.T,columns = data_o.index,index = data_o.columns) 
# print(data_o)
'归一化处理'
scaler = StandardScaler().fit(data_o.values)
features = scaler.transform(data_o.values)
scaled_features = pd.DataFrame(features)
data = scaled_features
# print(data)



'''调参'''
# for dam in np.arange(0.6,1,0.1):
#     for pre in range(200,250):        
#         af1 = AffinityPropagation(damping = dam, # 阻尼系数，取值[0.5,1)
#                                 preference = -pre ## 使用的示例样本数量
#                                 )
#         af1.fit(data)
#         ## 输出聚类分析的结果
#         af1.labels_
#         # print(af1.labels_)
#         print("参数damping取值为:",dam,"参数preference取值为:",pre)
#         print("亲和力传播聚类1:\n每簇包含的样本数量:",np.unique(af1.labels_,return_counts = True))
#         # print("每个簇的聚类中心为:\n",af1.cluster_centers_)



'''聚类'''
af1 = AffinityPropagation(damping = 0.6, # 阻尼系数，取值[0.5,1)
                         preference = -300 ## 使用的示例样本数量
                         )
af1.fit(data.values)
print(af1.labels_)
data_o["label"] = af1.labels_ # 添加标签
# print(data_o)
# print(data.shape)

'''聚类结果绘图'''
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
X = data.columns.values
colors = ['blue','red','green','yellow','#375B69', '#F9AA98', '#ECA5A8', '#62D566', '#F64537', '#CCB65E', '#2AE328', '#4CF937', '#821ABC', '#2F253F', '#C68A4A', '#FBA6CA', '#F58CE2', '#C961EC', '#F5E2AA', '#6F335E', '#88E265', '#6A667B', '#979D13', '#B99B6A', '#3A389D', '#459CEA', '#842B7D', '#8D44D8', '#781C5F', '#B1DB83', '#2D3D18', '#7B3DBF', '#355C7C', '#479B28', '#C77655', '#54A728', '#D7FFB4', '#73862A', '#E6F951', '#7F95B3', '#9121D2', '#4E861C', '#ADC35A', '#8B764E', '#49F8F4']
list_label = list(set(af1.labels_))
print(list_label)
for j in range(len(list_label)):
    df_0 = data_o[:][data_o.label == list_label[j]]
    Y = df_0.index.values
    Z = data_o[:][data_o['label'] == list_label[j]].iloc[:, 0:41].values
    for i in range(len(Y)):
        ax.scatter(X, Y[i], Z[i], c=colors[j] ,s=60) #c=colors[j],
ax.view_init(30, 185)
# plt.savefig('KM.svg',format='svg')
plt.show()