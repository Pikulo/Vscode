# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/21  22:06
lst=[1,3,5,6,9,11,20,23]
a=int(input('��������\n'))
k=0
for i in range(len(lst)):
    if i<len(lst)-1:
        if lst[i] <= a <= lst[i + 1]:
            lst.insert(i+1,a)
            k=1
            break

if k==0:
    lst.append(a)
print(lst)
'''��if __name__ == 'main': �µĴ���
ֻ���ڵ�һ������£����ļ���Ϊ�ű�ֱ��ִ�У�
�Żᱻִ�У���import�������ű����ǲ��ᱻִ�еġ�'''