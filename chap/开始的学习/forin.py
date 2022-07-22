# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/1/20  9:28

# for item in 'LIUMINGYANG':#第一次取出来的值是P，将P赋值给item，将item输出
#     print(item)
# for i in range(10,18,2):
#     print(i)
# #循环体中不需要用到自定义变量，将其写成_
# for _ in range(3):
#     print('我爱kiddy')
# #使用for循环计算累加和
# sum=0;
# for a in range(1,101):
#     sum+=a;
# print('1到100的和为：',sum)
# #——————————————————第二种方法————————————————————————————
# sum=0;
# for a in range(101):
#     print(a,end="")#end=""表示去掉末尾的自动换行
#     print('+',end="")
#     sum+=a;
# print('\b=',sum)
# print('\b\n1到100的和为：',sum)#\b表示推一格

#100到999的水仙花数：个位的三次方+十位的三次方+百位的三次方和这个数相等
###使用for循环
#举例：153=1*1*1+5*5*5+3*3*3
# for i in range(100,1000):
#     if i==((i%10)**3+(i//10%10)**3+(i//100)**3):
#         print(i,"是水仙花数")
#
#
# print(100/10)#除
# print(100//10)#整除

################break语句################
# #取款机输入密码
#
#
# k=1;
# while k<=3:
#     a = (input('请输入您的密码'))
#     k+=1;
#     if (a == '6666'):
#         print('您的密码正确')
#         break
#     else:
#         print('您的密码错误，请再次输入')



# lst=['a','b',98]
# print(lst)
# lst2=list(['a','s',99])
# print(lst2)
# print(list(range(100)))

# #要求输出1——50之间，所以5的倍数,使用continue
# for i in range(1,51):
#     if i%5!=0:
#         continue
#     print(i)

# for i in range(3):
#     a=input('请输入密码')
#     if a=='6666':
#         print('您的密码正确')
#         break
#     else:
#         print('再次输入您的密码')
# else:
#     print('对不起，三次均错误，请于1小时后重试')

# print('#####################用while语句写#####################')
# b=0
# while b<3:
#     a = input('请输入密码')
#     if a == '6666':
#         print('您的密码正确')
#         break
#     else:
#         print('再次输入您的密码')
#         b += 1
# else:
#     print('对不起，三次均错误，请于1小时后重试')

# for i in range(1,5):
#     for j in range(1,5):
#         print('*',end='\t')
#     print()
# print('#########打印直角三角形#########')
# a=int(input('您想打印一个长为几的直角三角形？'))
# for i in range(1,a+1):
#     for _ in range(i):
#         print('*',end='')
#     print()
print('#########打印乘法口诀表#########')
for i in range(1,10):
    a = 1
    for j in range(i):
        print(a,'*',i,'=',a*i,end='\t')
        a+=1
    print()




























































