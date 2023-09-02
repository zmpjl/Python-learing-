def log_in():
    """
    登录函数，可以通过链接数据库实现多用户登录
    目前，采用固定用户名和密码登录方式
    :return:
    """
    while 1:
        print("输入你的用户名：")
        user_name=input()
        print("输入你的密码：")
        user_key=input()
        if user_name=="pinger"and user_key=="123456":
            return user_name
            break
        else:
            print("用户名或密码错误，请重新输入")
            continue
def menu():
    money=50000
    user_name=log_in()
    while 1:
        print(  f"------------------------主菜单------------------------\n"
                f"{user_name}，您好，欢迎来到ATM在线界面，请选择你要进行的操作：\n"
                f"查询余额   请按1；\n"
                f"存款      请按2；\n"
                f"取款      请按3；\n"
                f"退出      请按4；\n"
                f"请输入您的选择：")
        choice=input()
        if choice=="1":
            print(f"--------------------查询余额----------------------\n"
                    f"{user_name}，您好，您的余额剩余：{money}元。\n"
                    f"即将返回到主菜单，谢谢您的使用\n")
            continue
        elif choice=="2":
            print(f"---------------------存款------------------------\n"
                    f"请输入您要存款的金额:\n")
            add=input()
            while 1:
                if add.isdigit():  # 检查是否可以转换为整数
                    money += int(add)  # 将字符串转换为整数并添加到现有金额中
                    break
                else:
                    print("存款的金额必须是一个数字")
                    continue
            print(f"{user_name},恭喜您，存款{add}元成功。\n"
                    f"当前账户余额剩余{money}元。\n"
                    f"即将返回到主菜单，谢谢您的使用\n")
            continue
        elif choice=="3":
            print(f"---------------------取款------------------------\n"
                    f"请输入您要取款的金额:\n")
            minus = input()
            while 1:
                if minus.isdigit():  # 检查是否可以转换为整数
                    money += int(minus)  # 将字符串转换为整数并添加到现有金额中
                    break
                else:
                    print("取款的金额必须是一个数字")
                    continue
            print(f"{user_name},恭喜您，取款{minus}元成功。\n"
                    f"当前账户余额剩余{money}元。\n"
                    f"即将返回到主菜单，谢谢您的使用\n")
            continue
        elif choice=="4":
            print("谢谢您的使用，欢迎下次光临。\n")
            break
        else:
            print("检测到错误输入，即将退回到主菜单。\n")
            continue

menu()