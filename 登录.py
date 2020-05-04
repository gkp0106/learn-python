dict_users = {'Mike': '123', 'Peter': 'ababab', 'Marry': '8091'}
name = input("请输入你的用户名：")
pwd = input("请输入你的密码：")
if name in dict_users and pwd == dict_users[name]:
    print("登录成功")
if name not in dict_users:
    print("用户名错误")
if name in dict_users and pwd != dict_users[name]:
    print("密码错误")
