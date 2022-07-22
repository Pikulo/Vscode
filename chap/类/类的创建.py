# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/1  12:09
'''
class Restaurant():  # 类的定义
    def __init__(self,name,cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type
    def describe_resturant(self):
        print('我的餐厅叫：'+self.name,'菜品有:'+self.cuisine_type)
    def open_restaurant(self):
        print(self.name+'正在营业')
my_resturant=Restaurant('一品轩','烤鸭，鸡翅，鱼排')
my_resturant.describe_resturant()
my_resturant.open_restaurant()
my_resturant=Restaurant('海底捞','捞派毛肚，虾滑，捞面，鹌鹑蛋')
my_resturant.describe_resturant()
my_resturant.open_restaurant()
'''

'''创建User的类'''
'''
class User():
    def __init__(self,first_name,last_name,age,career):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.career=career
    def describe_user(self):
        print('用户名：'+self.first_name+self.last_name,'\n'+'年龄：'+self.age,'\n'+'职业：'+self.career)
    def greet_user(self):
        print('Hello',self.first_name+self.last_name,'Welcome~~~')
user=User('Liu','Mingyang','20','学生')
user.describe_user()
user.greet_user()
user=User('Wu','Yidi','21','学生')
user.describe_user()        
user.greet_user()
'''
'''
class Car():
    """一次模拟汽车的尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_read=0  # 添加一个名为odometer_reading的属性，其初始值总是为0
    def get_describe_name(self):
        """返回简洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name
    def read_odometer(self):
        """打印一条指出汽车里程的信息"""
        print("This car has "+str(self.odometer_read)+" miles on it")
    def update_odomater(self,mileage):
        """将里程碑读数设置为指定值
           禁止将里程表读数回调"""
        if mileage>=self.odometer_read:
            self.odometer_read = mileage
        else:
            print('You can‘t roll back an odometer')  # 现在，update_odometer()在修改属性前检查指定的读数是否合理。
    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        if miles>=0:
            self.odometer_read += miles
        else:
            print('You cant’ roll back')
my_car=Car('Audi','A4',2016)
print(my_car.get_describe_name())
my_car.read_odometer()
my_car.odometer_read=12  # 要修改属性的值，最简单的方式是通过实例直接访问它。下面的代码直接将里程表读数设置为23
my_car.read_odometer()
my_car.update_odomater(33)
my_car.read_odometer()
my_car.update_odomater(20)  # 在里程33基础上调回20
my_car.read_odometer()
my_car.increment_odometer(20)  # 有时候需要将属性值递增特定的量，而不是将其设置为全新的值
my_car.read_odometer()
my_car.increment_odometer(-20)  # 有时候需要将属性值递增特定的量，而不是将其设置为全新的值
my_car.read_odometer()
'''
"""
class Restaurant():  # 类的定义
    def __init__(self,name,cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type
        self.number_served=0
        self.eated_number=0
    def describe_resturant(self):
        print('我的餐厅叫：'+self.name,'菜品有:'+self.cuisine_type)
    def ested_people(self):
        print('餐厅有' + str(my_resturant1.number_served) + '人进餐过')
    def open_restaurant(self):
        print(self.name+'正在营业')
    def set_number_served(self,eated_number1):

        if eated_number1>=0:
            self.eated_number += eated_number1
            print('餐厅最多能容纳' + str(self.eated_number) + '人进餐')
        else:
            print("输入的人数为负")
    def increment_number_served(self,indeed):
        if indeed>=0:
            self.eated_number += indeed
            print('餐厅最多能容纳' + str(self.eated_number) + '人进餐')
        else:
            print('请输入非负数')
my_resturant1=Restaurant('海底捞', '捞派毛肚，虾滑，捞面，鹌鹑蛋')
my_resturant1.describe_resturant()
my_resturant1.open_restaurant()
my_resturant1.number_served=55
my_resturant1.ested_people()
my_resturant1.set_number_served(60)
my_resturant1.increment_number_served(10)
"""
