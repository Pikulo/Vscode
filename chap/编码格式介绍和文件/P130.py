# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/5  16:16
'''
import schedule  # 第三方模块安装
import time

def job():
    i = 0
    print('——————')
    file = open('b.txt', 'a')
    file.write('{0}helloworld\n'.format(i))
    file.close()
    i += 1
schedule.every(1).seconds.do(job)
while  True:
    schedule.run_pending()
    time.sleep(0)
'''
'''
# 图片的复制
src_file=open('112.png','rb')
target_file=open('copy112.png','wb')
target_file.write(src_file.read())
target_file.close()
src_file.close()
'''