with open("salary.txt") as r, open("salary_year.txt", "w") as o:
    for l in r:
        o.write(str(12 * int(l)) + "\n")
