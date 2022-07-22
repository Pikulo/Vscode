# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/1/24  10:26

items=['Fruits','Books','Others','zipper']
prices=[90,85,76]
a={item.upper():price for item,price in zip(items,prices)}
print(a)

