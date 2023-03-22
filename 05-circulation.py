#利用while循环写1-100的加法
print("下面将展示1-100的加法结果")
i=0
Sum=0  
while i<=100:
    Sum=Sum+i
    i +=1
print("1-100的和为",Sum)
#循环的嵌套
day=1

while day<=100:
    print(f"这是我跟小小表白的第{day}天。")
    day += 1
    flower = 1
    while flower<=10:
        print(f"这是我今天送给小小的第{flower}支花")
        flower +=1
print("我真喜欢小小吧")

#end 和\t的使用
print("Hello",end=" ")
print("World")
print("Hello",end=" ")
print("World",end=" ")
print("Hello",end=" ")
print("World")
print("Hello\tWorld")
print("Hello World")