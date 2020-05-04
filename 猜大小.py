import random
s = random.randint(1, 100)
guess = 0
while guess != s:
    temp = input("请输入你猜的数字：")
    if temp.isdigit():
        guess = int(temp)
        if guess == s:
            print("您猜对了！")
        else:
            if guess < s:
                print("您猜小了！")
            else:
                print("您猜大了！")
            p = input("是否继续？")
            while p != "是" and p != "否":
                p = input("是否继续？(回答是or否)")
            if p == "是":
                continue
            if p == "否":
                break
    else:
        print("输入有误，请输入一个整数：")
print("游戏结束")
