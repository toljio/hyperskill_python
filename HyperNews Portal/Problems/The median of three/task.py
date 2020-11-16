def choose_median(lst, start, middle, end):
    if start >= middle:
        return start
    if lst[start] <= lst[middle] <= lst[end]:
        return middle
    if lst[end] <= lst[middle] <= lst[start]:
        return middle
    if lst[start] <= lst[end] <= lst[middle]:
        return end
    if lst[middle] <= lst[end] <= lst[start]:
        return end
    return start


def partition(lst, pivot, start, end):
    lst[start], lst[pivot] = lst[pivot], lst[start]
    j = start

    for i in range(start + 1, end + 1):
        if lst[i] <= lst[start]:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[start], lst[j] = lst[j], lst[start]
    return j


user_list = [int(x) for x in input().split()]
median = choose_median(user_list, 0, len(user_list) // 2 - 1, len(user_list) - 1)
partition(user_list, median, 0, len(user_list) - 1)
print(median)
print(*user_list)
