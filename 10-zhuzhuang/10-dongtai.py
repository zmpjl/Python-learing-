#打开文件
from pyecharts.charts import Timeline, Bar
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts

f=open("1960-2019全球GDP数据.csv","r",encoding="ANSI")
data_lines=f.readlines()
f.close()
#删除第一条无用数据
data_lines.pop(0)
#将数据转换为字典储存，格式为：
#{年份：[[国家，GDP][国家，GDP]…],年份：————————}
data_dict={}
for  line in data_lines:
    year=line.split(",")[0]
    country=line.split(",")[1]
    gdp=float(line.split(',')[2])
    #如何判断字典里有没有指定的key
    try:
        data_dict[year].append([country,gdp])
    except KeyError:
        data_dict[year]=[]
        data_dict[year].append([country,gdp])

keys=data_dict.keys()
timeline=Timeline(
    {"theme":ThemeType.LIGHT}
)
#排序年份

final_year_list=sorted(keys)

for year in final_year_list:
    time_list=data_dict[year].sort(key=lambda element: element[1],reverse=True)
    #取出前八的国家
    year_data=data_dict[year][0:8]
    x_data=[]
    y_data=[]
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1]/100000000)
    bar=Bar()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)",y_data,label_opts=LabelOpts(position="right"))
    x_data.reverse()
    y_data.reverse()
    #反转xy轴
    bar.reversal_axis()

    #
    timeline.add(bar,str(year))
#设置播放设置
timeline.add_schema(
    play_interval=1000, #自动播放的时间间隔，单位毫秒
    is_timeline_show=True, #是否在自动播放的过程中显示时间线
    is_auto_play=True, #是否自动播放

)

timeline.render("1960年到2019年全球GDP前八的国家.html")