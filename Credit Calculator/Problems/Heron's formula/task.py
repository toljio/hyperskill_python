import math
a, b, c = (int(input()) for _ in range(3))
p = (a + b + c) / 2
print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
