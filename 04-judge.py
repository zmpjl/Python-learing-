# python中的if语句
print("请输入你的年龄")
age = input()
print(f"你今年{age}岁了。")
age=int(age)
if age >= 18:
    print("已经没有防沉迷限制了（喜）")
else:
    print("还有未成年防沉迷限制（悲）")
print(" have a happy college life ")

#多条件判断
print("请输入你的身高：")
height=int(input())
if height<140:
    print(f"您好，您的身高为{height}，可以购买儿童票")
elif height<160:
    print(f"您好，1您的身高为{height}，可以购买学生半价票")
else :
    print(f"您好，您的身高为{height}，只能购买成人票")