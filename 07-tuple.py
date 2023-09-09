#定义元组
tub=(1,2,3,True,"牜")
tub2=()
tub3=tuple()
#元组嵌套
tub4=((1,2,3),(4,5,6))
print(tub4[1][0])
tub5=(0,1,2,3,4,5,6,7)
x=tub5.index(7)
print(x)
#index返回下标
#count统计
tub6=(1,5,1,56,1,43,2,76,1,6,1,5,1,2)
print(tub6.count(1))


#遍历
for element in tub6:
    print(element)
# #元组不能进行修改
# tub5[0]=1
# 但是可以通过嵌套一个列表，从而实现内容改变
tub7=(1,2,[1,2])
tub7[2][0]=0
print(tub7)