# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/6  13:35
import os.path
print(os.path.abspath('P134.py'))  # ��ȡ����·��
# exists�ж��ļ�����Ŀ¼�Ƿ���� ��Ture ����False
print(os.path.exists('P134.py'),os.path.exists('P135.py'))
# join��Ŀ¼��Ŀ¼�����ļ�����������
print(os.path.join('E:\\PyCharm\\learning\\kiddo��ѧϰ��־\chap\\�����ʽ���ܺ��ļ�','P134.py'))
# split����Ŀ¼�ͺ��ļ�����
print(os.path.split('E:\\PyCharm\\learning\\kiddo��ѧϰ��־\\chap\\�����ʽ���ܺ��ļ�\\P134.py'))
# splitext�����ļ�������չ��
print(os.path.splitext('P134.py'))  # ����ļ��ͺ�׺��
# basename��Ŀ¼����ȡ�ļ���
print('--------------')
print(os.path.basename('E:\\PyCharm\\learning\\kiddo��ѧϰ��־\\chap\\�����ʽ���ܺ��ļ�\\112.png'))
# dirname��һ��·������ȡ�ļ�·�� �������ļ���
print(os.path.dirname('E:\\PyCharm\\learning\\kiddo��ѧϰ��־\\chap\\�����ʽ���ܺ��ļ�\\P134.py'))
# isdir�����ж��Ƿ�Ϊ·��
print(os.path.isdir('E:\\PyCharm\\learning\\kiddo��ѧϰ��־\\chap\\�����ʽ���ܺ��ļ�\\P134.py'))
print(os.path.isdir('E:\\PyCharm\\learning\\kiddo��ѧϰ��־\\chap\\�����ʽ���ܺ��ļ�'))
