#文件操作
import time

f=open("测试.txt","r",encoding="UTF-8")
print(type(f))
# print(f"读取十个字节的结果是 {f.read(10)}")
# print(f"读取其余全部内容结果为 {f.read()}")
#由于指针在读取结束后指向最后一个字符，所以继续读没有结果
#如果将前面两行注释掉，则可以正常读取
#print(f"读取全部行封装到列表中的结果是 {f.readlines()}")
# line1=f.readline()
# line2=f.readline()
# line3=f.readline()
# print(f"读取第一行结果为{line1}")
# print(f"读取第二行结果为{line2}")
# print(f"读取第三行结果为{line3}")
# for line in f:
#     print(f"每一行的数据是{line}")
#解除文件占用
# f.close()
#withopen方法，会在执行完withopen中的语句后自动将文件关闭
with open ("测试.txt","r",encoding="UTF-8") as f:
    for line in f:
        print(f"每一行的数据是{line}")
#课后练习
with open("word.txt","r",encoding="UTF-8") as d:
    # result=d.readlines()
    # result1=str(result)
    # print(result1)
    # result1.split(" ")
    # sum=result1.count("itheima")
    # print(sum)
    result=d.read()
    print(result)
    sum=result.count("itheima")
    print(sum)
#写入
file=open("test.txt","w",encoding="UTF-8")
file.write("hello world")#写入内存中
file.flush()#写入硬盘
file.close()#close中内置了flush即刷新的功能
#add
file=open("test.txt","a",encoding="UTF-8")
file.write("\nif you give me a chance i will kill you")
file.close()

#课后作业
hw=open("bill.txt","r",encoding="UTF-8")
wr=open("bill.txt.bak","w",encoding="UTF-8")

hw.read()
hw.seek(0)
# for line in hw:
#     print(line)
#     if line.count("测试")==0:
#         wr.write(line)
#     else:
#         continue
for line in hw:
    if "测试" not in line:
        wr.write(line)
hw.close()
wr.close()