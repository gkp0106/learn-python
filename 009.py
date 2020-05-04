i = 3
while i:
    password= input("请输入密码：")
    if password == "gkpnb":
        print("密码正确,进入程序")
        break
    elif "*" in password:
        print('密码中不能有"*"你还有',i,"次机会")
        continue
    else:
        i -= 1
        print('密码错误,你还有',i,'次机会')

