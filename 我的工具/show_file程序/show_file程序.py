# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/6  15:47
def show_file():
        import os
        get = input('��������Ҫ�������ļ�·��:\n')
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
            print('\t\t\t\t\t\tͳ�Ƶ����ļ�����Ŀ��{0}��'.format(a))
            for file in filename:
                try:
                    b += 1
                    print(os.path.join(dirpath, file))
                except UnicodeEncodeError:
                    k_nogkb += 1
            sum += b
            print('\t\t\t\t\t\tͳ�Ƶ����ļ���Ŀ��{0}��'.format(b))
            print('----------------��{0}���ļ��б������,���ļ���������ļ�����{1}����Ŀ---------------------'.format(d, a + b))
            d += 1
        print('��GKB������ļ��������ļ�����{0}��'.format(k_nogkb))
        print('GBK������ļ��������ļ�������{0}��'.format(sum))
        print('����Ŀ¼�¹��ɼ�{0}���ļ�(������zip�ļ�)'.format(sum+k_nogkb))

show_file()

