import random

# print("Hello world!")
#
# print("+Hello Efe How Are You? \n-I am fine hbu?")
#
# print("Hello" + " " + "Angela")
#
# print("Hi" + " " + input("What is your name?\n") + "!")
#
# name = input("What is your name?\n")
#
# print("Hi" + " " + name + "!")
#
# name = "Angel"
#
# print("Hi" + " " +name)
#
# username = (input("What is your username?\n"))
#
# length = len(username)
#
# print(length)
#
# print("Welcome to the Band Name Generator")
#
# city = input("Which city did you grow up in?\n")
# pet = input("What is the name of a pet?\n")
#
# print("Your band name could be :" + city + " " + pet)
#
# print("length"[-3])
#
# print("31"+" "+"69")
#
# print(31+69)
#
# print(float(3.14159))
#
# print(bool(False))
#
# a = "Hi"
#
# print(len(a))
#
# print(type(a))
#
# print(type(31))
#
# print(type(False))
#
# print(type(3.1))
#
# print(int("31") + int("69")) #checking data types, converting,
#
# print("Number of the letters in your name : "+ str(len(input("What's your name?\n"))))
#
# print("My age is: "+ str(18))
#
# print(type(int(6/2))) #mathematical operators
# print(type(6/2))
#
# print(2**3) # this just shows that a**b means b going to power of a
#
# print(14//3) # just gives the int of the result
#
# OtuzBir = 3.1
#
# print(round(OtuzBir,1))
#
# score = 31
#
# score += 31
#
# print("Your score is: "+ str(score))
#
# print(f"Your score is: {score}")
#
# #input always returns string value
#
#
# print("Welcome to the tip calculator!")
# bill = print(type(input("What is the total bill? $")))
# tip = input("What percentage tip would you like to give? 10, 12 ,15")
# people = int(input("How many people to split the bill?"))
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_with_tip,2)
# print(f"Each person should pay: ${final_amount}")
#
# print("Welcome to the rollercoaster")
# height = int(input("what is your height in cm?: \n"))
# bill = 12
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age?: \n"))
#     if age <= 12:
#         bill = 5
#         print("Please pay $5.")
#         bill = 7
#     elif age <= 18:
#         print("Please pay 7$.")
#     else:
#         bill = 12
#         print("Please pay 12$.")
#
#     wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
#     if wants_photo == "y":
#         bill += 3
#
#     print(f"Your final bill is {bill}")
#
# else:
#     print("Sorry you have to grow taller before you can ride.")
#
#
# number_to_check = int(input("What is the number you want to check?"))
#
# if number_to_check % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
#
# print("Welcome to the Python Pizza Deliveries!")
# size = input("What size pizza do you want? S,M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
#
# price = 0
#
# if size == "S":
#     price = 15
#     if pepperoni == "Y":
#         price += 2
#     if pepperoni == "N":
#         price = price
# elif size == "M":
#     price = 20
#     if pepperoni == "Y":
#         price += 3
#     if pepperoni == "N":
#         price = price
# elif size == "L":
#     price = 25
#     if pepperoni == "Y":
#         price += 3
#     if pepperoni == "N":
#         price = price
#
# if extra_cheese == "Y":
#     price += 1
# else:
#     price = price
#
# print(f"Your price is: {price}")
#
#
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".\n').lower()
#
# if choice1 == "left":
#     choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
#     if choice2 == "wait":
#         choice3 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
#         if choice3 == "red":
#             print("It's a room full of a fire. Game Over.")
#         elif choice3 == "yellow":
#             print("You find the treasure. You win!")
#         elif choice3 == "blue":
#             print("You enter a room of beasts. Game Over.")
#         else:
#             print("You chose a door that doesn't exist. Game Over.")
#     else:
#         print("You have been attacked by an angry trout. Game Over. ")
# else:
#     print("You fell in to a hole. Game Over.")


# print(random.random()*10)
# print(random.uniform(1,31))
#
# HeadsOrTails = random.randint(0,1)
# if HeadsOrTails == 0:
#     print("Heads")
# else:
#     print("Tails")
#
# item1 = "a"
# item2 = "b"
#
# fruits = [item1, item2]
#
# print(fruits)
#
# states_of_america = ["Delaware", "Pennysylvania", "New Jersey", "Georgia", "Connecticut"]
# print(states_of_america[-1])
#
# states_of_america.append(2)
# print(states_of_america[-1])
#
# states_of_america.append("Angelaland")
# print(states_of_america[-1])
#
# states_of_america.extend(["Angelaland","Jack Bauer Land"])
# print(states_of_america[-1])
#
#
#
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# print(random.choice(friends))
#
# randomNumber = random.randint(1,5)
# print(friends[randomNumber])
#
# print(len(states_of_america))
#
# print(states_of_america[randomNumber -1])
#
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", " Potatoes"]
#
# dirty_dozen = [fruits,vegetables]
# print(dirty_dozen)
#
# print(dirty_dozen[1][1]) # 1.listenin icindeki 1.liste yani 1 > vegetables o da 1 > kale gibi
#
# user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
#
# computer_choice = random.randint(0,2)
# print(f"Computer chose: {computer_choice}")
#
# if user_input == 0:
#     print('rockimage')
# elif user_input ==1:
#     print('paperimage')
# elif user_input == 2:
#     print('scissorsimage')
#
# if computer_choice == 0:
#     print('rockimage')
# elif computer_choice ==1:
#     print('paperimage')
# elif computer_choice == 2:
#     print('scissorsimage')
#
# if user_input == computer_choice:
#     print("Draw")
# elif user_input == 0 and computer_choice == 2:
#     print("User win!")
# elif user_input == 1 and computer_choice == 0:
#     print("User win!")
# elif user_input == 2 and computer_choice == 1:
#     print("User win!")
# else:
#     print("You lose!")

# DAY 5 ----------------------------------------------------------------------------------------------------------------

# fruits = ["Apple", "Peach", "Pear"]
#
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " " + "Pie")
#     print(fruits)
#
# student_scores = [10,50,1000,5000]
#
# total_exam_score = sum(student_scores)
#
# sum = 0
# for score in student_scores:
#     sum += score
#
# print(sum)
#
# print(max(student_scores))
#
# student_result = [13,96,1313,9696]
# max_score = 0
# for score in student_result:
#     if score > max_score:
#         max_score = score
#
# for number in range(30,70,3): # start-stop-step mechanism
#     print(number)
#
# total = 0
# for number in range(0,101,1):
#     total += number # it just skips to the next line when the loop ends.
# print(total)
#
# letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
#            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#
# symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "/", "<", ">", "?"]
#
# lenght_password = int((input("How long do you want your password to be?\n")))
# symbols_password = int(input("How many symbols do you want in your password to be?\n"))
# numbers_password = int(input("How many numbers do you want in your password to be?\n"))
#
# password = []
#
# for length in range(0,lenght_password):
#     random_letter = random.choice(letters)
#     password += random_letter
#
# for number in range(0,numbers_password):
#     random_number = random.choice(numbers)
#     password += random_number
#
# for symbol in range(0,symbols_password):
#     random_symbol = random.choice(symbols)
#     password += random_symbol
#
# random.shuffle(password)
# print((password))

# DAY 6 ----------------------------------------------------------------------------------------------------------------
#
#  def turn_right():
#     turn_left
#     turn_left
#     turn_left
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left
#
# for step in range(6)
#     jump()
#
# number_of_hurdles =6
# while(number_of_hurdles > 0):
#     jump()
#     number_of_hurdles -= 1
#     print(number_of_hurdles)
# while not at_goal():
#     jump()
# def jump():
# turn_left()
# while wall_on_right():
#     move()
# turn_right()
# move()
# turn_right()
# while front_is_clear():
#     move()
# turn_left()
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()
# while front_is_clear():
#     move()
# turn_left()
#
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()

# DAY 7 ----------------------------------------------------------------------------------------------------------------
