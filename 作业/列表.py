lst = [3, 5, 6, 0, -2, -8, 9]
lst1 = []
lst2 = []
lst1 = [x for x in lst if x > 0]
lst2 = [x for x in lst if x < 0]


def avg(*args):
    return sum(args) / len(args)


print("列表1为", lst1, "，平均数为", avg(*lst1))
print("列表2为", lst2, "，平均数为", avg(*lst2))


def product(*args):
    j = 1
    if len(args) == 0:
        raise TypeError
    for i in args:
         j *= i
    return j
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')