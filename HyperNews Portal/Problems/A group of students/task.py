def quicksort(arr):
    if len(arr) > 1:
        left, center, right = [], [], []
        t = [arr[0][1], arr[-1][1], arr[len(arr) // 2][1]]
        pivot = sum(t) - max(t) - min(t)
        for v in arr:
            if v[1] < pivot:
                left.append(v)
            elif v[1] > pivot:
                right.append(v)
            elif v[1] == pivot:
                center.append(v)
                for j in range(len(center) - 1):
                    if v[0] < center[j][0]:
                        center = center[:j] + [center[-1]] + center[j:-1]
                        break
        return quicksort(left) + center + quicksort(right)
    return arr

user_lst = []
for _ in range(int(input())):
    i = input().split()
    user_lst.append([i[0], int(i[1])])
user_lst = quicksort(user_lst)
for l in user_lst:
    print(l[0])
