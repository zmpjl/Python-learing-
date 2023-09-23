class Student:
    def __init__(self,name,age,):
        self.name=name
        self.age = age
    def __str__(self):
        return  f"我是{self.name}，我今年{self.age}岁拉"
    def __lt__(self, other):
        return  self.age<other.age
    def __le__(self, other):
        return self.age<=other.age
    def __eq__(self, other):
        return self.age==other.age
Stu1=Student("周婕纶",40)
Stu2=Student("林君姐",36)
print(Stu1.__lt__(Stu2))
#也可以直接用大于号或小于号表示(这个操作是lt方法提供的
print(Stu1<Stu2)
print(Stu1>Stu2)
print(Stu1<=Stu2)
print(Stu1>=Stu2)