s = [int(x) for x in input()]
print([sum(s[:x + 1]) for x in range(len(s))])
