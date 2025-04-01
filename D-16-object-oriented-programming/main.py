from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu_items = menu.get_items()
turn_off = False

while not turn_off:
    choice = input(f"What would you like? {menu_items}: ").lower()

    if choice == "off":
        turn_off = True
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink_object = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink_object):
            if money_machine.make_payment(drink_object.cost):
                coffee_maker.make_coffee(drink_object)
            