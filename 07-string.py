#字符串实际上也是一种数据容器
my_str="oh you djajdioajdi"
char=my_str[3]
char2=my_str[-5]
print(char2)
print(char)
#string类型不能进行修改操作
#my_str[2]=y
#replace方法
#replac（x,y）将原字符串中的x替换为y，并生成新的字符串
new_str=my_str.replace("d","x")
print(new_str)
#split方法，分割，得到列表对象
my_str="hello vab vab bub dub"
my_str_list=my_str.split(" ")
print(my_str_list)
#strip方法，默认去除字符串前后空格或回车
my_str="   hello vab vab bub dub   "
strip_my_str=my_str.strip()
print(my_str)
print(strip_my_str)
print(my_str.strip(" hb"))
#count,计数字符串出现次数，不做演示
#len，长度返回
#遍历
for x in my_str:
    print(x)
#课后练习
learn_str="itheima itcast boxuegu"
print(learn_str.count("it"))
new_learn_str=learn_str.replace(" ","|")
print(new_learn_str)
print(new_learn_str.split("|"))