import random
random_number = random.randint(0,100)

end = 0
def if_cold_or_hot_or_got(user_input):
    difference = abs(random_number - user_input)
    if(difference == 0):
        print("Got It!")
        end = 1
    elif(difference <= 3):
        print("Too Hot!")
    elif(difference <= 6):
        print("Hot")
    elif(difference <= 10):
        print("Warm")
    else:
        print("Cold")


guess_count = input("How difficult do you want your game to be? Type easy or hard.").lower()

if(guess_count == "easy"):
    print("You have 10 attempts remaining. Enter natural numbers.")
    for i in range(10):  
        if(end == 1):
            break
        user_input = int(input())
        if_cold_or_hot_or_got(user_input)

        print(f"You have {10 - (i + 1)} attempts left.")
    
elif(guess_count == "hard"):
    print("You have 5 attempts remaining. Enter natural numbers.")
    for i in range(5):  
        if(end == 1):
            break
        user_input = int(input())  
        if_cold_or_hot_or_got(user_input)
        print(f"You have {5 - (i + 1)} attempts left.")
else:
    print("You typed wrong. Write easy or hard.")
    