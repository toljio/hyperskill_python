s = [int(x) for x in input()]
print([(s[x] + s[x + 1]) / 2 for x in range(len(s) - 1)])
