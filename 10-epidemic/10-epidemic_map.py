#读取数据文件
import json

from pyecharts.charts import Map
from pyecharts.options import *

f = open("疫情.txt", "r", encoding="UTF-8")
data = f.read()
#关闭文件
f.close()
#将json转换为字典
data_dict = json.loads(data)
province_data_list = data_dict["areaTree"][0]["children"]
#组装每个省份和确诊人数为元组，并将各个省份数据封装到列表内
data_list=[]
for province_data in province_data_list:
        province_name=province_data["name"]                     #省份名
        province_confirm = province_data["total"]["confirm"]    #确诊人数
        data_list.append((province_name,province_confirm))

print(data_list)
#创建地图对象
map=Map()
#添加数据
map.add("各省份确诊人数",data_list,"china")
#设置全局
map.set_global_opts(
    title_opts=TitleOpts(title= "全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":99,"lable":"1-99","color":"#CCFFFF"},
            {"min": 100, "max": 999, "lable": "100-999", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "lable": "1000-4999", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "lable": "5000-9999", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "lable": "10000-99999", "color": "#CC3333"},
            {"min": 100000, "lable": "100000+", "color": "#990033"}

        ]
    )
)

#生成
map.render("疫情地图.html")