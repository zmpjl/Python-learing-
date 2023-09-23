#构建柱状图
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

bar2=Bar()
#添加x轴数据
bar2.add_xaxis(["中国","美国","英国"])
#添加y轴数据
bar2.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right"))

bar2.reversal_axis()
bar2.render("基础柱状图.html")