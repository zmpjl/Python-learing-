import json
data=[{"name":"张大山","age":11},{"name":"王大锤","age":13},{"name":"赵小虎","age":16}]
json_str=json.dumps(data,ensure_ascii=False)#ensure_ascii保证能正确展示中文，如果没有中文，可以不带
print(json_str)
print(type(json_str))
#将字符串还原回列表用json中的load
s='[{"name":"张大山","age":11},{"name":"王大锤","age":13},{"name":"赵小虎","age":16}]'
l=json.loads(s)
print(l)
print(type(l))