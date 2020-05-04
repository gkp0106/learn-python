number = 6 + 50
S = 0
if number % 2 != 0:
    number += 1
for i in range(1, number, 2):
    S += 1 / i
print(S)
