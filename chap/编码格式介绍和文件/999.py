# coding=utf-8
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/5  20:15


file=open('a.txt','r',encoding='gb18030')
file.seek(2)
print(file.read())
file.close()