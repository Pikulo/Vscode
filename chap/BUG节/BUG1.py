# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/1/31  11:49
'''多个except结构'''
try:
    a = int(input('请输入第一个整数'))
    b = int(input('请输入第二个整数'))
    result = a / b
    print('结果为：', result)
except ZeroDivisionError:
    print('对不起，除数不允许为0')
except ValueError:
    print('只能输入字符串')

print('程序结束')












