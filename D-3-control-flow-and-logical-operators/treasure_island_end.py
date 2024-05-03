print('''
  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88         
      ''')

print('Welcome to Treasure Island.\nYour mission is to find the treasure.')

choice_one = input("You are on at a cross road, where do you want to go? \"left\" or \"right\"")
choice_two = input("You have come to a lake. There is an island in the middle of lake. Type \"wait\" for wait for a boat. type \"swim\" to swim across.")
choice_three = input("You find a house in top of island. type \"inside\" to search in house or \"garage\" to check the garage or \"stares\" to check second level.")

if choice_one == "left":
    if choice_two == "wait":
        if choice_three == "inside" or "garage":
            print('ops! you got shot! Game Over!')
        elif choice_three == "stares":
            print('You Got It. What about another round?')
    else:
        print('You fell into a n hole! Game Over!')
else:
    print('You had an accident!Not that Lucky huh? Game Over!')
