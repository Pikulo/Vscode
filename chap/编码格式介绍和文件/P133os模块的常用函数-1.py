# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/6  12:46
import os
print(os.getcwd())  # 返回当前工作目录

# os.listdir('编码格式介绍和文件')  # FileNotFoundError: [WinError 3] 系统找不到指定的路径。: '编码格式介绍和文件'
lst=os.listdir('../编码格式介绍和文件')
print(lst)

# os.mkdir('newdir2')  # 创建目录

# os.makedirs('A/B/C')
# os.rmdir('newdir2')  # 删除newdir2
# os.removedirs('A/B/C')  # 删除多级目录A/B/C

os.chdir('E:\\PyCharm\\learning\\kiddo的学习日志\chap\\继承')
print(os.getcwd())
lst=os.listdir('../继承')
print(lst)