print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

final_tip = bill * (tip / 100)

bill_with_tip = final_tip + bill

bill_per_person = round(bill_with_tip / people, 2)

print(f"The tip is {round(final_tip, 2)} and the bill total is {round(bill_with_tip, 2)}. Each person should pay: ${bill_per_person}")
