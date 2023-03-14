#猜心中的数字（利用ifelif语句对一个固定数字进行判断）
num=5
if int(input("请从0-10之间猜想一个可能的数字"))==num:
    print("恭喜你，第一次就猜对了")
elif int(input("猜错了，请再猜一遍"))==num:
    print("恭喜你，猜对了")
elif int(input("猜错了，还有一次机会"))==num:
    print("恭喜你，最后一次猜对了")
else:
    print("机会用完了，没猜对哦，要猜的数字是",num)