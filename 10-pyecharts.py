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
line.set_global_opts(
    #用来设置标题
    title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_bottom="1%"),
    #设置图例
    legend_opts=LegendOpts(is_show=True ),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),

)
#通过render生成图表
line.render()
