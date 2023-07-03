print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like tp give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = bill * (1 + (tip / 100))
total_bill = bill_with_tip / people
final_amount = ("{:.2f}".format(total_bill))
print(f"Each person should pay ${final_amount}")
