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
#新增元素操作
my_dic["20211120008"]={"语文":88,"数学":86,"英语":75}
print(my_dic)
#更新字典
my_dic["20211120008"]["语文"]=90
print(my_dic)
#删除元素,通过pop语句可以删除并得到对应key的语句
mydict2=my_dic.pop("20211120008")
print(mydict2)
print(my_dic)
mydict2.clear()
print(mydict2)
#返回所有key值
keys=my_dic.keys()
print(f"这里是keys{keys}")
for key in keys:
    print(key)
    print(f"对应的value值是{my_dic[key]}")
#直接从字典中获取key值
for key in my_dic:
    print(key)
    print(f"对应的value值是{my_dic[key]}")
#统计字典的元素数量
print(len(my_dic))
#课后练习
my_staff={
    "王力宏":{
        "部门":"科技部",
        "工资":3000,
        "级别":1
    },
    "周杰伦":{
        "部门":"市场部",
        "工资":5000,
        "级别":2
    },
    "林俊杰":{
        "部门":"市场部",
        "工资":7000,
        "级别":3
    },
    "张学友":{
        "部门":"科技部",
        "工资":4000,
        "级别":1
    },
    "刘德华":{
        "部门":"市场部",
        "工资":6000,
        "级别":2
    }
}
print(my_staff)
for key in my_staff:
    if my_staff[key]["级别"]==1:
        my_staff[key]["工资"] =my_staff[key]["工资"]+1000
        my_staff[key]["级别"] =my_staff[key]["级别"]+1
print(my_staff)