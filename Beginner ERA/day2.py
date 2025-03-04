print("length"[-3])

print("23"+" "+"46")

print(23+46)

print(float(3.14159))

print(bool(False))

a = "Hi"

print(len(a))

print(type(a))

print(type(14))

print(type(False))

print(type(1.4))

print(int("14") + int("35")) #checking data types, converting,

print("Number of the letters in your name : "+ str(len(input("What's your name?\n"))))

print("My age is: "+ str(18))

print(type(int(6/2))) #mathematical operators
print(type(6/2))

print(2**3) # this just shows that a**b means b going to power of a

print(14//3) # just gives the int of the result

number = 2

print(round(2,1))

score = 14

score += 34

print("Your score is: "+ str(score))

print(f"Your score is: {score}")

# input always returns string value

print("Welcome to the tip calculator!")
bill = print(type(input("What is the total bill? $")))
tip = input("What percentage tip would you like to give? 10, 12 ,15")
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(total_bill,2)
print(f"Each person should pay: ${final_amount}")