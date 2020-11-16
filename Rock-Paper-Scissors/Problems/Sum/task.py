f = open("sums.txt")
print(*[sum(int(y) for y in x.split()) for x in f.readlines()], sep="\n")
f.close()
