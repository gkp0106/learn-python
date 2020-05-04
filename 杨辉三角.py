def triangles():
    l = [1]
    while True:
        yield l
        l=[1]+[l[x]+l[x+1] for x in range (len(l)-1)]+[1]
        