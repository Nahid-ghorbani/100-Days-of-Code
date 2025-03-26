from art import logo

bids_dictionary = {}
calculation_completed = False

def find_highest_bidder(bidding_dictionary):
    max_bidder = max(bidding_dictionary)
    print(f"The winner is {max_bidder} with a bid of ${bidding_dictionary[max_bidder]}")

print(logo)

while not calculation_completed:
    user_name = input("what is your name?\n")
    bid = int(input("what is your bid?\n$"))
    bids_dictionary[user_name] = bid
    add_new_bid = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if add_new_bid == "no":
        calculation_completed = True
        find_highest_bidder(bids_dictionary)
    else:
        print("\n" * 20)
