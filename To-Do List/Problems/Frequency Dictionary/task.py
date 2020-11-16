from collections import Counter
words = input().lower().split()
for k, v in Counter(words).items():
    print(k, v)
