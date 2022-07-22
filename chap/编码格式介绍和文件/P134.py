# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/6  13:35
import os.path
print(os.path.abspath('P134.py'))  # 获取绝对路径
# exists判断文件或者目录是否存在 是Ture 不是False
print(os.path.exists('P134.py'),os.path.exists('P135.py'))
# join将目录与目录或者文件名连接起来
print(os.path.join('E:\\PyCharm\\learning\\kiddo的学习日志\chap\\编码格式介绍和文件','P134.py'))
# split分离目录和和文件名字
print(os.path.split('E:\\PyCharm\\learning\\kiddo的学习日志\\chap\\编码格式介绍和文件\\P134.py'))
# splitext分离文件名和拓展名
print(os.path.splitext('P134.py'))  # 拆分文件和后缀名
# basename从目录中提取文件名
print('--------------')
print(os.path.basename('E:\\PyCharm\\learning\\kiddo的学习日志\\chap\\编码格式介绍和文件\\112.png'))
# dirname从一个路径中提取文件路径 不包括文件名
print(os.path.dirname('E:\\PyCharm\\learning\\kiddo的学习日志\\chap\\编码格式介绍和文件\\P134.py'))
# isdir用于判断是否为路径
print(os.path.isdir('E:\\PyCharm\\learning\\kiddo的学习日志\\chap\\编码格式介绍和文件\\P134.py'))
print(os.path.isdir('E:\\PyCharm\\learning\\kiddo的学习日志\\chap\\编码格式介绍和文件'))
