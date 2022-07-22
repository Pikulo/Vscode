# -*- encoding=utf-8 -*-
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/7/26  18:45
import urllib.request
import certifi
# 获取一个get请求
# reponse=urllib.request.urlopen("http://www.baidu.com")
# print(reponse)
# html = reponse.read().decode('utf-8') # 对获取的网页源码进行utf-8解码
# print(html)

# 获取一个Post请求，模拟用户真实登录
# import urllib.parse # 解析器
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8") # 把字典内容封装成byte数组
# reponse=urllib.request.urlopen("http://httpbin.org/post",data=data) # 用post方式封装数据
# print(reponse.read().decode("utf-8"))

# 验证get请求

# 超时处理
# try:
#     reponse=urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(reponse.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print('timeout')

# reponse=urllib.request.urlopen("http://www.baidu.com")
# print(reponse.getheaders()) # 浏览器里header的信息
# print(reponse.getheader("Server")) # 获取sever的内容

# 伪装为浏览器
## url = "https://www.douban.com"
# #测试
# url="http://httpbin.org/post"
# headers = {
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response=urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

# 访问豆瓣
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码,解决解码报错问题
url = "https://www.douban.com"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
}
req = urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(req)
print(response.read().decode("utf-8"))







