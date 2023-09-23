#柱状图的绘制
from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import *
#构建柱状图
bar1=Bar()
#添加x轴数据
bar1.add_xaxis(["中国","美国","英国"])
#添加y轴数据
bar1.add_yaxis("GDP",[30,30,20],label_opts=LabelOpts(position="right"))

bar1.reversal_axis()
#构建柱状图
bar2=Bar()
#添加x轴数据
bar2.add_xaxis(["中国","美国","英国"])
#添加y轴数据
bar2.add_yaxis("GDP",[50,50,40],label_opts=LabelOpts(position="right"))

bar2.reversal_axis()
#构建柱状图
bar3=Bar()
#添加x轴数据
bar3.add_xaxis(["中国","美国","英国"])
#添加y轴数据
bar3.add_yaxis("GDP",[60,70,60],label_opts=LabelOpts(position="right"))

bar3.reversal_axis()

timeline=Timeline(
    {"theme":ThemeType.LIGHT}
)

#应该用基础时间线去绘图
timeline.add_schema(
    play_interval=1000, #自动播放的时间间隔，单位毫秒
    is_timeline_show=True, #是否在自动播放的过程中显示时间线
    is_auto_play=True, #是否自动播放
    is_loop_play=True, #是否循环播放
)

def choose_sort_key(element):
    return element[1]
my_list1=list(bar1).sort(key=choose_sort_key,reverse=False)
my_list2=list(bar2).sort(key=choose_sort_key,reverse=False)
my_list3=bar3.sort(key=choose_sort_key,reverse=False)

timeline.add(my_list1,"点1")
timeline.add(my_list2,"点2")
timeline.add(my_list3,"点3")
timeline.render("时间柱状图.html")