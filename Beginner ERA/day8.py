def greet():
    print("Hello")
    print("How are you?")
    print("It's been a long time since I saw you, how are you?")

greet()


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}?")
    print(f"It's been a long time since I saw you, how are you {name}?")

greet_with_name("Angela")
# name is our parameter and Angela is your argument


def life_in_weeks(age):
    weeks_left = 52 * (90 - age)
    print(f"You have {weeks_left} weeks left.")

life_in_weeks(18)

def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Serdar","Istanbul")
greet_with(name = "Serdar",location = "Istanbul")

true_letter_count = 0
love_letter_count = 0
T_letter_count = 0
R_letter_count = 0
U_letter_count = 0
true_E_letter_count = 0
L_letter_count = 0
O_letter_count = 0
V_letter_count = 0
E_letter_count = 0
name1 = "Angela Yu"
name2 = "Jack Bauer"
for true_letters in name1:
    if(true_letters == "T"):
        true_letter_count += 1
        T_letter_count += 1
    elif(true_letters =="R"):
        true_letter_count += 1
        R_letter_count += 1
    elif (true_letters == "U"):
        true_letter_count += 1
        U_letter_count += 1
    elif (true_letters == "E"):
        true_letter_count += 1
        true_E_letter_count += 1
    elif (true_letters == "t"):
        true_letter_count += 1
        T_letter_count += 1
    elif (true_letters == "r"):
        true_letter_count += 1
        R_letter_count += 1
    elif (true_letters == "u"):
        true_letter_count += 1
        U_letter_count += 1
    elif (true_letters == "e"):
        true_letter_count += 1
        true_E_letter_count += 1
    else:
        continue
    print(T_letter_count)
    print(R_letter_count)
    print(U_letter_count)
    print(E_letter_count)
    print(true_letter_count)

for love_letters in name2:
    if(love_letters == "L"):
        love_letter_count += 1
        L_letter_count += 1
    elif(love_letters == "O"):
        love_letter_count += 1
        O_letter_count += 1
    elif (love_letters == "V"):
        love_letter_count += 1
        V_letter_count += 1
    elif (love_letters == "E"):
        love_letter_count += 1
    elif (love_letters == "l"):
        love_letter_count += 1
        L_letter_count += 1
    elif (love_letters == "o"):
        love_letter_count += 1
        O_letter_count += 1
    elif (love_letters == "v"):
        love_letter_count += 1
        V_letter_count += 1
    elif (love_letters == "e"):
        love_letter_count += 1
    else:
        continue
    print(L_letter_count)
    print(O_letter_count)
    print(V_letter_count)
    print(E_letter_count)
    print(love_letter_count)


def calculate_love_score(name1, name2):
    combined_name = name1 + name2

    true_count = 0
    love_count = 0
    t_count = 0
    r_count = 0
    u_count = 0
    e_count = 0
    l_count = 0
    o_count = 0
    v_count = 0

    for letter in combined_name.lower():
        if letter == "t" or letter == "r" or letter == "u" or letter == "e":
            true_count += 1
            if letter == "t":
                t_count += 1
            elif letter == "r":
                r_count += 1
            elif letter == "u":
                u_count += 1
            elif letter == "e":
                e_count += 1

    for letter in combined_name.lower():
        if letter == "l" or letter == "o" or letter == "v" or letter == "e":
            love_count += 1
            if letter == "l":
                l_count += 1
            elif letter == "o":
                o_count += 1
            elif letter == "v":
                v_count += 1
            elif letter == "e":
                e_count += 1

    print(f"T occurs {t_count} times")
    print(f"R occurs {r_count} times")
    print(f"U occurs {u_count} times")
    print(f"E occurs {e_count} times")
    print(f"L occurs {l_count} times")
    print(f"O occurs {o_count} times")
    print(f"V occurs {v_count} times")

    love_score = str(true_count) + str(love_count)
    print(f"Love Score: {love_score}")

fruits = ["apple","peach","pear"]
numero_uno = fruits.index("peach")
print(numero_uno)

cars = [911,1.6]
numero_uno = cars.index(1.6)
print(numero_uno)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
direction = input("Do you want to encrypt or decrypt? To encrypt write encrypt and to decrypt write decode.\n").lower()
text = input("Type the text you want to use\n").lower()
shift_amount = int(input("Type the amount of shift you want\n"))
def encrypt(text, shift_amount):
    cipher_text = []

    for letter in text:
        if (letter not in alphabet):
            cipher_text += letter
        indexing_number = alphabet.index(letter) + shift_amount
        if (indexing_number>=26):
            indexing_number %= len(alphabet)
        cipher_text.append(alphabet[indexing_number])

    print(f"Your cipher text is:{cipher_text}")


def decrypt(text, shift_amount):
    cipher_text = []

    for letter in text:
        if (letter not in alphabet):
            cipher_text += letter
        indexing_number = alphabet.index(letter) - shift_amount
        if (indexing_number >= 26):
            indexing_number %= len(alphabet)
        cipher_text.append(alphabet[indexing_number])

    print(f"Your cipher text is:{cipher_text}")


def ceasar(text,shift_amount,direction):
    if(direction == "decode"):
        decrypt(text,shift_amount)

    elif(direction== "encrypt"):
        encrypt(text,shift_amount)

ceasar(text,shift_amount,direction)

yes_or_no = input("Would you like to change your choice of direction? Type yes or no.?\n").lower()
if(yes_or_no == "yes"):
    ceasar(text,shift_amount,direction="encrypt")
else:
    print("Okay bro.")