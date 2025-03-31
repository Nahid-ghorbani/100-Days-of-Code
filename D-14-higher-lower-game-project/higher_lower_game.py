from game_data import data
from random import choice
from art import logo, vs

def compare_followers(a_followers, b_followers):
    if a_followers["follower_count"] > b_followers["follower_count"]:
        return a_followers
    elif b_followers["follower_count"] > a_followers["follower_count"]:
        return b_followers
    else:
        return 

def set_random_accounts():
    accounts = []
    for _ in range(2):
        accounts.append(choice(data))
    return accounts


def play():
    print(logo)
    game_over = False
    scores = 0
    while not game_over:
        random_accounts = set_random_accounts()
        first_account = random_accounts[0]
        second_account = random_accounts[1]
        correct_answer = compare_followers(first_account, second_account)
        print(correct_answer)

        print(f"Compare A: {first_account['name']}, a {first_account['description']}, from {first_account['country']}." )
        print(vs)
        print(f"Against B: {second_account['name']}, a {second_account['description']}, from {second_account['country']}." )

        selected_account = {}
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_guess == "a":
            selected_account = first_account
        else:
            selected_account = second_account


        if correct_answer["name"] == selected_account["name"]:
            scores += 1
            print("\n" * 100)
            print(logo)
            print(f"You're right! Current score: {scores}.")
        else:
            print(f"Sorry, that's wrong. Final score: {scores}")
            game_over = True

play()