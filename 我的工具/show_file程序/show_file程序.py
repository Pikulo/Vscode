# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/6  15:47
def show_file():
        import os
        get = input('请输入你要遍历的文件路径:\n')
        path = '{0}'.format(get)
        lst_files = os.walk(path)
        print(lst_files)
        d = 1
        sum = 0
        k_nogkb=0
        for dirpath, dirname, filename in lst_files:
            '''print(dirpath)
            print(dirname)
            print(filename)
            print('-------------------')'''
            a = 0
            b = 0
            for dir in dirname:
                try:
                    a += 1
                    print(os.path.join(dirpath, dir))
                except UnicodeEncodeError:
                    k_nogkb += 1
            print('\t\t\t\t\t\t统计到的文件夹数目有{0}个'.format(a))
            for file in filename:
                try:
                    b += 1
                    print(os.path.join(dirpath, file))
                except UnicodeEncodeError:
                    k_nogkb += 1
            sum += b
            print('\t\t\t\t\t\t统计到的文件数目有{0}个'.format(b))
            print('----------------第{0}个文件夹遍历完毕,本文件夹里包含文件共有{1}个项目---------------------'.format(d, a + b))
            d += 1
        print('非GKB编码的文件夹名和文件名有{0}个'.format(k_nogkb))
        print('GBK编码的文件夹名和文件名共有{0}个'.format(sum))
        print('该总目录下共可见{0}个文件(不包括zip文件)'.format(sum+k_nogkb))

show_file()

