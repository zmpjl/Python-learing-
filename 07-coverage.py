def list_while(listx):
    count=0
    while count<len(listx):
        print(listx[count])
        count+=1
stunum=[1,2,3,4,5,6]
list_while(stunum)
#利用for循环，进行更简单的遍历
for element in stunum:
    print(f"list的元素依次是{element}")



#课后作业遍历列表{1,2,3,4,5,6,7,8,9,10},取出其中偶数，并组成一个新列表
num=[1,2,3,4,5,6,7,8,9,10]
num1=list()
for element in num:
    if element%2==0:
        num1.append(element)
print(num1)