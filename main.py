from art import logo, vs
from game_data import data
import random
import os


def format_data(account):
    """format the account data and returns the printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_description}, from {account_country}")


def check_answer(guess, a_followers, b_followers):
    """takes the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# display art
print(logo)
score = 0
countinue_game = True
account_b = random.choice(data)

while countinue_game:
    # generate a random account from the game data.

    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # ask user for a guess
    guess = input("Who has more followers? type 'A' or 'B': ").lower()

    # Check if user is correct
    # get follower count of eac account
    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower, b_follower)
    os.system("cls")
    print(logo)
    # give user feedback on their guess
    if is_correct:
        score += 1
        print(f"you got it right, current score {score}")
    else:
        countinue_game = False
        print(f"bad luck brian, thats wrong your final score is {score}")
