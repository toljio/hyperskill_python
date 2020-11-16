import random
username = input("Enter your name: ")
print("Hello, " + username)
f = open("rating.txt", "r")
user_score = 0
for l in f:
    s = l.split()
    if s[0] == username:
        user_score = int(s[1])
        break
f.close()
i = input()
if i:
    choices = i.split(",")
else:
    choices = ("rock", "paper", "scissors")
print("Okay, let's start")
user_choice = input()
while user_choice != "!exit":
    computer_choice = random.choice(choices)
    if user_choice == "!rating":
        print(user_score)
    elif user_choice not in choices:
        print("Invalid input")
    elif computer_choice == user_choice:
        print(f'There is a draw ({computer_choice})')
        user_score += 50
    elif 0 < choices.index(computer_choice) - choices.index(user_choice) <= len(choices) // 2\
            or choices.index(user_choice) - choices.index(computer_choice) > len(choices) // 2:
        print(f'Sorry, but computer chose {computer_choice}')
    else:
        print(f'Well done. Computer chose {computer_choice} and failed')
        user_score += 100
    user_choice = input()
print("Bye!")
