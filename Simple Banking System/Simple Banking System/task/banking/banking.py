import random
import sqlite3
from sqlite3 import Error


class Bankomat:
    dbfilename = "card.s3db"
    current_card = 0
    terminated = False
    conn = None

    def __init__(self):
        self.create_db_connection()
        self.create_card_table()

    def create_db_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.dbfilename)
        except Error as e:
            print(e)
        self.conn = conn

    def create_card_table(self):
        sql_create_card_table = """ CREATE TABLE IF NOT EXISTS card (
                                            id INTEGER,
                                            number TEXT,
                                            pin TEXT,
                                            balance INTEGER DEFAULT 0
                                        ); """
        try:
            c = self.conn.cursor()
            c.execute(sql_create_card_table)
        except Error as e:
            print(e)

    def main_menu(self):
        if self.current_card:
            self.internal_menu()
            return
        choices = {
            "0": "Exit",
            "1": "Create an account",
            "2": "Log into account",
        }
        for k, v in choices.items():
            print(f'{k}. {v}')
        i = input()
        if i == "0":
            self.terminated = True
        elif i == "1":
            self.create_account()
        elif i == "2":
            self.login_account()

    def create_account(self):
        Card(self.conn)

    def login_account(self):
        n = input("Enter your card number:")
        p = input("Enter your PIN:")
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM card WHERE number=? AND pin=?", (n, p,))
        card = cur.fetchone()
        if card:
            self.current_card = card
            print("You have successfully logged in!")
            return
        print("Wrong card number or PIN!")

    def logout_account(self):
        self.current_card = 0

    def internal_menu(self):
        choices = {
            0: "Exit",
            1: "Balance",
            2: "Log out",
        }
        for k, v in choices.items():
            print(f'{k}. {v}')
        i = input()
        if i == "2":
            self.logout_account()
        elif i == "1":
            print(self.current_card.balance())
        elif i == "0":
            self.terminated = True

    def start(self):
        while not self.terminated:
            self.main_menu()


class Card:
    number = 0
    pin = 0

    def __init__(self, conn):
        random.seed()
        self.generate_pin()
        self.generate_number()
        print("Your card has been created")
        sql = ''' INSERT INTO card(number,pin)
                  VALUES(?,?) '''
        cur = conn.cursor()
        cur.execute(sql, (self.number, self.pin,))
        conn.commit()

        print(self)

    def generate_pin(self):
        self.pin = str(random.randrange(10000)).zfill(4)

    def generate_number(self):
        s = "400000" + "".join(str(random.randrange(10)) for _ in range(9)) + "0"
        digits = list(map(int, s))
        odd_sum = sum(digits[-1::-2])
        even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
        checksum = (10 - (odd_sum + even_sum) % 10) % 10
        self.number = s[:-1] + str(checksum)

    def __str__(self):
        return "Your card has number\n" + self.number + "\nYour card has PIN\n" + self.pin

    def check(self, pin, number):
        return pin == self.pin and number == self.number

    def balance(self):
        return 0


Bankomat().start()
