# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/6  13:54
import os
path='F:\�ֻ��ϵ���Ƭ&��Ƶ\IT'S ME'
lst_files=os.walk(path)
print(lst_files)
for dirpath,dirname,filename in lst_files:
    print(dirpath)
    print(dirname)
    print(filename)
    print('-------------------')

