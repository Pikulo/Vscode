# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/7  14:47

def copy_file():
    import os
    path=input('输入您要复制的文件所在的路径:\n')
    os.chdir(path)
    pictuer_name = input('复制照片名称以及格式在此:\n')
    tick = int(input('输入您想复制的个数:\n'))
    for i in range(tick):
        with open('{0}'.format(pictuer_name), 'rb') as file_1:
            with open('{0}-{1}'.format(i + 1, pictuer_name), 'wb') as file_2:
                file_2.write(file_1.read())

copy_file()
