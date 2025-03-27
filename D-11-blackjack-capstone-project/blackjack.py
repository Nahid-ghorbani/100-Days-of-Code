import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    

user_cards = []
computer_cards = []

def select_first_card():
    for i in range(0,2):
        user_cards.append(random.choice(cards))    
    computer_cards.append(random.choice(cards))    

def end_game(user_current_score, computer_current_score):
    print(f"Your final hand: {user_cards}, final score: {user_current_score}")
    print(f"computers final hand: {computer_cards}, final score: {computer_current_score}")

    if user_current_score <= 21 and computer_current_score <= 21:
        if user_current_score < computer_current_score:
            print("You lose!")
        elif user_current_score > computer_current_score:
            print("You win!")
        else:
            print("Its a dowel!")
    elif user_current_score > 21:
        print("You went over. You lose!")
        
    elif computer_current_score > 21:
        print("opponent went over. You win!")
    

def play_game():
    continue_game = True
    select_first_card()

    while continue_game:
        user_current_score = sum(user_cards)
        computer_current_score = sum(computer_cards)            

        print(f"Your cards: {user_cards}, current score: {user_current_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_current_score < 21 and computer_current_score < 21:
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            if get_another_card == "y":
                user_cards.append(random.choice(cards))
            else:
                while computer_current_score < 17 :
                    computer_cards.append(random.choice(cards))
                    computer_current_score = sum(computer_cards)            

        else:
            continue_game = False
            end_game(user_current_score, computer_current_score)

game_start = True
while game_start:
    print(logo)
    start_permission = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start_permission == "y":
        user_cards = []
        computer_cards = []
        print("\n" * 100)
        play_game()
    else:
        game_start = False