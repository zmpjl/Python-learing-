#str_util模块

#str_reverse函数将字符串反转后返回
def str_reverse(s):
    """
    功能：将输入字符串反转后输出
    :param s:
    :return:
    """
    strin=s[::-1]
    print(strin)
    return strin
def substr(s,x,y):
    """
    功能：将输入字符串在x和y处分隔，然后输入三个新的字符串
    :param s:
    :param x:
    :param y:
    :return:
    """
    st1=s[:x:1]
    st2=s[x:y:1]
    st3=s[y::1]
    print(st1)
    print(st2)
    print(st3)
