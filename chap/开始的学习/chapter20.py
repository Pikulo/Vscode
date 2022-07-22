#学习场所： 家里
#写 习 者：刘明阳
#学习时间：2021/1/17  12:17

# present=input('你开心吗？')
# print(present,type(present))

# #练习题目，从键盘输入两个数字，然后计算他们的和
# a=input('数字')
# b=input('数字')
# print(int(a+b))
# print(int(a)+int(b))
# print(type(a))

# print(11//2)#取整运算
# print(11/2)
# print(11%2)
# print(2**10)

# print(-9/-4)
# print(-9/4)
# print(9//4)
# print(-9//4)
# print(9//-4)
# print(11%-3)
# print(-11%3)

# #赋值运算符
# a=1
# a+=1
# print(a)
# a,b,c=1,2,3#系列解包赋值
# print(a,b,c)

#比较运算符 其结果类型为布尔类型 比较的事值

# a,b=10,20
# print('a>=b吗？')
# a=input('输入a的值')
# b=input('输入b的值')
# if(a>=b):
#     print('是的')
# else:
#     print('不是')

# #比较对象标识用  is
#
# a=10
# b=10.0
# print(a==b)#说明a和b的value相等
# print(a is b)#说明a和b的id标识相等

# list1=[11,22,33,44]
# list2=[11,22,33,44]
# print(list1==list2)
# #is 如果相同为Ture 不同为False
# print(list1 is list2)
# print(id(list1),id(list2))
# #is ont  如果不同为Ture 相同为False
# print(list1 is not list2)

# a,b=1,2
# #布尔运算符and 只有两个都为真 结果才为真
# print(a==1 and b==2)# 真 真 为 真
# print(a==1 and b!=2)#真 假 为 假
# print(a!=1  and  b!=2)#假 假 为 假
# #布尔运算符or 有一个为真 结果为真
# print(a==1 or b==2)
# print(a!=1 or b==2)
# print(a!=1 or b!=2)
# #not 取反
# f1=True
# f2=False
# print( not f1)
# print(not  f2)

#In 和not in————————in表示在字符串里 not in 表示不在字符串里

# h='Helloween'
# print('a'in h)
# print('e'in h)
# print('e'not in h)
# g='12365'
# print('12'in g,'123' in g,'125'in g,'123'not in g)


#位运算

print(4&8)#按位与 同为1才为1 否则为0
print(4|8)#同为0才为0 否则为1
print(4<<1)
print(4<<2)
print(4<<3)
print(4>>1)
print(4>>2)
print(4>>3)











