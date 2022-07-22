# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/2  14:06
class User():
    def __init__(self,first_name,last_name,age,career):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.career=career
        self.login_attempts=0

    def describe_user(self):
        print('用户名：'+self.first_name+self.last_name,'\n'+'年龄：'+self.age,'\n'+'职业：'+self.career)
    def greet_user(self):
        print('Hello',self.first_name+self.last_name,'Welcome~~~')
    def increment_login_attempts(self):
        self.login_attempts+=1
        print('增加过后login_attempts的值为'+str(self.login_attempts))
    def reset_login_attempts(self):
        self.login_attempts=0
        print('重置过后login_attempts的值为' + str(self.login_attempts))
class Admin(User):
    def __init__(self,first_name,last_name,age,career):
        super().__init__(first_name,last_name,age,career)  # 继承父类
        self.privileges = Privileges()
        # privileges=['can add post','can delete post','can ban user']
        # self.privileges = privileges

    # def show_privileges(self):
    #     if self.first_name+self.last_name=='LiuMingyang':
    #         print('Helo!Liumingyang,'+'you '+self.privileges[0]+' and you '+self.privileges[1]+' and you '+self.privileges[2])
    #     elif self.first_name+self.last_name=='WuYidi':
    #         print('Helo,WuYidi,'+'you '+self.privileges[1])
    #     else:
    #         print('you ' + self.privileges[0])
class Privileges():
    def __init__(self):
        self.privileges=['can add post', 'can delete post', 'can ban user']
    def show_privileges(self):
        if self.first_name+self.last_name=='LiuMingyang':
            print('Helo!Liumingyang,'+'you '+self.privileges[0]+' and you '+self.privileges[1]+' and you '+self.privileges[2])
        elif self.first_name+self.last_name=='WuYidi':
            print('Helo,WuYidi,'+'you '+self.privileges[1])
        else:
            print('you ' + self.privileges[0])
# user=User('Liu','Mingyang','20','学生')
# user.describe_user()
# user.greet_user()
# user=User('Wu','Yidi','21','学生')
# user.describe_user()
# user.greet_user()
# for i in range(6):
#     user.increment_login_attempts()
# user.reset_login_attempts()
admin=Admin('Liu','Mingyang','20','学生')
admin.privileges.show_privileges()
admin=Admin('Wu','Yidi','21','学生')
admin.privileges.show_privileges()
admin=Admin('LLLL','Yidi','21','学生')
admin.privileges.show_privileges()





