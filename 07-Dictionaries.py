#字典的定义
my_dic={"20211120007":"王泽平","20211120044":"王致权","20211120000":"小白"}
print(my_dic)
my_dict={}
mydict1=dict()
print(my_dic["20211120007"])
print(my_dic["20211120000"])
my_dic={
    "20211120007": {
        "语文":99,
        "数学":66,
        "英语":20
    },
    "20211120044":{
        "语文":86,
        "数学":89,
        "英语":99
    },"20211120000": {
        "语文":89,
        "数学":89,
        "英语":89
    }}
print(my_dic)
#查询成绩
print(my_dic["20211120044"]["语文"])