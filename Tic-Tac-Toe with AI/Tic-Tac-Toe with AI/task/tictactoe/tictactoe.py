import sys, random


def print_desk():
    print("---------")
    t = c.replace("_", " ")
    for i in range(3):
        print("| " + " ".join(t[3 * i:3 * i + 3]) + " |")
    print("---------")


def result(c):
    win_x = 0
    win_o = 0
    for i in range(3):
        if c[3*i:3*i+3].count("X") == 3:
            win_x = 1
        elif c[3*i:3*i+3].count("O") == 3:
            win_o = 1
        if (c[i] + c[i + 3] + c[i + 6]).count("X") == 3:
            win_x = 1
        elif (c[i] + c[i + 3] + c[i + 6]).count("O") == 3:
            win_o = 1
    if (c[0] + c[4] + c[8]).count("X") == 3:
        win_x = 1
    elif (c[0] + c[4] + c[8]).count("O") == 3:
        win_o = 1
    if (c[2] + c[4] + c[6]).count("X") == 3:
        win_x = 1
    elif (c[2] + c[4] + c[6]).count("O") == 3:
        win_o = 1
    res = ""
    if win_o == 0 and win_x == 0 and c.count("_") == 0:
        res = "Draw"
    elif win_x == 1 and win_o == 0:
        res = "X wins"
    elif win_o == 1 and win_x == 0:
        res = "O wins"
    # else:
    #     res = "Game not finished"
    return res


def comp_turn(mode, v):
    global c
    print("Making move level", mode)
    if mode == "easy":
        i = c.index("_")
        c = c[:i] + v + c[i + 1:]
        # print_desk()
    elif mode == "medium":
        t = c
        current = 0
        temp_stack = []
        for j in range(c.count("_")):
            current = c.index("_", current)
            temp_stack.append(current)
            c = c[:current] + v + c[current + 1:]
            if result(c) == v + " wins":
                return
            c = t
        u = "X" if v == "O" else "O"
        for j in temp_stack:
            c = c[:j] + u + c[j + 1:]
            if result(c) == u + " wins":
                c = t
                c = c[:j] + v + c[j + 1:]
                return
            c = t
        current = random.choice(temp_stack)
        c = c[:current] + v + c[current + 1:]
    elif mode == "hard":
        if result(c):
            comp_turn("easy", v)
            return
        current = next_turn(c, v, True)
        c = c[:current] + v + c[current + 1:]


def next_turn(desk, v, comp_turn):
    res = result(desk)
    u = "X" if v == "O" else "O"
    if res:
        if res == "Draw":
            return 0
        elif res == v + " wins" and comp_turn or res == u + " wins" and not comp_turn:
            return 10
        else:
            return -10
    h = {}
    ind = 0
    for j in range(desk.count("_")):
        ind = desk.index("_", ind)
        h[ind] = next_turn(desk[:ind] + v + desk[ind + 1:], u, not comp_turn)
    if comp_turn:
        return max(h, key=h.get)
    else:
        return min(h, key=h.get)


def user_turn(v):
    global c
    new_coord = input("Enter the coordinates: ").split()
    if new_coord[0] == "exit":
        sys.exit()
    elif not new_coord[0].isnumeric() or not new_coord[1].isnumeric():
        print("You should enter numbers!")
        user_turn(v)
    elif not 1 <= int(new_coord[0]) <= 3 or not 1 <= int(new_coord[1]) <= 3:
        print("Coordinates should be from 1 to 3!")
        user_turn(v)
    elif c[(3 - int(new_coord[1])) * 3 + (int(new_coord[0]) - 1)] != "_":
        print("This cell is occupied! Choose another one!")
        user_turn(v)
    else:
        c_id = (3 - int(new_coord[1])) * 3 + (int(new_coord[0]) - 1)
        # new_v = "X" if c.count("X") <= c.count("O") else "O"
        c = c[:c_id] + v + c[c_id + 1:]


def play(*args):
    global c
    c = "_________"
    print_desk()
    xo = ["X", "O"]
    n = 0
    while "_" in c:
        turn = args[n % 2]
        if turn == "user":
            user_turn(xo[n % 2])
        else:
            comp_turn(turn, xo[n % 2])
        n += 1
        print_desk()
        print(result(c))
    else:
        print(result(c))


modes = ["easy", "user", "medium", "hard"]
i = input("Input command")
while i != "exit":
    i = i.split()
    if len(i) == 3 and i[0] == "start" and i[1] in modes and i[2] in modes:
        play(i[1], i[2])
    else:
        print("Bad parameters!")
    i = input("Input command")
