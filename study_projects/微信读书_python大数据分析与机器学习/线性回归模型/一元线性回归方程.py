import matplotlib.pyplot as plt
X = [[1], [2], [4], [5]]
Y = [2, 4, 6, 8]
# plt.scatter(X, Y)
# plt.show()

from sklearn.linear_model import LinearRegression
regr = LinearRegression()
regr.fit(X,Y) # 拟合的模型
# y = regr.predict([[1.5]])
y = regr.predict([[1.5],[2.5],[4.5]])
print(y)
plt.scatter(X, Y)  # 绘制散点图
plt.plot(X,regr.predict(X)) # 拟合曲线
plt.show()

'''得到拟合曲线的系数（斜率）和截距'''
print('系数a：' + str(regr.coef_[0])) # 系数
print('截距b：' + str(regr.intercept_)) # 截距
print('一元线性回归方程y={0}x+{1}'.format(regr.coef_[0],regr.intercept_))
