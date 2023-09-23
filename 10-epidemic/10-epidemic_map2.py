#绘制河南省疫情地图
import json

from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

f = open("疫情.txt", "r", encoding="UTF-8")
data = f.read()
f.close()
#将json转换为字典
data_dict = json.loads(data)
city_data_list = data_dict["areaTree"][0]["children"][3]["children"]
#组装每个市和确诊人数为元组，并将各个市数据封装到列表内
data_list=[]
for city_data in city_data_list:
        city_name=city_data["name"]     +"市"                #市名
        city_confirm = city_data["total"]["confirm"]    #确诊人数
        data_list.append((city_name,city_confirm))

print(data_list)
#如有需要   ，可以对单独对象进行添加
data_list.append(("济源市",5))
#创建地图对象
map=Map()
#添加数据
map.add("各市份确诊人数",data_list,"河南")
#设置全局
map.set_global_opts(
    title_opts=TitleOpts(title= "河南疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":9,"lable":"1-9","color":"#CCFFFF"},
            {"min": 10, "max": 49, "lable": "10-49", "color": "#FFFF99"},
            {"min": 50, "max": 99, "lable": "50-99", "color": "#FF9966"},
            {"min": 100, "max": 199, "lable": "100-199", "color": "#FF6666"},
            {"min": 200, "max": 499, "lable": "200-499", "color": "#CC3333"},
            {"min": 500, "lable": "500+", "color": "#990033"}

        ]
    )
)

#生成
map.render("河南疫情地图.html")