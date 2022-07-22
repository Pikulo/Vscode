# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/6  13:54
import os
path='F:\手机上的照片&视频\IT'S ME'
lst_files=os.walk(path)
print(lst_files)
for dirpath,dirname,filename in lst_files:
    print(dirpath)
    print(dirname)
    print(filename)
    print('-------------------')

