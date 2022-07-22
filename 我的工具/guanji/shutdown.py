# -*- encoding=utf-8 -*-
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2022/3/6  12:13
import os
minute=input("您想设置多少分钟后关机？格式：1 30 表示1小时30分钟后关机\n")
list_minute = [int(n) for n in minute.split()]
# print(list_minute)
int_minute=list_minute[0]*60+list_minute[1]
# print(int_minute)
def shutdown(int_minute):
    string="shutdown -s -t "+ str(int_minute)
    os.system(string)

if input("您确定关机？输入 是的 以关机") == "是的":
    shutdown(int_minute)
else:
    print("好的")