# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/10  12:41

'''��Ŀ������ĳ��ĳ��ĳ�գ��ж���һ������һ��ĵڼ��죿'''
year=int(input('������'))
month=int(input('������'))
day=int(input('������'))

last_month=[31,28,31,30,31,30,31,31,30,31,30,31]
sum=0
for i in range(month-1):
    sum+=last_month[i]
sum+=day
if (year%4==0 and year%100!=0) or year%400==0:
    sum+=1
print(sum)