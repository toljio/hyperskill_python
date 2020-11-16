def tallest_people(**kwargs):
    tallest = max(kwargs.values())
    for i in sorted(x for x in kwargs.keys() if kwargs[x] == tallest):
        print(i, kwargs[i], sep=" : ")
