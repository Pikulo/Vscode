# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/1/26  16:01
# '''从左边开始劈分'''
# s='hello world Python'
# lst=s.split()  # 以空格为劈分符号
# print(lst)
# s1='hello|world|Python'
# print(s1.split(sep='|'))  # 以|为劈分符号
# print(s1.split(sep='|',maxsplit=1))  # 以|为劈分符号,最大劈分次数为1
# '''从右侧开始劈分'''
# print(s.rsplit())
# print(s1.rsplit(sep='|',maxsplit=1))
#
# '''判断是不是合法的标识符'''
# s='hello,python'
# print('1',s.isidentifier())  # False逗号不是标识符
# print('2','hello'.isidentifier())  # True
# print('3','张三'.isidentifier())  # True
# print('4','张三_123'.isidentifier())  # True
# '''判断字符串是否由空白字符串组成'''
# print('5','\t'.isspace())  # True
# print('6','123'.isspace())  # False
# '''用isalpha判断字符串是否由字母组成'''
# '''用isdecimal判断是否由十进制数字组成'''
# '''用判断是否由数字组成'''
# '''用判断是否由字母和数字组成'''

s='hello,python'
print(s.replace('python','java'))
s1='hello,python,python,python'
print(s1.replace('python','java',2))
print(s1.replace('python','java',3))

lst=['hello','python','java']
print('|'.join(lst))
print('**'.join(lst))
t=('helo','java','python')
print(''.join(t))
print('*'.join('python'))


