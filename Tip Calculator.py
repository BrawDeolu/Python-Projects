# Greeting
print("Welcome to the tip calculator built with love by Moses")

# Facts
bill = float(input("What was your total bill? $"))
tip_percentage = int(input("How much tip would you like to give? This is already in percentage, please do not add any percentage sign: 10, 12 or 15 "))
how_many_people_splitting = int(input("How many people are splitting this bill? "))

# Calculations
tip_in_number = (tip_percentage / 100) * bill
bill_plus_tip = bill + tip_in_number

amount_per_person = bill_plus_tip / how_many_people_splitting
final_amount = round(amount_per_person, 2)

# Response
print(f"Each person should pay ${final_amount}")