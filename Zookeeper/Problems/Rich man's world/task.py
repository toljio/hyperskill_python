start = int(input())
i = 1
while start * 1.071 < 700000:
    start *= 1.071
    i += 1
print(i)
