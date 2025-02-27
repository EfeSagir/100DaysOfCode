print("Welcome to the rollercoaster")
height = int(input("what is your height in cm?: \n"))
bill = 12
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?: \n"))
    if age <= 12:
        bill = 5
        print("Please pay $5.")
        bill = 7
    elif age <= 18:
        print("Please pay 7$.")
    else:
        bill = 12
        print("Please pay 12$.")

    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
    if wants_photo == "y":
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")


number_to_check = int(input("What is the number you want to check?"))

if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")

print("Welcome to the Python Pizza Deliveries!")
size = input("What size pizza do you want? S,M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

price = 0

if size == "S":
    price = 15
    if pepperoni == "Y":
        price += 2
    if pepperoni == "N":
        price = price
elif size == "M":
    price = 20
    if pepperoni == "Y":
        price += 3
    if pepperoni == "N":
        price = price
elif size == "L":
    price = 25
    if pepperoni == "Y":
        price += 3
    if pepperoni == "N":
        price = price

if extra_cheese == "Y":
    price += 1
else:
    price = price

print(f"Your price is: {price}")


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
        if choice3 == "red":
            print("It's a room full of a fire. Game Over.")
        elif choice3 == "yellow":
            print("You find the treasure. You win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You have been attacked by an angry trout. Game Over. ")
else:
    print("You fell in to a hole. Game Over.")