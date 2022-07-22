# -*- encoding=utf-8 -*-
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/7/28  23:38
# -*- encoding=utf-8 -*-
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/7/28  19:00
import os

import requests
import re
import pprint
import json
import subprocess
from ffmpy import FFmpeg
import winsound

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码,解决解码报错问题

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'referer': 'https://passport.bilibili.com/login?from_spm_id=333.851.top_bar.login_window',
    'Cookie': '_uuid=D3650EC8-4C13-7983-2392-3388182BFC3350873infoc; buvid3=B60F5129-85A7-42CD-A889-677ADE4C829034749infoc; sid=ixamiwlt; fingerprint=59cea74cb3fe7b98b682dc96622f1537; buvid_fp=B60F5129-85A7-42CD-A889-677ADE4C829034749infoc; buvid_fp_plain=80B17262-12E0-4F2E-AA15-CF7D036BDE2B34787infoc; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(u)mmY|Yum~0J.\'uYumlkmJ)u; PVID=1; LIVE_BUVID=AUTO3016220187960243; bp_video_offset_394444754=545653767934136232; CURRENT_BLACKGAP=1; CURRENT_QUALITY=80; bp_t_offset_29563732=553604409532513930; SESSDATA=340361c8%2C1643594711%2C8bff8%2A81; bili_jct=31f7aebd4c0fda2e63f7b38c7b46b9dd; DedeUserID=282107851; DedeUserID__ckMd5=ef564c2e29a66ec6'
}


def send_request(url):
    response=requests.get(url=url,headers=headers)
    return response
# 改变网址
html_data=send_request('{0}'.format(input('网址:'))).text
def get_video_data(html_data):
    # 有问题
    # try:
    title = re.findall('<h1 title="(.*?)">(.*?)</h1>', html_data)[0]  #tit tr-fix或者tit
    # except IndexError:
    #     pass ((tit tr-fix)|(tit))
    title = title[0]
    print(title)
    # print(re.findall('<h1 title="(.*?)">(.*?)</h1>', html_data)[0][0])
    # 提取视频对应的json数据
    json_data = re.findall('<script>window\.__playinfo__=(.*?)</script>', html_data)[0]
    # print(json_data)
    json_data = json.loads(json_data)
    pprint.pprint(json_data)

    # 提取音频的url
    audio_url=json_data['data']['dash']['audio'][0]['backupUrl'][0]
    # print('解析到的音频地址：',audio_url)

    # 提取视频
    video_url = json_data['data']['dash']['video'][0]['backupUrl'][0]
    # print('解析到的音频地址：', video_url)

    video_data = [title,audio_url,video_url]
    return video_data
def save_data(file_name,audio_url,video_url):
    # 请求数据
    print('正在请求音频数据')
    audio_data = send_request(audio_url).content
    print('正在请求视频数据')
    video_data = send_request(video_url).content
    with open(r'./B站视频/' + file_name + '.mp3', 'wb') as f:
        f.write(audio_data)
        print('正在保存音频数据')

    with open(r'./B站视频/' + file_name + '.mp4', 'wb') as f:
        f.write(video_data)
        print('正在保存视频数据')

def merge_data(video_name):
    '''数据合并'''
    print('视频合并开始:',video_name)
    # outfile_name = video_name.split('.')[0] + '-new.mp4'
    # cmd = f'E:\\FFmpeg\\bin\\ffmpeg -i {video_name}.mp4 -i -i {video_name}.mp3 -acodec copy -vcodec copy {outfile_name}.mp4'
    # print(cmd)
    # subprocess.call(cmd, shell=True)
    # COMMAD = f'ffmpeg -i {video_name}.mp4 -i {video_name}.mp3 -c:v copy -c:a aac -strict experimental output.mp4'
    # subprocess.call(COMMAD, shell=True)
    # subprocess.Popen(COMMAD,shell=True)


    mp4_f = 'E:/PyCharm/learning/kiddo的学习日志/pachong/B站视频/B站视频/'+video_name+'.mp4'  # 类似这样"F:/xxx/xxxxx.webm"  视频文件
    mp3_f = 'E:/PyCharm/learning/kiddo的学习日志/pachong/B站视频/B站视频/'+video_name+'.mp3'
    n_mp4_n = 'new ' + mp4_f.split('/')[-1]
    n_mp4_f = mp4_f.replace(mp4_f.split('/')[-1], n_mp4_n)
    com = f'E:\\FFmpeg\\bin\\ffmpeg.exe -i "{mp3_f}" -i "{mp4_f}" ' \
          f'-acodec copy -vcodec copy "{n_mp4_f}"'
    # print(com)
    os.system(com)
    os.remove('E:/PyCharm/learning/kiddo的学习日志/pachong/B站视频/B站视频/' + video_name + '.mp4')
    os.remove('E:/PyCharm/learning/kiddo的学习日志/pachong/B站视频/B站视频/' + video_name + '.mp3')
    print('视频合成结束：',video_name)

    # 提醒
    duration = 500  # 持续时间以毫秒为单位
    freq = 440  # Hz
    winsound.Beep(freq, duration)  # 叮~~~

# print(html_data)
video_data = get_video_data(html_data)
save_data(video_data[0],video_data[1],video_data[2])
merge_data(video_data[0])







