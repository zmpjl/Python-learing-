#用print打印一个数据类型
print(type(0.666))
print(type("string"))
print(type(6))
#使用变量存储type输出的数据结构类型
int_type=type(6)
str_type=type("string")
float_type=type(0.66)
print(int_type)
print(str_type)
print(float_type)
#查看变量内存储的数据类型
i=6
s="string"
f=0.66
print(type(i))
print(type(s))
print(type(f))

#shu数据类型转换。
print(int(0.66))
print(str(6))
print(float(6))

#转义字符\的使用
print("\"你好\"")

#字符串拼接
name="David"
print("my"+" name is "+name)
#字符串拼接pro
num=100
print("my name is %s %s" %(name,num))
print('my name is %s %d' % (name, num))

#数字精度控制
print("%5d" %i)
print("%.5f" %f)

#占位符 f:format
print(f"{name}'s number is {num}")