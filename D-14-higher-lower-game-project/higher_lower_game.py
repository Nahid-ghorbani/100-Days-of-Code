from game_data import data
from random import choice
from art import logo, vs
    
def format_data(account): 
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}."

def check_answer(user_guess, account_a_followers, account_b_followers):
    if account_a_followers > account_b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


print(logo)
game_over = False
scores = 0
account_b = choice(data)

while not game_over:
    account_a = account_b
    account_b = choice(data)
    if account_a == account_b :
        account_b = choice(data)

    print(f"Compare A: {format_data(account_a)}" )
    print(vs)
    print(f"Against B: {format_data(account_b)}" )

    account_a_followers_count = account_a["follower_count"]
    account_b_followers_count = account_b["follower_count"]

    scores = 0

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    state = check_answer(guess, account_a_followers_count, account_b_followers_count)

    print("\n" * 20)
    print(logo)

    if state:
        scores += 1
        print(f"You're right! Current score: {scores}.")
    else:
        print(f"Sorry, that's wrong. Final score: {scores}")
        game_over = True
