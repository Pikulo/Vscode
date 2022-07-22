# -*- encoding=utf-8 -*-
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/7/26  17:49

from bs4 import BeautifulSoup   # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request,urllib.error  #制定URL，获取网页数据
import xlwt # 进行Excel操作
import sqlite3 # 进行SQLite数据库操作
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码,解决解码报错问题

def main():
    baseurl="https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist=getDATA(baseurl)
    #2.解析数据(逐一解析)
    savepath=".\\豆瓣电影Top250.xls" # \表示保存到当前文件系统，第一个\表示转义字符。
    #3.保存数据
    saveDATA(datalist,savepath)
    # askURL("https://movie.douban.com/top250")

# 影片详情的规则
findlink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式规则
# 影片图片的规则
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S) #re.S让换行符包含在字符中
# 影片的片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 影片相关内容
finBd = re.compile(r'<p class="">(.*?)</p>',re.S)


# 爬取网页
def getDATA(baseurl):
    datalist=[]
    for i in range(0,10): # 调用获取页面信息的函数*10次
        url = baseurl + str(i*25)
        html = askURL(url)   # 保存获取到的网页源码

        # 逐一解析每一网页数据
        soup = BeautifulSoup(html,'html.parser') #用靓汤模块把文档放在内存里
        # html.parser解析器解析html
        for item in soup.find_all('div',class_="item"):  # 查找符合要求的字符串，形成列表
            # print(item)
            data = [] # 保存一部电影的所有信息
            item = str(item)
            # 影片详情的连接
            link = re.findall(findlink,item)[0]  # 通过正则表达式查找指定字符串
            data.append(link) # 添加链接
            ImgSrc = re.findall(findImgSrc,item)[0] # 添加图片
            data.append(ImgSrc)
            titles = re.findall(findTitle,item)
            if(len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle) # 添加中文名
                otitle = titles[1].replace('/','') # 去掉无关符号
                # otitle=titles[1].replace('\xa0', '').encode('utf-8')
                # otitle=''.join(titles[1].split())
                data.append(otitle) # 添加外国名
            else:
                data.append(titles[0])
                data.append('') # 外国名留空
            rating = re.findall(findRating,item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge,item)
            data.append(judgeNum)

            inq = re.findall(findInq,item)
            if len(inq) != 0:
                inq = inq[0].replace('。','')
                data.append(inq)
            else:
                data.append('')
            bd = re.findall(finBd,item)[0]
            bd = re.sub('<br(\s+?)/>（\s+）?','',bd) #去掉<br/>
            bd = re.sub('/','',bd)
            data.append(bd.strip())

            datalist.append(data)
    print(datalist[0][3])
    print(type(datalist[0][3]))
    return datalist

# 得到指定URL的网页内容
def askURL(url):
    head = {            # 模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 92.0.4515.107Safari / 537.36"
    }
                       # 用户代理，表示告诉豆瓣服务器，我们是什么类型的浏览器
    request=urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
        # print(response.read().decode("utf-8"))
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

# 保存数据
def saveDATA(datalist,savepath):
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)
    col = ('电影详情链接','图片链接','影片中文名','影片外国名','评分','评价数','概况','相关信息')
    for i in range(0,8):
        sheet.write(0,i,col[i]) #列名
    for i in range(0,250):
        print('第%d条'%(i+1))
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])
    print('爬取完毕')
    book.save('豆瓣电影Top250-爬虫爬取.xls')  # 保存
if __name__ == "__main__":
# 调用函数
    main()