a = str(input("请输入一个排列："))
b = []
for i in a:
    i= int(i)
    b.append(i)
c = len(a)
tao = 0
for d in range(c):
    for e in range(d):
        if b[e] > b[d]:
            tao += 1
print("此排列的逆序数为：",tao)