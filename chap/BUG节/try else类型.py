# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/1/31  12:09
# try:
#     a = int(input('请输入第一个整数'))
#     b = int(input('请输入第二个整数'))
#     result = a / b
# except BaseException as e:
#     print('出错了',e)
# else:  # 没错执行else
#     print('计算结果为:',result)

#
# lst=[11,22,33,44]
# # # print(lst[4])  # IndexError   索引从0开始
# # dic={'name':'张三','age':20}
# # # print()
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
my_car=Car('Audi','A4',2016)
print(my_car.get_describe_name())
my_car.read_odometer()
my_car.odometer_read=12  # 要修改属性的值，最简单的方式是通过实例直接访问它。下面的代码直接将里程表读数设置为23
my_car.read_odometer()
