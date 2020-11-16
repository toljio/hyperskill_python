from collections import Counter
l = input()
h = Counter(l.split())
print(h.most_common(1)[0][0])
