from data import MENU, resources

turn_off = False
profit = 0.0

def check_resources(selected_order):
    """ check ingredients for each order."""
    order_ingredients = MENU[selected_order]["ingredients"]
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False

def report_ingredients(resources_ingredients, money):
    print(f"Water: {resources_ingredients["water"]}ml")
    print(f"Milk: {resources_ingredients["milk"]}ml")
    print(f"Coffee: {resources_ingredients["coffee"]}g")
    print(f"Money: ${money}")



# TODO: 1-ask user what's their order and repeat after finishing the process
order = input("What would you like? (espresso/latte/cappuccino): ").lower()

# TODO: 2- type off on order input to turn off the machine
if order == "off":
    turn_off = True

# TODO: 3- type report to print all resources and mony
elif order == "report":
    report_ingredients(resources, profit)

# TODO: 4- check resources after define the order, if there is enough resources make the order, else 
# print “Sorry there is not enough water.”
else:
    check_resources(order)
        





# TODO: 5- prompt user to insert coins, a input for each coin and calculate all received mony.

# TODO: 6- compare received money and order cost, if user payed less print: “Sorry that's not enough money. Money refunded.”
# else add money to profit, and if user payed more money, offer change : “Here is $2.45 dollars in change.”, the change rounded to
# 2 decimal.

# TODO: 7- if everything done well, the integrated should deducted from resources


# TODO: 8- if the order was done, print: “Here is your latte. Enjoy!”