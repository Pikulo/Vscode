from multiprocessing.dummy import Array
import numpy as np
from sklearn.datasets import make_classification
from sklearn.cluster import AffinityPropagation
from matplotlib import pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler

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
# print(data)

'''绘图颜色'''
colors = ['#9D18D2', '#E1CD6D', '#56A2B5', '#5638F1', '#1331E5', '#888F7F', '#5D4EC9', '#2BABFA', '#8F83A9', '#4EF6E3', '#E6991A', '#669D8D', '#F45E3C', '#424D92', '#729BD5', '#9E65CD', '#7664CB', '#F81B15', '#1D98AC', '#C74B18', '#8DA429', '#9538AA', '#77F5E6', '#6EAE92', '#1FCD46', '#985CAA', '#73BBC6', '#D1E895', '#F2F244', '#4AE446', '#5338C3', '#441D55', '#5B7D69', '#D9DFE1', '#A3D74D', '#39B7B5', '#5FB888', '#E59E23', '#59D675', '#3C3D78', '#89B1ED']
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False 


'''参数选择'''
# fig = plt.figure(figsize=(10,10))
# num_plt = 1
# for dam in np.arange(0.6,1,0.1):
#     # 迭代不同的min_samples值
#     plt.subplot(2,2,num_plt)
#     x_sam = []
#     num_typ = []
#     for pre in range(200,300):  # 200-300
#         x_sam.append(pre)
#         af = AffinityPropagation(damping = dam,preference = -pre)
#         af.fit(data)
#         print('分类标签：',af.labels_)
#         num_typ.append(len(set(af.labels_)))
#         print("参数damping取值为:",dam,"参数preference取值为:",pre)
#         print("每簇包含的样本数量:",np.unique(af.labels_,return_counts = True))
#         print('------------------------------------------------------------------------------------')
#     plt.plot(x_sam, num_typ, linestyle='-', label='Damping:{0}'.format(round(dam,2)),color=colors[num_plt-1])
#     plt.xlabel('Preference')
#     plt.ylabel('Number of clusters')
#     plt.legend(loc='best')
#     fig.tight_layout()
#     num_plt+=1
# if index_1 == 41:
#     plt.savefig('AffinityPropagation_compare_row.svg',format='svg')
#     plt.savefig('AffinityPropagation_compare_row.png',format='png')
# if index_1 == 288:
#     plt.savefig('AffinityPropagation_compare_col.svg',format='svg')
#     plt.savefig('AffinityPropagation_compare_col.png',format='png')
# plt.show()



'''聚类结果绘图'''
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X(天)')
ax.set_ylabel('Y(分钟)')
ax.set_zlabel('Z(值)')

'''row'''
if index_1 == 41:
    af = AffinityPropagation(damping = 0.6,preference = -220)
    af.fit(data)
    data_o["label"] = af.labels_ # 添加标签
    print(data_o)
    X = data.columns.values
    for i in range(len(X)):
        X[i]+=1
    print(X)
    list_label = list(set(af.labels_))
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
    plt.savefig('Ap_dam0.6_pre220_row_cluster{0}.svg'.format(len(set(af.labels_))),format='svg')
    plt.savefig('Ap_dam0.6_pre220_row_cluster{0}.png'.format(len(set(af.labels_))),format='png')
    plt.show()

'''columns''' # 更改
if index_1 == 288:
    af = AffinityPropagation(damping = 0.7,preference = -300)
    af.fit(data)
    data_o["label"] = af.labels_ # 添加标签

    print(data_o)
    print(data_o)
    # print(data.shape)
    X = data.columns.values
    for i in range(len(X)):
        X[i]=(X[i]+1)*5
    print(X)
    list_label = list(set(af.labels_))
    # print(list_label)
    for j in range(len(list_label)):
        df_0 = data_o[:][data_o.label == list_label[j]]
        Y = df_0.index.values
        print(Y)
        Z = data_o[:][data_o['label'] == list_label[j]].iloc[:, 0:index_1].values
        print(Z)
        for i in range(len(Y)):
            ax.scatter(Y[i], X, Z[i], c=colors[j], s=60)
    print(set(af.labels_))
    ax.view_init(30, 220)
    plt.savefig('Ap_dam0.6_pre220_col_clusters{0}.svg'.format(len(set(af.labels_))),format='svg')
    plt.savefig('Ap_dam0.6_pre220_col_clusters{0}.png'.format(len(set(af.labels_))),format='png')
    plt.show()