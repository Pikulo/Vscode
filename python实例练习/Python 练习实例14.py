# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/10  14:38
'''题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。'''

# 判断素数
def judge(n):
    spot=0
    for i in range(2,n):
        if n%i==0:
            spot+=1
            return n+1
    if spot==0:
        return n
n=int(input('请输入整数'))
# 找因数
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