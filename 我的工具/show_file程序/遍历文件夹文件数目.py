# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/6  15:26
import os
path='F:\�人����ѧ'
lst_files=os.walk(path)
print(lst_files)
d=1
sum=0
for dirpath,dirname,filename in lst_files:
    a=0
    b=0
    for dir in dirname:
        a+=1
    print('\t\tͳ�Ƶ����ļ�����Ŀ��{0}��'.format(a))
    for file in filename:
        b+=1
    sum+=b
    print('\t\tͳ�Ƶ����ļ���Ŀ��{0}��'.format(b))
    print('-----------------��{0}���ļ��б������,���ļ���������ļ�����{1}����Ŀ----------------------'.format(d,a+b))
    d+=1
print('����Ŀ¼�¹��ɼ�{0}���ļ���zip�ļ��������ڣ�������zip���ļ���'.format(sum))