from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operation_dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(logo)
quite_app = False
first_number = 0
while not quite_app:
    if first_number == 0:
        first_number = float(input("what's the first number?: "))
    for key in operation_dictionary:
        print(key)
    operation = input("Pick an operation: ")
    second_number = float(input("What's the next number?: "))

    calculated_number = operation_dictionary[operation](first_number, second_number)
    print(f"{first_number} {operation} {second_number} = {calculated_number}")

    continue_calculation = input(f"Type 'y' to continue calculating with {calculated_number}, or type 'n' to start a new calculation: " ).lower()

    if continue_calculation == "y":
        first_number = calculated_number
    elif continue_calculation == "n":
        first_number = 0



