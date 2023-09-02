#定义一个函数检测句子长度
def str_len(data):
    """
    str_len函数检测句子长度
    :param data:检测的句子
    :return:
    """
    count = 0
    for i in data:
        count +=1
    print(f"字符串{data}的长度为{count}")
def sayhi():
    while True:
        print("请输入一个任意字符串")
        str_len(input())
        print("谢谢你的使用，按1重置,或按其他退出程序。")
        count2 = input()
        if count2 != "1":
            print("检测错误，退出程序")
            break
        else:
            continue

    return 0




count3=sayhi()

if count3==0:
    print("感谢使用！")
