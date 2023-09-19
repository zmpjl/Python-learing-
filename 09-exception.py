try:
    f=open("bucunzai.txt","r",encoding="UTF-8")
    print("文件正常打开")

except:
    print("出现异常，因为文件不存在")
    f=open("bucunzai.txt","w",encoding="UTF-8")
#对具体类型的错误进行捕捉
#捕获多个异常
try:
    1/0
    print(name)
except (NameError,ZeroDivisionError) as e:
    print("name未被定义")
    print(e)
#捕获所有异常
try:
    # 1/0
    # print(name)
    # open("anfian.txt","r",encoding="UTF-8")
    print("hello")
except Exception as f:#或者不写
    print("检测到异常")
    print(f)
else:
    print("未检测到异常")
finally:#无论如何都要执行
    print("检测结束，进程运行完毕")

#异常的传递
def func1():
    print("func1开始执行")
    num=1/0
    print("func1执行结束")
def func2():
    print("func2开始执行")
    func1()
    print("func2执行结束")
def main():
    try:
        func2()
    except Exception as f:
        print("出错了")
        print(f)

main()