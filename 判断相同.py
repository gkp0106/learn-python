# 编写一个函数isdiff(n)，判断参数n的各位数字是否互不相同，若互不相同，则返回1，否则返回0，利用isdiff函数找出100到200之间所有各位数字均不同的整数。#
def isdiff(n):
    if isinstance(n, int):
        if len(set(str(n))) < len(str(n)):
            return 0
        else:
            return 1
    else:
        raise TypeError("输入的参数应为整数")


for i in range(100, 201):
    if isdiff(i):
        print(i)