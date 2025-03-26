from art import logo

bids_dictionary = {}

calculation_completed = False
while not calculation_completed:
    user_name = input("what is your name?\n")
    bid = int(input("what is your bid?\n$"))
    bids_dictionary[user_name] = bid
    print(bids_dictionary)
    add_new_bid = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if add_new_bid == "no":
        calculation_completed = True
    else:
        print("\n" * 20)


max_bid = 0
winner = ""
for key in bids_dictionary:
    if bids_dictionary[key] > max_bid:
        max_bid = bids_dictionary[key]
        winner = key

print(f"The winner is {winner} with a bid of ${max_bid}")
