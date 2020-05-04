year = input("请输入一个年份：")
while True:
    if year.isdigit():
        year = int(year)
        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            print("是闰年")
            break
        else:
            print("不是闰年")
            break
    else:
        input("输入错误，请输入整数：")
print("程序结束",end = '')
