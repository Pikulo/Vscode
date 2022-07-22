# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/5  21:31



class MycontentMgr(object):
    def __enter__(self):
        print('enter方法被调用执行了')
        return self
    def __exit__(self,exc_type,exc_val,exc_tb):
        print('exit方法被调用执行了')

    def show(self):
        print('show方法被调用执行了')

with MycontentMgr() as file:
    file.show()
