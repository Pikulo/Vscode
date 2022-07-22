# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/3  16:36

class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print('姓名:{0},年龄:{1}'.format(self.name,self.age))

class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score=score
    def info(self):
        super().info()
        print('学号：{0}'.format(self.score))
    def __str__(self):
        return '我的名字是{0}，今年{1}岁'.format(self.name,self.age)

stu=Student('Jack',20,'1001')
stu.info()
print(dir(stu))
print(stu)
print(stu.__dict__)
