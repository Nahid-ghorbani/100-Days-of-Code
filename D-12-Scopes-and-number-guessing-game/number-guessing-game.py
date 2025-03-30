from art import logo
import random

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    lives = 0

    game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if game_difficulty == "easy":
        lives = 10
    else:
        lives = 5


    game_over = False
    random_number = random.randint(1, 100)

    while not game_over:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess_number = int(input("Make a guess: "))
        lives -= 1

        if guess_number == random_number:
            print(f"You got it! The answer was {random_number}")
            game_over = True

        elif lives == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            game_over = True

        elif guess_number > random_number:
            print("Too high.")
            print("Guess again.")

        else:
            print("Too low")
            print("Guess again.")


play_game()