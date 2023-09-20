def print_file_info(file_name):
    """
    功能：打开对应文件，若不能打开，捕获报错
    :param file_name:
    :return:
    """
    s=None
    try:
        s=open(file_name,"r",encoding="UTF-8")
        print("打开文件成功！")
    except Exception as e:
        print("打开文件错误，文件不存在")
        print(f"出现了错误，错误为{e}")
    finally:
        if s:#如果未能打开相应文件，s为None语句不执行
            s.close()
            print("打开文件完成，已为您关闭文件")
        else:
            print("文件不存在，未能关闭")
def append_to_file(file_name,data):
    """
    功能：将指定data数据追加到文件中
    :param file_name:指定的文件路径
    :param data:要追加的内容
    :return:None
    """
    s=open(file_name,"a",encoding="UTF-8")
    s.write(data)
    print("追加完成，打开文件查看一下吧！")
