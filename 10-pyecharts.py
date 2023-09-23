#在这个函数中我们来学习建立一个折线图
#导包pyecharts
from pyecharts.charts import Line
from pyecharts.options import *
#创建一个折线图对象
line=Line()
#给折线图添加数据
#添加x轴数据
line.add_xaxis(["中国","美国","英国"])
#添加y轴数据
line.add_yaxis("GDP",[30,20,10])
#设置全局配置通过set_global_opts进行配置
list.set_global_opts(
    #增加工具栏
    toolbox_opts=ToolboxOpts(is_show=True),
    legend_opts=LegendOpts(is_show=True),
    #增加颜色对比
    visualmap_opts=VisualMapOpts(is_show=True),
    #设置title
    title_opts=TitleOpts(title="三国GDP对比图", pos_left="center", pos_bottom="1%"),

)
#通过render生成图表
line.render()
