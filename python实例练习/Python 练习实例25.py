# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/18  15:42
'''��Ŀ����1+2!+3!+...+20!�ĺ͡�'''
def multipe(n):
    sum=1
    for i in range(n):
        sum*=n
        n-=1
    return sum
sum=0
for i in range(1,21):
    sum+=multipe(i)
print(sum)


