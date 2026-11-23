print("Welcome to the tip calculator!")
bill_total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people_qty = int(input("How many people to split the bill? "))
total_per_person = (bill_total * (1 + (tip/100))) / people_qty
print(f"Each person shoud pay: {round(total_per_person,2)}")
