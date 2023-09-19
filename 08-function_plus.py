#函数多个返回值
import random


def print_add():
    x=random.randint(0,10)
    y=random.randint(0,10)
    z=x+y
    return x,y,z
x,y,z=print_add()
print(f"{x}+{y}={z}")
#函数传入参数
#位置参数
def print_data(x,y,z):
    print(f"按照您的输入顺序，依次为{x},{y},{z}")
print_data("ni","hao","a")
#关键字参数
print_data(y="的",z="天",x="我")
#缺省参数
#即如果传入参数，则按传入的使用，如果不传入，则为默认值
def print_stu(age,name,sex="男"):
    print(f"学生姓名：{name}，年龄：{age},性别：{sex}")
print_stu("Dio","08")
print_stu("Lucy","12","女")
#可变长参数
def printf(*args):
    print(args)
printf("tom",18,"男")
def printd(**kwargs):
    print(kwargs)
printd(name= "tom",age=18,sex='男')

#函数的调用
def test_func(computer):
    result=computer(1,2)
    return result
def computer(x,y):
    return x+y
print(test_func(computer))
#lambda匿名函数
def tset_func(computer):
    result=computer(1,2)
    return result
tset_func(lambda x,y:x+y)
