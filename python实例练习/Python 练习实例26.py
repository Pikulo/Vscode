# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/18  15:51
'''��Ŀ�����õݹ鷽����5!��'''
def multipile(n):
    sum=1
    if n==0:
        return 1
    else:
        sum=n*multipile(n-1)
    return sum

print(multipile(5))