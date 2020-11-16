for i in [Drinks, Pastry, Sweets]:
    if issubclass(child, i):
        print(i.__name__)
