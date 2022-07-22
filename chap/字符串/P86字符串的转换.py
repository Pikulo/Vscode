# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/1/27  14:39
s='天涯共此时'
#编码
print(s.encode(encoding='GBK'))
#在GBK这种编码中，一个中文占两个字符
print(s.encode(encoding='UTF-8'))
#在UTF-8这种编码中，一个中文占三个字符
#解码
byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))
byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))
#编码和解码要对应相同







