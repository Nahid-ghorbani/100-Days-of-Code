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
    return True

def report_ingredients(resources_ingredients, money):
    print(f"Water: {resources_ingredients["water"]}ml")
    print(f"Milk: {resources_ingredients["milk"]}ml")
    print(f"Coffee: {resources_ingredients["coffee"]}g")
    print(f"Money: ${money}")

def calculate_received_money():
    quarters = int(input("quarters: "))
    dimes = int(input("dimes: "))
    nickles = int(input("nickles: "))
    pennies= int(input("pennies: "))

    received_money = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    return round(received_money, 2)


while not turn_off:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "off":
        turn_off = True

    elif order == "report":
        report_ingredients(resources, profit)

    elif check_resources(order):            
        received_money = calculate_received_money()
        order_cost = MENU[order]["cost"]

        if order_cost > received_money:
            print("Sorry that's not enough money. Money refunded.")
        else:
            profit += order_cost
            if order_cost < received_money:
                change = received_money - order_cost
                change = round(change, 2)
                print(f"Here is ${change} dollars in change.")
            
            for ingredient in MENU[order]["ingredients"]:
                resources[ingredient] -= MENU[order]["ingredients"][ingredient]

            print(f"Here is your {order}. Enjoy!")
