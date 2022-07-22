# -*- encoding=utf-8 -*-
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/7/29  8:57
import json
import pprint
from bs4 import BeautifulSoup
import requests
import re
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码,解决解码报错问题


# 数据抓取
base_url = 'https://player.novipnoad.com/vod/ts/0dSxvbW-KRBi8xghlePjVHAsHPOvsT9n5oB_nwopRzfccEeA7E6ctf5S2695dpZKLpawtIXgnAmp3evIdY5PD_ApXQ71OguW4dfIzrXy_2WEi5SZasVjHA' #开发者模式修改

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'cookie': 'Hm_lvt_adb3aa71d67f562e9968e77648b4008c=1627519572; Hm_lpvt_adb3aa71d67f562e9968e77648b4008c=1627521537',
    'referer': 'https://www.novipnoad.com/movie/'
}
response = requests.get(base_url,headers=headers) # 第一次请求
# print(response)
# print(response.status_code) # 200说明能访问
data = response.text
print(data)
pprint.pprint(data)
# title = re.findall('content="(.*?)"><meta property="og:type" ', data)
# print(re.findall('content="(.*?)"><meta property="og:type" ', data))
# 提取视频对应的json数据

# json_data = re.findall('<meta property="og:url" content="(.*?)">',data)[0]
# print(json_data)

# f = open(json_data, encoding = 'utf-8')
# str = f.readline()
# json_data = json.loads(str)
# pprint.pprint(json_data)


video_title = title+'.mp4'
video_url = json_data
print(video_title,video_url)
print('正在下载')
# 第二次请求
# video_data = requests.get(video_url,headers=headers).content # 二进制
# with open(r'./视频/'+video_title,'wb') as f:
#     f.write(video_data)
#     print('下载完成\n')








