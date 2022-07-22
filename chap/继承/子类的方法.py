# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/1  16:11
'''
class Car(object):  # 在Python2.7中使用继承时，务必在定义父类时在括号内指定object。
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
class Battery():
    def  __init__(self):
        battery_size = 70

        self.battery_size=battery_size
    def describe_battery(self,car_model):
        self.car_model = car_model
        print('This car has a  '+str(self.battery_size)+'-kWh battery')
        if  self.car_model=='ELC'  and self.battery_size==70:
            range=240
            print('This car can go appoximately ' + str(range) + 'miles on a full charge')
        elif self.car_model=='ELC' and self.battery_size==85:
            range=270
            print('This car can go appoximately ' + str(range) + 'miles on a full charge')
        if self.car_model!='ELC':
            print('非电动车')

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):
        '初始化父类的属性'
        #super(ElectricCar,self).__init__(make,model,year)
        #self.battery_size=70
        super().__init__(make,model,year)  # 子类的方法__init__()需要父类施以援手
        self.battery=Battery()
    #def describe_battery(self):
        #"""打印一条描述电瓶容量的消息"""
        #print('This car has a  '+str(self.battery_size)+'kWh battery')
my_tesla=ElectricCar('tesla','model S',2016)
print(my_tesla.get_describe_name())
my_tesla.battery.describe_battery('ELC')
my_tesla.battery.battery_size=85
my_tesla.battery.describe_battery('EL')
'''











































