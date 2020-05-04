def gcb(x, y):
    while y:
        t = x % y
        x = y
        y = t
    return x


print(gcb(6, 3))
