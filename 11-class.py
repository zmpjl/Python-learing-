class Student:
    name = None  # 记录学生姓名
    gender = None  # 记录学生性别
    nationality = None  # 记录学生国籍
    native_place = None  # 记录学生籍贯
    age = None  # 记录学生年龄

    def study(self):  # self的作用之一就是在类函数调用自身变量时，方便区别
        print(f"{self.name} can study A!L!L! D!A!Y!")



Stu1 = Student()
Stu1.name = "周婕纶"
Stu1.gender = "男"
Stu1.nationality = "中国"
Stu1.native_place = "台湾"
Stu1.age = 30


print(Stu1.name)
print(Stu1.gender)
print(Stu1.nationality)
print(Stu1.native_place)
print(Stu1.age)

Stu1.study()

#创建一个闹钟
class Clock:
    #因为init的使用，可忽略不写
    # id=None
    # price=None
    def ring(self):
        import winsound
        winsound.Beep(2000,3000)#前者代表频率，后者代表时间
    def __init__(self,id,price):
        self.id=id
        self.price=price


Clock1=Clock("3301",20)

# Clock1.ring()
Clock2=Clock("3302",21)
#因为init的使用创建对象的方式有所改变
# Clock2.id="3302"
# Clock2.price=20
# Clock2.ring()
Clock3=Clock("3303",25)