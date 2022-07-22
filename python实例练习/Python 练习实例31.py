# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/18  17:08
'''题目：请输入星期几的第一个字母来判断一下是星期几，
如果第一个字母一样，则继续判断第二个字母。'''
# s=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
while(True):
    a = input('请输入第一个字母\n')
    if a!='M' and  a!='F' and a!='W' and  a!='T' and a!='S':
        print('您的输入有误')
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
            b = input('再输入第二个字母\n')
            if b == 'u':
                print('Tuesday')
                break
            elif b == 'h':
                print('Thursday')
                break
        elif a == 'S':
            b = input('再输入')
            if b == 'a':
                print('Saturday')
                break
            elif b == 'u':
                print('Sunday')
                break

