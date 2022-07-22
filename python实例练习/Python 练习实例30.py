# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/18  17:04
a=input('输入一个5位数')
if a[0]==a[4] and a[1]==a[3]:
    print('{}是回文数'.format(a))
else:
    print('{}不是回文数'.format(a))