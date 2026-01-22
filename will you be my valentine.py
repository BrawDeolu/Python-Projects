print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# players make their first step
first_step = (input("Would you like to go left or right? Type 'left' or 'right' ")).lower()

# Logic
if first_step == "left":
    second_step = input("Good choice. You are now at the river bank. Would you like to swim or wait? Type 'swim' or 'wait' ").lower()
    if second_step == "wait":
        final_door = input("Good choice! The boat has arrived, hop on\n...\nYou are now at entrance of the treasure room with 3 doors: Which door would you choose? Red, Blue, or Purple? ").lower()
        if final_door == "purple":
           test_of_fate = input("Would you be my valentine? Type 'Yes' or 'No' ").lower()
           if test_of_fate == "yes":
               print("Thank you!")
           elif test_of_fate == "no":
               print("Ok. Thanks. Bye")
           else:
               print("Game Over!")
        elif final_door == "red":
            print("Make better choices next time")
        elif final_door == "blue":
            print("Really?! Game over, start again.")
        else:
            print("Was that a part of the option? Game Over!")
    else:
        print("You should have seen the crocodile, game over!")
else:
    print("Way too early to loose, game over!")

