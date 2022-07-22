# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/13  13:59
'''题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。'''
a=int(input(''))  # 循环次数
b=int(input(''))
sum=0
c=b
for i in range(a):
    print(b)
    sum +=b
    b=10*b+c
print(sum)


