# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/10  17:16
'''��Ŀ�����ָ����ʽ�����ڡ�'''

import datetime

if __name__ =='__main__':
    print(datetime.date.today().strftime('%d/%m/%Y'))
# �������ڶ���
miyazakiBirthDate = datetime.date(1941, 1, 5)
print(miyazakiBirthDate.strftime('%d/%m/%Y'))
# ������������
miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=3)
print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))


# �����滻
miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 2)
print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))