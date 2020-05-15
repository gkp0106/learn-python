x=int(input("输入层数："))
c=2*x-1
for i in range(1,x+1):
    y=2*i-1
    m="*"*y
    print('{0:^{1}}'.format(m,c))