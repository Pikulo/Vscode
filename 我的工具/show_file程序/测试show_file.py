# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/6  16:20
import os
get = input('请输入你要遍历的文件路径:\n')
path = '{0}'.format(get)
lst_files = os.walk(path)
print(lst_files)
d = 1
sum = 0
for dirpath, dirname, filename in lst_files:
    '''print(dirpath)
    print(dirname)
    print(filename)
    print('-------------------')'''
    a = 0
    b = 0
    for dir in dirname:
        a += 1
        print(os.path.join(dirpath, dir))
    print('\t\t统计到的文件夹数目有{0}个'.format(a))
    for file in filename:
        b += 1
        print(os.path.join(dirpath, file))
    sum += b
    print('\t\t统计到的文件数目有{0}个'.format(b))
    print('-----------------第{0}个文件夹遍历完毕,本文件夹里包含文件共有{1}个项目----------------------'.format(d, a + b))
    d += 1
print('该总目录下共可见{0}个文件（zip文件包含在内，不包括zip内文件）'.format(sum))