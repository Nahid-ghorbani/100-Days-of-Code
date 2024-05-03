print("Welcome to tip calculator.")

total_bill = float(input("What was the total bill?\n $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
people_number = int(input("How many people to split the bill? \n"))

bill_with_tip = (percentage_tip / 100) * total_bill + total_bill
# second solution : 
# bill_with_tip = total_bill * (1 + percentage_tip / 100)
bill_per_person = round(bill_with_tip / people_number, 2)
# in some rounded numbers, round just return one decimal which is format problem not mathematic, 
# so we can use the format change to be sure always get two decimal:
bill_per_person = "{:.2f}".format(bill_per_person) 

print(f"Each person should pay: ${bill_per_person}")