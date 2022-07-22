# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/4  11:18
'''
a=10
b=200
c=a+b  # 两个整数类型的相加操作
d=a.__add__(b)

print(c)
print(d)

class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):  # 为实现加法操作 这个必不可少
        return self.name+other.name
    def __len__(self):
        return len(self.name)
stu1=Student('张三')
stu2=Student('Jack')
s=stu1+stu2  # 实现了两个对象的加法运算（因为在Student类中 编写了————add————的特殊操作）
print(s)
s=stu1.__add__(stu2)
print(s)
print('__________________________________')
lst=[11,22,33,44]
print(len(lst))  # len是内容函数
print(lst.__len__())
# print(len(stu1))  # TypeError: object of type 'Student' has no len()
print(len(stu1))
print(len(stu2))
'''

class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj=super().__new__(cls)
        print('创建的对象的id为：{0}'.format(id(obj)))

    def __init__(self, name, age):
        print('__init__被调用了，self的id值为：{0}'.format(id(self)))
        self.name = name
        self.age = age

print('object这个类对象的id为：{0}'.format(id(object)))
print('Person这个类对象的id为：{0}'.format(id(Person)))

# 创建Person类的实例对象
p=Person('liu',30)
print('p这个Person类的实例对象的id：{0}'.format(id(p)))



