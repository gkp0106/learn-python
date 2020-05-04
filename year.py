year = lambda a: a % 4 == 0 and a % 100 != 0 or a % 400 == 0
while 1:
    year1 = int(input("请输入起始年份："))
    year2 = int(input("请输入结束年份："))
    if year1 >= 1 and year2 >= year1:
        for i in filter(year, range(year1, year2 + 1)):
            print(i)
        break
    else:
        print("输入有误，起始年份应大于等于1，同时结束年份不应小于起始年份，请修改")