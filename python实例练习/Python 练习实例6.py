# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/10  13:16
'''��Ŀ��쳲��������С�'''

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(10))

lst=[]
for i in range(11):
    lst.append(fib(i))
print(lst)


