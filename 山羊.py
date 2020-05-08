import random
times=10000
dict1=dict(a='car',b='sheep',c='sheep')
success=twsucceess=0
for i in range(times-1):
    x = ['a', 'b', 'c']
    choice=random.choice(x)
    if dict1.get(choice)=="car":
        success+=1
    else:
        x.remove('b')
        choice=random.choice(x)
        if dict1.get(choice)=='car':
            twsucceess+=1
print("不修改选择获胜概率为%.2f" % (success/times))
print("修改选择获胜概率为%.2f" % ((twsucceess+success)/times))