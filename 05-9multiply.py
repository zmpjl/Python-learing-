#利用while循环嵌套打印九九乘法表
print("下面将为您打印九九乘法表")
i=1
while i<10:
    j=1
    while j<=i:
        product=j*i
        print(f"{i}*{j}={product}\t",end='')
        j+=1
    print("")
    i+=1