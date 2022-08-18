# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/2  20:37
'''
class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已启动')
car=Car('BWNX5')
car.start()
print(car.brand)
'''

class Student:
    def __init__(self,name,age,career):
        self.name=name
        self.__age=age  # 年龄不希望在类的外部被使用，所以加了两个__
        self.__career=career
    def show(self):
        print(self.name,self.__age)

stu=Student('张三',20,'学生')
stu.show()
# 在类的外部使用name和age
print(stu.name)
print(stu._Student__career)  # 在类的外部可以通过_Student__career访问
#print(stu.__age)
print(dir(stu))  # 通过函数dir查找能访问的类属性
print(stu._Student__age)  # 在类的外部可以通过_Student__age访问
print(stu._Student__age)


