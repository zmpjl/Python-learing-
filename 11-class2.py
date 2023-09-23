#开学了有一批学生信息需要录入系统，请设计一个类，记录学生的:姓名、年龄、地址，这3类信息
# 请实现:
# 通过for循环，配合input输入语句，并使用构造方法，完成学生信息的键盘录入·输入完成后，使用print语句，完成信息的输出
class Student:
    def __init__(self,name,age,location):
        self.name=name
        self.age=age
        self.location=location
    def __str__(self):
        return f"【学生姓名：{name}，年龄：{age}，地址：{location}】"
Stu_meau=[]
for i in range(1,11):

    print(f"当前录入第{i}位学生信息，总共需要录入10位学生信息")
    print(f"请输入学生姓名:")
    name=input()
    print(f"请输入学生年龄:")
    age = input()
    print(f"请输入学生地址:")
    location = input()
    Stu=Student(name,age,location)
    Stu_meau.append(Stu)
    print(f"学生{i}信息录入完成，信息为：【学生姓名：{name}，年龄：{age}，地址：{location}】")
    continue
