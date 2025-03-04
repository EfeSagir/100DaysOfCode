import random

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " " + "Pie")
    print(fruits)

student_scores = [10,50,1000,5000]

total_exam_score = sum(student_scores)

sum = 0
for score in student_scores:
    sum += score

print(sum)

print(max(student_scores))


student_result = [13,96,1313,9696]
max_score = 0
for score in student_result:
    if score > max_score:
        max_score = score

for number in range(30,70,3): # start-stop-step mechanism
    print(number)

total = 0
for number in range(0,101,1):
    total += number # it just skips to the next line when the loop ends.
print(total)

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
           "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "/", "<", ">", "?"]

lenght_password = int((input("How long do you want your password to be?\n")))
symbols_password = int(input("How many symbols do you want in your password to be?\n"))
numbers_password = int(input("How many numbers do you want in your password to be?\n"))

password = []

for length in range(0,lenght_password):
    random_letter = random.choice(letters)
    password += random_letter

for number in range(0,numbers_password):
    random_number = random.choice(numbers)
    password += random_number

for symbol in range(0,symbols_password):
    random_symbol = random.choice(symbols)
    password += random_symbol

random.shuffle(password)
print((password))