# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/5  21:31

with open('112.png','rb') as file_1:
    with open('copy112_1.png','wb') as file_2:
        file_2.write(file_1.read())


# import os
# print(os.getcwd())

