# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/10  14:38
'''��Ŀ����һ���������ֽ������������磺����90,��ӡ��90=2*3*3*5��'''

# �ж�����
def judge(n):
    spot=0
    for i in range(2,n):
        if n%i==0:
            spot+=1
            return n+1
    if spot==0:
        return n
n=int(input('����������'))
# ������
def clac(n):
    spot=0
    for i in range(2, n + 1):
        if spot==0:
            for j in range(2, n + 1):
                if i * j == n:
                    spot += 1
                    return [i, j]
                    break
        else:
            break
list=[]
while True:
    if judge(n)==n:
        list.append(n)
        break
    else:
        list.append(clac(n)[0])
        n=clac(n)[1]
print(list)