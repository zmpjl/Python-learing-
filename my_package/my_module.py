__all__=["test_b"]#用all来定义能调用哪些函数
def test_a(a,b):
    print(a+b)
def test_b(a,b):
    print(a-b)
#利用if判断从而防止在其他程序中调用模块时，执行if中的语句，又能保证if中语句在单独执行模块时，正常执行
if __name__ == '__main__':
    test_a(1,2)