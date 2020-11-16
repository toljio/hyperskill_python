from collections import deque
n = int(input())
d = deque()
for _ in range(n):
    i = input().split()
    if i[0] == "READY":
        d.appendleft(i[1])
    elif i[0] == "EXTRA":
        d.appendleft(d.pop())
    elif i[0] == "PASSED":
        print(d.pop())
