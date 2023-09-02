#简单的for循环初试
name="wangzeping"
for x in name:
    print(x,end="")
print()
#利用for循环对某一字母进行数数
sentence="some times ,we may sdhaucusaubasbubasjubicasbiuohdwwhioggryuyeygftfgtfwdqpmv;ll"
char=input("请输入你要查找的字母")
num=0
for x in sentence:
    if x==char:
        num+=1

print(f"经过统计，这段句子中有{char}，{num}个")
#range的使用，方法一
for x in range(10):
    print(x,end=" ")
print()
for y in range(10):
    print(y,end=" ")
print()
#range的使用，方法二
for x in range(0,10):
    print(x,end=" ")
print()
#range的使用，方法三
for x in range(0,10,2):
    print(x,end=" ")
print()
#continue 的使用
# for x in range(1,10):
#     print("第一句")
#     for x in range(10):
#         print("第二句")
#         continue
#         print("第三句")
#     print("第四句")
#break的使用
for x in range(10):
    print("这是我说的第一句")
    break
