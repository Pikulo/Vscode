# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/6  16:20
import os
get = input('��������Ҫ�������ļ�·��:\n')
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
    print('\t\tͳ�Ƶ����ļ�����Ŀ��{0}��'.format(a))
    for file in filename:
        b += 1
        print(os.path.join(dirpath, file))
    sum += b
    print('\t\tͳ�Ƶ����ļ���Ŀ��{0}��'.format(b))
    print('-----------------��{0}���ļ��б������,���ļ���������ļ�����{1}����Ŀ----------------------'.format(d, a + b))
    d += 1
print('����Ŀ¼�¹��ɼ�{0}���ļ���zip�ļ��������ڣ�������zip���ļ���'.format(sum))