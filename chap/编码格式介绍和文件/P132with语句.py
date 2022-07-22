# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/5  21:31

with open('a.txt','r',encoding='utf-8') as file:  # 离开with语句自动释放资源 避免忘记写close语句
    print(file.read())