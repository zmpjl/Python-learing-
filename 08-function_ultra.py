#lambda匿名函数
def tset_func(computer):
    result=computer(1,2)
    return result
tset_func(lambda x,y:x+y)
