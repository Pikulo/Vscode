# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/7  14:47

def copy_file():
    import os
    path=input('������Ҫ���Ƶ��ļ����ڵ�·��:\n')
    os.chdir(path)
    pictuer_name = input('������Ƭ�����Լ���ʽ�ڴ�:\n')
    tick = int(input('�������븴�Ƶĸ���:\n'))
    for i in range(tick):
        with open('{0}'.format(pictuer_name), 'rb') as file_1:
            with open('{0}-{1}'.format(i + 1, pictuer_name), 'wb') as file_2:
                file_2.write(file_1.read())

copy_file()
