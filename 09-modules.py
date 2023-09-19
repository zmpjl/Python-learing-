# #导入模块
# # import time
# #同样代表导入全部功能
# #但下面方法可以不用写time.sleep，可以直接写sleep
# #导入某个具体的功能
# # from time import sleep
# print("你好")
# # sleep(5)#通过.调用模块中的功能
# print("你好")
# #给time起了个名字叫t
# # t.sleep(2)
# print("你好")
# #利用all变量，改变了*的调用范围，从而使调用test_a出错
# import my_package.my_module as m
# m.test_a(8,9)
# #一方面，如果同时调用两个模块中的同名函数，后调用的会覆盖前面调用的
# #另一方面，在调用模块时，相当于把对应模块全部执行了一遍，所以如果模块中有输出，依然会执行
# import my_package.my_module2
# my_package.my_module2.info_print2()
from my_package import *
my_module.test_a(6,3)
#由于__init__中的__all__导致my_packa中只有module能被调用