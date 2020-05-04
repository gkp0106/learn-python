import math

a = float(input("请输入三角形第一条边的长度："))
b = float(input("请输入三角形第二条边的长度："))
c = float(input("请输入三角形第三条边的长度："))  # 输入三角形边长
if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2  # 周长的二分之一
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("此三角形的面积为：", s)
else:
    print("无法构成三角形")
