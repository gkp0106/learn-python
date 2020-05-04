for a in range(100,1000):
    b = a // 100
    c = a // 10 - b * 10
    d = a - b * 100 - c * 10
    if a == b ** 3 + c ** 3 +d ** 3:
        print(a)
