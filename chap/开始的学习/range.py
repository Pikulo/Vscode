# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/1/19  15:28

# a=range(10)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]默认从0开始，相差1称为步长
# print(a)#range(0, 10)
# print(list(a))#查看range中的整数序列————》list是列表
# '''第二种创建方式，小括号中给了两个参数'''
# b=range(1,20)#指定从1开始，到10结束
# print(list(b))
# '''第二种创建方式，小括号中给了两三个参数'''
# c=range(1,10,3)#从1开始到10结束，步长为3
# print(list(c))
# '''判断指定的整数在序列中是否存在'''
# print(7 in c)
# print(10 in c)

# #循环结构
# i=10;
# c=0;
# while i>=0:
#     c+=1;
#     print(i)
#     i-=1;
# print(c)
# #计算1到100的累加和
# a=1;
# sum=0;
# while a<=100:
#     sum=sum+a;
#     a+=1;
# print('1到100的和为',sum)

#计算输入数i到j之间的偶数、奇数和
ki=i=int(input('输入一个整数'));
di=j=int(input('输入另一个个整数'));
if i>j:
    g = j;
    j=di=i;
    i=ki=g;
sumd=0;
sumj=0;
while i<=j:
    if i%2==0:
        sumd+=i;
    else:
        sumj+=i;
    i+=1;
print(str(ki),'到',str(di),'之间的偶数和为',sumd)
print(str(ki),'到',str(di),'之间的奇数和为',sumj)







