#发工资案例
#公司余额共10000元,要给20名员工发工资
sum=10000
per=20
#已发放的员工个数为i
i=0
for x in range(0,20):
    import random
    #利用随机数给员工定义一个绩效分num
    num=random.randint(1,10)
    #绩效分小于5的不发放工资
    if num<5:
        print(f"员工{x+1}，绩效分{num}，低于5，不发工资，下一位。")
    #其余则发放工资1000元
    else:
        #余额对应减去
        sum -=1000
        print(f"向员工{x+1}发放工资1000元，账户余额还剩余{sum}元。")
        #已发放的员工个数＋1
        i+=1
    if sum>0:
        continue
    else:
        break
print("工资发完了，下个月再领取吧。")
print("已发放员工个数",i)

