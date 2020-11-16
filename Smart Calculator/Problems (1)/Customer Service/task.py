n = int(input())
my_queue = []
for _ in range(n):
    i = input().split()
    if len(i) > 1:
        my_queue.append(i[1])
    elif len(my_queue) > 0:
        my_queue = my_queue[1:]
for i in my_queue:
    print(i)
