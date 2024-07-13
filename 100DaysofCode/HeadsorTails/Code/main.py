import random


def correct_input(prompt, choices):
    while True:
        user_input = input(prompt).lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid Choices, please try again. ")


def answer():
    zero_or_one = random.randint(0, 1)
    if zero_or_one == 1:
        return "Heads"
    elif zero_or_one == 0:
        return "Tails"


def heads_or_tails():
    user = correct_input("Let's play a game, heads or tails? \n", ['heads', 'tails'])
    game_answer = answer().lower()
    if user == "TAILS".lower() and game_answer == "TAILS".lower():
        print(f"It was {game_answer}, You WON!")
    elif user == "HEADS".lower() and game_answer == "HEADS".lower():
        print(f"It was {game_answer}, You WON!")
    else:
        print(f"Incorrect, it was {game_answer}")
    retry()


def retry():
    while True:
        user = correct_input("Do You want to try again? \n", ['yes', 'no'])
        if user == 'Yes'.lower():
            heads_or_tails()
        elif user == 'No'.lower():
            print("Thanks for playing!")
        break


heads_or_tails()
