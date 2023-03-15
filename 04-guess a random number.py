#猜一个随机数字
#产生一个随机数num
import random
num=random.randint(1,10)
print("现在有一个0-10之间的随机整数")
print("请您猜出数字的具体值")
print("您共有三次猜测机会")
guess1=int(input("请写出您的第一次猜想："))
if guess1==num:
    print("恭喜您第一次就猜中了！")
else:
    if guess1>num:
        print("您猜的数字偏大。")
    else:
        print("您猜的数字偏小。")
    guess2=int(input("请写出您的第二次猜想："))
    if guess2==num:
        print("恭喜你第二次就猜中了！")
    else:
        if guess1 > num:
            print("您猜的数字偏大。")
        else:
            print("您猜的数字偏小。")
        guess3=int(input("请写出您的第三次猜想："))
        if guess3==num:
            print("恭喜你打三次猜中了！")
        else:
            print("对不起，您三次机会使用完了，还没有猜中哦，再试一次吧。")
print("")
print("程序结束，欢迎下次使用！谢谢！")