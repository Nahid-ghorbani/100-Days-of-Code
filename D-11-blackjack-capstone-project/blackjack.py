import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """ Take the list of cards and return the score calculated from cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_current_score, computer_current_score):
    if user_current_score == computer_current_score:
        print("Its a draw!")
    elif computer_current_score == 0:
        print("Lose, opponent has a blackJack!")
    elif user_current_score == 0: 
        print("Win with a blackjack!")
    elif user_current_score > 21:
        print("You went over. You lose!")
        
    elif computer_current_score > 21:
        print("opponent went over. You win!")
    elif user_current_score < computer_current_score:
            print("You lose!")
    else:
        print("You win!")

def play_game():
    print(logo)
    user_cards = []
    computer_cards = [] 
    user_score = -1
    computer_score = -1
    continue_game = True

    for _ in range(2):
        user_cards.append(deal_card())    
        computer_cards.append(deal_card())

    while continue_game:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)            

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21 :
            continue_game = False
        else:
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            if get_another_card == "y":
                user_cards.append(deal_card())
            else:
                continue_game = False

    while computer_score != 0 and computer_score < 17 and user_score < 21 :
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"computers final hand: {computer_cards}, final score: {computer_score}")
    compare(user_score , computer_score)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
        print("\n" * 100)
        play_game()