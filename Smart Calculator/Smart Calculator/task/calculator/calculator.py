def assign_var(s):
    a = s.split("=")
    left = a[0].strip()
    if not is_valid_id(left):
        print("Invalid identifier")
        return
    if len(a) == 2:
        right = a[1].strip()
        if is_valid_dgt(right):
            vars[left] = int(right)
        elif right in vars:
            vars[left] = right
        elif is_valid_id(right):
            print("Unknown variable")
        else:
            print("Invalid assignment")
    elif len(a) > 2:
        print("Invalid assignment")
    elif left in vars:
        print(vars[left])
    else:
        print("Unknown variable")


def is_valid_id(s):
    if len(s) > 0 and all(x.isalpha() for x in s):
        return True
    else:
        return False


def is_valid_dgt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def get_value(n):
    if n in vars:
        return get_value(vars[n])
    else:
        return int(n)


def get_postfix(s):
    postfix_stack = []
    temp_stack = []
    while "++" in s:
        s = s.replace("++", "+")
    s = s.replace("(", " ( ").replace(")", " ) ").replace("*", " * ").replace("/", " / ").replace("+", " + ")
    for n in s.split():
        if is_valid_dgt(n):
            postfix_stack.append(int(n))
        elif is_valid_id(n):
            postfix_stack.append(n)
        elif n == "(":
            temp_stack.append(n)
        elif n == "*" or n == "/":
            temp_stack.append(n)
        elif n == ")":
            if len(temp_stack) == 0 or "(" not in temp_stack:
                return -1
            while "(" != temp_stack[-1]:
                postfix_stack.append(temp_stack.pop())
            else:
                temp_stack.pop()
        elif n.count('-') + n.count('+') == len(n) and len(n) > 0:
            if n.count('-') % 2 != 0:
                op = "-"
            else:
                op = "+"
            while len(temp_stack) > 0 and temp_stack[-1] != "(":
                postfix_stack.append(temp_stack.pop())
            temp_stack.append(op)
        else:
            return -1
    if "(" in temp_stack or ")" in temp_stack:
        return -1
    while temp_stack:
        postfix_stack.append(temp_stack.pop())
    return postfix_stack


def calc(s):
    p = get_postfix(s)
    if p == -1:
        print("Invalid expression")
        return
    temp_stack = []
    while p:
        a = p[0]
        p = p[1:]
        if is_valid_dgt(a):
            temp_stack.append(int(a))
        elif is_valid_id(a):
            if a in vars:
                temp_stack.append(vars[a])
            else:
                print("Unknown variable")
                return
        else:
            temp_stack.append(expression(temp_stack.pop(), temp_stack.pop(), a))
    print(temp_stack[-1])


def expression(b, a, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return int(a / b)


def get_help():
    print("The program calculates the sum and subtraction of numbers")


i = input()
vars = {}
while i != "/exit":
    if i.startswith("/"):
        if i == "/help":
            get_help()
        else:
            print("Unknown command")
    elif "=" in i:
        assign_var(i)
    elif len(i) > 0:
        try:
            calc(i)
        except ValueError:
            print("Unknown variable")
    i = input()
print("Bye!")