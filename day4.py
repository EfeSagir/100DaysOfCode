import random

print(random.random()*10)
print(random.uniform(1,31))

HeadsOrTails = random.randint(0,1)
if HeadsOrTails == 0:
    print("Heads")
else:
    print("Tails")

item1 = "a"
item2 = "b"

fruits = [item1, item2]

print(fruits)

states_of_america = ["Delaware", "Pennysylvania", "New Jersey", "Georgia", "Connecticut"]
print(states_of_america[-1])

states_of_america.append(2)
print(states_of_america[-1])

states_of_america.append("Angelaland")
print(states_of_america[-1])

states_of_america.extend(["Angelaland","Jack Bauer Land"])
print(states_of_america[-1])



friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))

randomNumber = random.randint(1,5)
print(friends[randomNumber])

print(len(states_of_america))

print(states_of_america[randomNumber -1])

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", " Potatoes"]

dirty_dozen = [fruits,vegetables]
print(dirty_dozen)

print(dirty_dozen[1][1]) # 1.listenin icindeki 1.liste yani 1 > vegetables o da 1 > kale gibi

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer_choice = random.randint(0,2)
print(f"Computer chose: {computer_choice}")

if user_input == 0:
    print('rockimage')
elif user_input ==1:
    print('paperimage')
elif user_input == 2:
    print('scissorsimage')

if computer_choice == 0:
    print('rockimage')
elif computer_choice ==1:
    print('paperimage')
elif computer_choice == 2:
    print('scissorsimage')

if user_input == computer_choice:
    print("Draw")
elif user_input == 0 and computer_choice == 2:
    print("User win!")
elif user_input == 1 and computer_choice == 0:
    print("User win!")
elif user_input == 2 and computer_choice == 1:
    print("User win!")
else:
    print("You lose!")