# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/18  17:08
'''��Ŀ�����������ڼ��ĵ�һ����ĸ���ж�һ�������ڼ���
�����һ����ĸһ����������жϵڶ�����ĸ��'''
# s=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
while(True):
    a = input('�������һ����ĸ\n')
    if a!='M' and  a!='F' and a!='W' and  a!='T' and a!='S':
        print('������������')
    else:
        if a == 'M':
            print('Monday')
            break
        elif a == 'F':
            print('Friday')
            break
        elif a == 'W':
            print('Wednesday')
            break
        elif a == 'T':
            b = input('������ڶ�����ĸ\n')
            if b == 'u':
                print('Tuesday')
                break
            elif b == 'h':
                print('Thursday')
                break
        elif a == 'S':
            b = input('������')
            if b == 'a':
                print('Saturday')
                break
            elif b == 'u':
                print('Sunday')
                break

