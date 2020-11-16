def print_desk():
    print("---------")
    for i in range(3):
        print("| " + " ".join(c[3 * i:3 * i + 3]) + " |")
    print("---------")


def result():
    win_x = 0
    win_o = 0
    for i in range(3):
        if c[3*i:3*i+3].count("X") == 3:
            win_x += 1
        elif c[3*i:3*i+3].count("O") == 3:
            win_o += 1
        if (c[i] + c[i + 3] + c[i + 6]).count("X") == 3:
            win_x += 1
        elif (c[i] + c[i + 3] + c[i + 6]).count("O") == 3:
            win_o += 1
    if (c[0] + c[4] + c[8]).count("X") == 3:
        win_x += 1
    elif (c[0] + c[4] + c[8]).count("O") == 3:
        win_o += 1
    if (c[2] + c[4] + c[6]).count("X") == 3:
        win_x += 1
    elif (c[2] + c[4] + c[6]).count("O") == 3:
        win_o += 1
    res = ""
    if win_o == 0 and win_x == 0 and c.count("_") == 0:
        res = "Draw"
    elif win_x == 1 and win_o == 0:
        res = "X wins"
    elif win_o == 1 and win_x == 0:
        res = "O wins"
    return res


c = "_________"
print_desk()
new_coord = input("Enter the coordinates: ").split()
while True:
    if not new_coord[0].isnumeric() or not new_coord[1].isnumeric():
        print("You should enter numbers!")
    elif not 1 <= int(new_coord[0]) <= 3 or not 1 <= int(new_coord[1]) <= 3:
        print("Coordinates should be from 1 to 3!")
    elif c[(3 - int(new_coord[1])) * 3 + (int(new_coord[0]) - 1)] != "_":
        print("This cell is occupied! Choose another one!")
    else:
        c_id = (3 - int(new_coord[1])) * 3 + (int(new_coord[0]) - 1)
        new_v = "X" if c.count("X") <= c.count("O") else "O"
        c = c[:c_id] + new_v + c[c_id + 1:]
        print_desk()
        r = result()
        if r:
            print(r)
            break
    new_coord = input("Enter the coordinates: ").split()
