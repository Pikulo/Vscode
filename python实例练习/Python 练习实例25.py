# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/18  15:42
'''题目：求1+2!+3!+...+20!的和。'''
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


