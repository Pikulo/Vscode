# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/5  20:17
# file=open('a.txt','r',encoding='UTF-8')
# print(file.read())  # 读取所有内容
# print(file.read(2))  # 读取两个字符内容 美丽
# print(file.read(3))  # 读取三个字符内容 ’美丽 ‘
# print(file.read(4))  # 读取三个字符内容 ’美丽 中国‘
# print(file.readline())  # 读取一行 美丽
# print(file.readlines())  # 输出每一行内容 ['美丽\n', '中国']
# print('_______________________')

# file=open('c.txt','a')
# file.write('hello')
# lst=['java','go','python']
# file.writelines(lst)
# file.close()
'''
file=open('c.txt','r')
file.seek(2)
print(file.read())  # llohellojavagopython
print(file.tell())  # 22 从0开始计算
file.close()
'''


file=open('d.txt','a')
file.write('hello')
file.flush()
file.write('world')
file.close()  # helloworld






