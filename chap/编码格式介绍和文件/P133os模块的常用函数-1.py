# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/6  12:46
import os
print(os.getcwd())  # ���ص�ǰ����Ŀ¼

# os.listdir('�����ʽ���ܺ��ļ�')  # FileNotFoundError: [WinError 3] ϵͳ�Ҳ���ָ����·����: '�����ʽ���ܺ��ļ�'
lst=os.listdir('../�����ʽ���ܺ��ļ�')
print(lst)

# os.mkdir('newdir2')  # ����Ŀ¼

# os.makedirs('A/B/C')
# os.rmdir('newdir2')  # ɾ��newdir2
# os.removedirs('A/B/C')  # ɾ���༶Ŀ¼A/B/C

os.chdir('E:\\PyCharm\\learning\\kiddo��ѧϰ��־\chap\\�̳�')
print(os.getcwd())
lst=os.listdir('../�̳�')
print(lst)