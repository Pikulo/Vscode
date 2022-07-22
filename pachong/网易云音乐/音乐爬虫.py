# -*- encoding=utf-8 -*-
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/7/29  14:22
import requests
from lxml import etree
url = 'https://music.163.com/#/discover/toplist?id=3778678'
url_base = 'http://music.163.com/song/media/outer/url?id='
response = requests.get(url=url)
# print(response.text) # html代码

html = etree.HTML(response.text)  #数据解析，预处理

id_list = html.xpath('//a[contains(@href,"song?")]')


