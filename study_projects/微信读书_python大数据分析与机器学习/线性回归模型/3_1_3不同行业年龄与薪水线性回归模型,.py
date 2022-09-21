import pandas
df = pandas.read_excel('E:\VisualStudioCode\Vscode\study_projects\微信读书_python大数据分析与机器学习\线性回归模型\IT行业收入表.xlsx')
print(df.head())
X = df[['工龄']]
Y = df['薪水']
print(X,Y)
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.scatter(X, Y)
plt.xlabel('工龄')
plt.ylabel('薪水')
# plt.show()

# 模型搭建
from sklearn.linear_model import LinearRegression
regr = LinearRegression()
regr.fit(X, Y)
plt.scatter(X, Y)
plt.plot(X, regr.predict(X), color='red')
plt.xlabel('工龄')
plt.ylabel('薪水')
plt.show()

