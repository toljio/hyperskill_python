f = open("animals.txt")
w = open("animals_new.txt", "w")
w.write(" ".join(x.strip() for x in f.readlines()))
f.close()
w.close()
