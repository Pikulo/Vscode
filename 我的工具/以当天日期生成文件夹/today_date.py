# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/11  8:28
import os
import time
from datetime import date
os.chdir('F:\\微信公众号\\公众号素材\\一句晚安')
d=date.today()
m=str(d).replace('-','.')
# print(d,type(d))
# d.isoformat()
# print(d,type(d))
# file=open('{0}'.format(d),'a',encoding='utf_8')
os.mkdir('{0}'.format(m))