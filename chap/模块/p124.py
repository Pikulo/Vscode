# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/5  14:37
import sys
import time
import urllib.request
#  获取对象所占的内存大小
print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))
print(time.time())
print(time.localtime(time.time()))
print(urllib.request.urlopen('http://www.baidu.com').read())

