from art import logo
import random

EASY_ATTEMPTS_TURN = 10
HARD_ATTEMPTS_TURN = 5

def compare_guess_to_answer(user_guess, random_answer, turns):
    if user_guess == random_answer:
        print(f"You got it! The answer was {random_answer}")
    elif random_answer > user_guess:
        print("Too high.")
        return turns - 1
    else:
        print("Too low")
        return turns - 1

def set_attempts():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_ATTEMPTS_TURN
    else:
        return HARD_ATTEMPTS_TURN

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    turns = set_attempts()

    random_number = random.randint(1, 100)
    guess_number = 0

    while guess_number != random_number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess_number = int(input("Make a guess: "))
        turns = compare_guess_to_answer(guess_number , random_number , turns)

        if turns == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            return
        else:
            print("Guess again.")

play_game()