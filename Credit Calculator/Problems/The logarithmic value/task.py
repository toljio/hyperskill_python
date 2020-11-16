import math
a = int(input())
b = int(input())
if b < 2:
    n = math.log(a)
else:
    n = math.log(a, b)
print(round(n, 2))
