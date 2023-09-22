from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
from pyecharts.types import VisualMap

map = Map()
data = [
    ("北京市", 99),
    ("上海市", 199),
    ("江苏省", 299),
    ("台湾省", 399),
    ("广东省", 499),
]
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":9,"label":"1-9","color":"#CCFFFF"},
            {"min":10,"max":99,"label":"10-99","color":"#FF6666"},
            {"min":100,"max":999,"label":"100-999","color":"#990033"}
    ]),

)
map.add("测试地图", data, "china")
map.render("testmap.html")
