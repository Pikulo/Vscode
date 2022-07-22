# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/5  14:48
import schedule  # 第三方模块安装
import time
def job():
    print('哈哈——————')

schedule.every(1).seconds.do(job)
while  True:
    schedule.run_pending()
    time.sleep(0)

# 可以用来定时发送邮件
