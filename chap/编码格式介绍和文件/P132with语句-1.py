# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/5  21:31



class MycontentMgr(object):
    def __enter__(self):
        print('enter����������ִ����')
        return self
    def __exit__(self,exc_type,exc_val,exc_tb):
        print('exit����������ִ����')

    def show(self):
        print('show����������ִ����')

with MycontentMgr() as file:
    file.show()
