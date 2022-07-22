#学习场所： 家里
#写 习 者：刘明阳
#学习时间：2021/1/15  10:02



#可以输出数字
print(520)

#可以输出字符、字符串
print("hello")
print('helloworld')
#可以输出表达式
print(9*9)
#输出到文件中
fp=open('G:/kiddy.txt','a+')#如果文件不存在的话就创建 文件存在的话就在原有的基础上追加
print('kiddo loves kiddy',file=fp)
fp.close()
#在一行进行输出
print('hello','world','Python')