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

'''模型评估'''
import statsmodels.api as sm
X2 = sm.add_constant(X)
est = sm.OLS(Y, X2).fit()
print(est.summary())  # 在Jupyter Notebook中可以直接写est.summary()

from sklearn.metrics import r2_score
r2 = r2_score(Y, regr.predict(X))
print(r2)

