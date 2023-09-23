#定义一个类，内含私有成员变量
class Phone:
    __current_voltage =1#当前手机运行电压

    def __keep_single_core (self):
        print("让CPU以单核模式运行")
    def call_by_5g(self):
        if self.__current_voltage>=1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话，并设置CPU单核模式运行")
phone=Phone()
#私有方法不能在外部被调用
# phone.__keep_single_core()
phone.call_by_5g()