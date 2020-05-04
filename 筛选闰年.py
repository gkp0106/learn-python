###编写一个程序，用户输入起始年份year1和结束年份year2，输出[year1,year2]中的所有闰年。要求定义函数判断某一年是否是闰年，是闰年则返回True，否则返回False。闰年为能被4整除，但不能被100整除，或者能被400整除的年份。###
def year(a):
    if isinstance(a, int):
        if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
            return True
        else:
            return False
    else:
        raise TypeError("输入参数不为一个整数")


year1 = int(input("请输入起始年份："))
year2 = int(input("请输入结束年份："))
c = list(filter(lambda a:a % 4 == 0 and a % 100 != 0 or a % 400 == 0,[x for x in range(year1,year2+1)]))
print (c)
for i in range(year1, year2 + 1):
    if year(i):
        print(i)
    else:
        continue