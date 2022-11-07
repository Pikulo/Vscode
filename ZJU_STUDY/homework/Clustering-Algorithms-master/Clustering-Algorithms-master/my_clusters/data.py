import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
raw_data = pd.read_excel('聚类大作业--41天数据.xls', header=None)  # header=0表示第一行是表头，就自动去除了

# print(raw_data[:][:])

# for i in range(0,41):
#     data = ''
#     data+=str(i+1)
#     data+=','
#     for j in list(raw_data[:][i]):
#         data+=str(j)
#         data+=','
#     print(data)

#以1-288为横轴
# data = []
# n = 41
# for i in range(0,n):
#     data+=list(raw_data[:][i])
# print(len(data))
# y = []
# for i in range(288*41):
#     y.append(i)
# plt.plot(y,data)
# # k = 0
# # l = 288
# # for i in range(2):
# #     plt.scatter(y,data[k:l])
# #     k+=288
# #     l+=288
# plt.show()

# data = []
# n = 288
# print(raw_data.loc[0:0])
# data_part = raw_data.loc[0:287]
# data_part_list = np.array(data_part).tolist()
# print(len(data_part_list))
# for i in range(0,n):
#     data+=list(raw_data[i:i+1][:])
#     # print(raw_data[i:i+1][:])
# # print(data)
# y = []
# for i in range(41):
#     y.append(i)
# # plt.figure(figsize=(19.2, 10.8))
# for i in range(5):
#     print(len(data_part_list[i]))
#     plt.scatter(y,data_part_list[i])
# # plt.savefig('figure.svg',format='svg')
# plt.show()



'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
# warnings.filterwarning('ignore')
from sklearn.preprocessing import StandardScaler
s = StandardScaler()
raw_data = raw_data[[0,1]][:]
X = raw_data[[0,1]][:]
print(X)
X_scale = s.fit_transform(X)
X_scale = pd.DataFrame(X_scale, columns=X.columns, index=X.index)
print(X_scale.head())

from sklearn.cluster import KMeans
# 定义候选的K值。
scope = range(1, 10)
# 定义SSE列表，用来存放不同K值下的SSE。
sse = []
for k in scope:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X_scale)
    sse.append(kmeans.inertia_)
plt.xticks(scope)
sns.lineplot(sse, marker="o")
# plt.show()

kmeans = KMeans(n_clusters=3)
kmeans.fit(X_scale)
# 获取每个样本所属的簇。标签的数值对应所属簇的索引。
print("标签：", kmeans.labels_)
raw_data['kmeans.labels_']=kmeans.labels_
print(raw_data)

fig =plt.figure(figsize=(4,4), dpi=100)
color = ["r", "g", "b"]
for i in range(3):
    d = raw_data[kmeans.labels_ == i]
    plt.scatter(d[:][[0]], d[:][[1]],color=color[i], label=f"客户群{i}")
    plt.legend()
    plt.rcParams['font.family']='SimHei'
    plt.rcParams['axes.unicode_minus']='False'
plt.show()
'''
new_data = StandardScaler.fit_transform(raw_data)
print(new_data)