
#从1开始到4结束，步长为1，可省略不写
my_list=[0, 1, 2, 3, 4, 5, 6]
result1=my_list[1:4]
print(result1)
#从头开始到尾结束，步长为1
my_tuple=(0,1,2,3,4,5,6)
print(my_tuple[:])#起始和结束可省略不写
#从头开始，到尾结束，步长为2
my_str="0123456"
print(my_str[::2])
#从头到尾步长为-1
print(my_str[::-1])
#对列表从尾到头，步长为-1
print(my_list[3:1:-1])
#对元组，从头到尾，步长为-2
print(my_tuple[::-2])

#课后练习
new_str="万过薪月，员序程马黑来，nohtyP学"
str1=new_str.replace("来","，")
str2=str1.split("，")
str3=str2[1][::-1]
print(str3) 