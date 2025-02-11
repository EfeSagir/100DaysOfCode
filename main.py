import random
import math
import itertools
from tkinter.messagebox import YESNO

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
#
# DAY 7 ----------------------------------------------------------------------------------------------------------------
# word_list = ["bank"]
# random.shuffle(word_list)
# chosen_word = word_list[0]
# incorrect_count = 0
# correct_count = 0
#
# for checking in itertools.count():
#     guess = input("Enter a letter as your guess: ")
#     if guess in chosen_word:
#         print(f"Correct! The letter {guess} is in the word.")
#         correct_count += 1
#         if correct_count == len(chosen_word):
#             print(f"Congratulations! You've guessed the word: {chosen_word}")
#             break
#         else:
#             continue
#     else:
#         print(f"Wrong! The letter {guess} is not in the word.")
#         incorrect_count += 1
#
#         if incorrect_count == 6:
#             print("Game Over, You Lose!")
#             break
# DAY 8 ----------------------------------------------------------------------------------------------------------------
#
# def greet():
#     print("Hello")
#     print("How are you?")
#     print("It's been a long time since I saw you, how are you?")
#
# greet()
#
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How are you {name}?")
#     print(f"It's been a long time since I saw you, how are you {name}?")
#
# greet_with_name("Angela")
# # name is our parameter and Angela is your argument
#
# def life_in_weeks(age):
#     weeks_left = 52 * (90 - age)
#     print(f"You have {weeks_left} weeks left.")
#
# life_in_weeks(18)
#
# def greet_with(name,location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")
#
# greet_with("Serdar","Istanbul")
# greet_with(name = "Serdar",location = "Istanbul")
#
# true_letter_count = 0
# love_letter_count = 0
# T_letter_count = 0
# R_letter_count = 0
# U_letter_count = 0
# true_E_letter_count = 0
# L_letter_count = 0
# O_letter_count = 0
# V_letter_count = 0
# E_letter_count = 0
# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# for true_letters in name1:
#     if(true_letters == "T"):
#         true_letter_count += 1
#         T_letter_count += 1
#     elif(true_letters =="R"):
#         true_letter_count += 1
#         R_letter_count += 1
#     elif (true_letters == "U"):
#         true_letter_count += 1
#         U_letter_count += 1
#     elif (true_letters == "E"):
#         true_letter_count += 1
#         true_E_letter_count += 1
#     elif (true_letters == "t"):
#         true_letter_count += 1
#         T_letter_count += 1
#     elif (true_letters == "r"):
#         true_letter_count += 1
#         R_letter_count += 1
#     elif (true_letters == "u"):
#         true_letter_count += 1
#         U_letter_count += 1
#     elif (true_letters == "e"):
#         true_letter_count += 1
#         true_E_letter_count += 1
#     else:
#         continue
#     print(T_letter_count)
#     print(R_letter_count)
#     print(U_letter_count)
#     print(E_letter_count)
#     print(true_letter_count)
#
# for love_letters in name2:
#     if(love_letters == "L"):
#         love_letter_count += 1
#         L_letter_count += 1
#     elif(love_letters == "O"):
#         love_letter_count += 1
#         O_letter_count += 1
#     elif (love_letters == "V"):
#         love_letter_count += 1
#         V_letter_count += 1
#     elif (love_letters == "E"):
#         love_letter_count += 1
#         love_E_letter_count += 1
#     elif (love_letters == "l"):
#         love_letter_count += 1
#         L_letter_count += 1
#     elif (love_letters == "o"):
#         love_letter_count += 1
#         O_letter_count += 1
#     elif (love_letters == "v"):
#         love_letter_count += 1
#         V_letter_count += 1
#     elif (love_letters == "e"):
#         love_letter_count += 1
#         love_E_letter_count += 1
#     else:
#         continue
#     print(L_letter_count)
#     print(O_letter_count)
#     print(V_letter_count)
#     print(E_letter_count)
#     print(love_letter_count)
#
#
# def calculate_love_score(name1, name2):
#     combined_name = name1 + name2
#
#     true_count = 0
#     love_count = 0
#     t_count = 0
#     r_count = 0
#     u_count = 0
#     e_count = 0
#     l_count = 0
#     o_count = 0
#     v_count = 0
#
#     for letter in combined_name.lower():
#         if letter == "t" or letter == "r" or letter == "u" or letter == "e":
#             true_count += 1
#             if letter == "t":
#                 t_count += 1
#             elif letter == "r":
#                 r_count += 1
#             elif letter == "u":
#                 u_count += 1
#             elif letter == "e":
#                 e_count += 1
#
#     for letter in combined_name.lower():
#         if letter == "l" or letter == "o" or letter == "v" or letter == "e":
#             love_count += 1
#             if letter == "l":
#                 l_count += 1
#             elif letter == "o":
#                 o_count += 1
#             elif letter == "v":
#                 v_count += 1
#             elif letter == "e":
#                 e_count += 1
#
#     print(f"T occurs {t_count} times")
#     print(f"R occurs {r_count} times")
#     print(f"U occurs {u_count} times")
#     print(f"E occurs {e_count} times")
#     print(f"L occurs {l_count} times")
#     print(f"O occurs {o_count} times")
#     print(f"V occurs {v_count} times")
#
#     love_score = str(true_count) + str(love_count)
#     print(f"Love Score: {love_score}")
#
# fruits = ["apple","peach","pear"]
# numero_uno = fruits.index("peach")
# print(numero_uno)
#
# cars = [911,1.6]
# numero_uno = cars.index(1.6)
# print(numero_uno)
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
# direction = input("Do you want to encrypt or decrypt? To encrypt write encode and to decrypt write decode.\n").lower()
# text = input("Type the text you want to use\n").lower()
# shift_amount = int(input("Type the amount of shift you want\n"))
# def encrypt(text, shift_amount):
#     cipher_text = []
#
#     for letter in text:
#         if (letter not in alphabet):
#             cipher_text += letter
#         indexing_number = alphabet.index(letter) + shift_amount
#         if (indexing_number>=26):
#             indexing_number %= len(alphabet)
#         cipher_text.append(alphabet[indexing_number])
#
#     print(f"Your cipher text is:{cipher_text}")
#
#
# def decrypt(text, shift_amount):
#     cipher_text = []
#
#     for letter in text:
#         if (letter not in alphabet):
#             cipher_text += letter
#         indexing_number = alphabet.index(letter) - shift_amount
#         if (indexing_number >= 26):
#             indexing_number %= len(alphabet)
#         cipher_text.append(alphabet[indexing_number])
#
#     print(f"Your cipher text is:{cipher_text}")
#
#
# def ceasar(text,shift_amount,direction):
#     if(direction == "decode"):
#         decrypt(text,shift_amount)
#
#     elif(direction== "encode"):
#         encode(text,shift_amount)
#
# ceasar(text,shift_amount,direction)
#
# yes_or_no = input("Would you like to change your choice of direction? Type yes or no.?\n").lower()
# if(yes_or_no == "yes"):
#     ceasar(text,shift_amount,direction="encode")
# else:
#     print("Okay bro.")

# DAY 9 ----------------------------------------------------------------------------------------------------------------
#
# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
#
# student_grades = {}
# for key in student_scores:
#     score = student_scores[key]
#     if score >= 91:
#         student_grades[key] = "Outstanding"
#     elif score >= 81:
#         student_grades[key] = "Exceeds Expectations"
#     elif score >= 71:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"
#
# print(student_grades)
#
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin"
# }
#
# print(capitals.get("France"))
# capitals.update({"Turkey": "Ankara"})
# print(capitals)
# capitals.pop("Germany")
# capitals.popitem()
# capitals.clear
# keys = capitals.keys()
# print(keys)
# values = capitals.values()
# print(values)
# items = capitals.items()
# print(items)
#
# for key,value in items:
#     print(f"{key} : {value}")
#
# travel_log = {
#     "France": ["Paris", "Lille", "Dij"],
#     "Germany": ["Stuttgart", "Berlin"]
# }
#
# # print(travel_log["France"][1])
#
# nested_list = ["A","B",["C","D"]]
# # print(nested_list[2][1])
#
# travel_log = {
#     "France": {
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "num_times_visited": 12
#     },
#     "Germany": {
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "num_times_visited": 5
#     }
# }
#
# print(travel_log["Germany"]["cities_visited"][2])
#
# operator = input("pls enter operator")
#
# if isinstance(operator, str):
#     print(operator)
#
# Dictionary = {"Key" : "Value"}
#
# programming_dictionary = {"Bug" : "An error in a program that prevents the program from running as expected.",
#                           "Function" : "A piece of code that you can easily call over and over again.",
#                           "Loop" : "The action of doing something of doing over and over again.",
#                           123 : "It is a combination of the first 3 positive numbers"}
#
# print(programming_dictionary["Bug"])
# print(programming_dictionary["Function"])
# print(programming_dictionary["Loop"])
# print(programming_dictionary[123])
# programming_dictionary["Continue"] = "It is a control flow statament for loops to whether you want to skip execution of a specific part in your code."
# print(programming_dictionary["Continue"])
#
# empty_dictionary = {}
# print(empty_dictionary)
#
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary)
#
# # nesting is adding a item into a dictionary
#
# Dictionary = {"Key" : "Value 1",
#               "Key 2" : "Value 2"}
#
# capitals = {"Germany" : "Berlin",
#             "France" : "Paris",
#             "Turkey" : "Ankara"} 	#Lists can be indexed directly (e.g., nested_list[2][0]), while Dictionaries require keys to access values (e.g., capitals["Germany"]).
#
#
# print(capitals["France"][1])
#
# travel_log = {
#     "France": {
#         "num_times_visited": 9,
#         "cities_visited": ["Paris", "Lille", "Dijon"]
#     },
#     "Germany": {
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5
#     }
# }
#
# print(travel_log["Germany"]["cities_visited"][2])
#
# name = input("Please enter your name:\n")
# bid = input("Please enter your bid:\n")
#
# bidding_dictionary = {}
# bidding_dictionary[name] = bid
#
# yes_or_no = input("If you want to enter another input write Y if you don't write N.")
# while True:
#     if (yes_or_no == "Y"):
#         print("\n" * 100)
#         name = input("Please enter your name:\n")
#         bid = input("Please enter your bid:\n")
#         bidding_dictionary[name] = bid
#         yes_or_no = input("If you want to enter another input write Y if you don't write N.")
#
#     elif(yes_or_no == "N"):
#         max_bidding = max(bidding_dictionary.values())
#         print(f"The highest bid is {bidding_dictionary[max_bidding]} by {max_bidding}")
#         break
# DAY 10 ----------------------------------------------------------------------------------------------------------------
# import utilities
#
# stack = []
# turn_start = False
#
# while True:
#
#     if (stack == []):
#         turn_start = False
#         first_input_from_user = float(input())
#         stack.append(first_input_from_user)
#         operator = input()
#         if isinstance(operator, float):
#             stack.append(stack[-1] + "operator")
#
#         if(operator == "="):
#             print(stack[-1])
#
#         second_input_from_user = float(input())
#
#         match operator:
#             case "+":
#                  stack.append(utilities.summation(stack[-1],second_input_from_user))
#             case "-":
#                   stack.append(utilities.substraction(stack[-1],second_input_from_user))
#             case "*":
#                   stack.append(utilities.multiplication(stack[-1],second_input_from_user))
#             case "/":
#                 if (second_input_from_user != 0):
#                     stack.append(utilities.division(stack[-1],second_input_from_user))
#                 else:
#                     print("Denominator Can't Be 0!")
#                     third_input_from_user = float(input())
#                     if (third_input_from_user != 0):
#                         stack.append(utilities.division(stack[-1],third_input_from_user))
#
#     user_input = input()
#
#     if (user_input not in ("+","-","*","/","=")):
#         stack.append(float(user_input))
#         turn_start = False
#         continue
#
#     match user_input:
#         case "+":
#             if (turn_start):
#                 continue
#             c = float(input())
#             stack.append(utilities.summation(stack[-1], c))
#         case "-":
#             if (turn_start):
#                 continue
#             d = float(input())
#             stack.append(utilities.substraction(stack[-1], d))
#         case "*":
#             if (turn_start):
#                 continue
#             e = float(input())
#             stack.append(utilities.multiplication(stack[-1], e))
#         case "/":
#             if (turn_start):
#                 continue
#             f = float(input())
#             if (f != 0):
#                 stack.append(utilities.division(stack[-1], f))
#             else:
#                 print("Denominator Can't Be 0!")
#                 fourth_input_from_user = float(input())
#                 if (fourth_input_from_user != 0):
#                     stack.append(utilities.division(stack[-1],fourth_input_from_user))
#
#         case "=":
#             if (turn_start == True):
#                 continue
#             print(stack[-1])
#             turn_start = False
# DAY 11 ----------------------------------------------------------------------------------------------------------------
