def Dec2Bin(dec):
    temp = []
    while dec:
        quo = dec % 2
        dec = dec // 2
        quo = str(quo)
        temp.insert(0,quo)
        d = ''.join(temp)
    print("你输入的数转为二进制是：%s" % (d))
c = int(input("请输入一个十进制数："))
Dec2Bin(c)
