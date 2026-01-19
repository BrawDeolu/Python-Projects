print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# How much they need to pay based on their size choice.
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Wrong input! Check your input.")

# How much to add to their bill based on their pepperoni choice.
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
else:
    bill += 0

# Final amount based on whether if they want extra cheese.
if extra_cheese == "Y":
    bill += 1
else:
    bill += 0

print(f"Your final bill is: ${bill}")
