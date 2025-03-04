import random
import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

user_cards = []
dealer_cards = []
user_cards_values = []
dealer_cards_values = []
user_total = 0
dealer_total = 0
execution_finished = 0
user_ace_count = 0
dealer_ace_count = 0

cards = ["2", "2", "2", "2",
         "3", "3", "3", "3",
         "4", "4", "4", "4",
         "5", "5", "5", "5",
         "6", "6", "6", "6",
         "7", "7", "7", "7",
         "8", "8", "8", "8",
         "9", "9", "9", "9",
         "10", "10", "10", "10",
         "J", "J", "J", "J",
         "Q", "Q", "Q", "Q",
         "K", "K", "K", "K",
         "A", "A", "A", "A"]

card_values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": [1,11]
}

yes_or_no = input("Do you want to play a hand of blackjack? Write 'Yes' or 'No': ").lower()

if (yes_or_no == "yes"):

    random_card1 = random.choice(cards)
    cards.remove(random_card1)
    user_cards.append(random_card1)

    random_card2 = random.choice(cards)
    cards.remove(random_card2)
    user_cards.append(random_card2)


    user_cards_values.append(card_values[random_card1])
    user_cards_values.append(card_values[random_card2])

    random_dealer_card1 = random.choice(cards)
    cards.remove(random_dealer_card1)
    dealer_cards.append(random_dealer_card1)

    random_dealer_card2 = random.choice(cards)
    cards.remove(random_dealer_card2)
    dealer_cards.append(random_dealer_card2)

    dealer_cards_values.append(card_values[random_dealer_card1])

    print("Your Hand:",user_cards)
    print("Dealer's Hand: ['" + dealer_cards[0] + "', '?']")

    while True:
        dealer_total = 0
        user_total = 0 
        for char in dealer_cards:
            if(char == "A"):
                dealer_ace_count += 1
            elif(char != "A"):
                dealer_total += card_values[char]
        if(dealer_ace_count > 1):
            if(21 >= (dealer_total + (11 + ((dealer_ace_count)-1) * 1))):
                dealer_total += (1   + ((dealer_ace_count)-1) * 1)
            elif((11 + ((dealer_ace_count)-1) * 1) >21):
                dealer_total += (dealer_ace_count)
        elif(dealer_ace_count == 1):
            if(11 > dealer_total):
                dealer_total += 11
            elif(dealer_total >= 21):
                dealer_total += (dealer_ace_count) * 1
                
        for char in user_cards:
            if(char == "A"):
                user_ace_count += 1
            elif(char != "A"):
                user_total += card_values[char]
        if(user_ace_count > 1):
            if(21 >= (user_total + (11 + ((user_ace_count) - 1) * 1))):
                user_total += (1 + ((user_ace_count) - 1) * 1)
            elif((11 + ((user_ace_count) - 1) * 1) > 21):
                user_total += (user_ace_count)
        elif(user_ace_count == 1):
            if(11 > user_total):
                user_total += 11
            elif(user_total >= 21):
                user_total += (user_ace_count) * 1
                
        
        if execution_finished == 1:
            if user_total > 21 and dealer_total > 21:
                clear_screen()
                print("Your Hand:",user_cards)
                print("Dealers Hand:",dealer_cards)
                print("ITS A TIE!")
                
            elif user_total > 21:
                clear_screen()
                print("Your Hand:",user_cards)
                print("Dealers Hand:",dealer_cards)
                print("HOUSE WINS!")

            elif dealer_total > 21:
                clear_screen()
                print("Your Hand:",user_cards)
                print("Dealers Hand:",dealer_cards)
                print("YOU WON!")

            elif dealer_total == user_total:
                clear_screen()
                print("Your Hand:",user_cards)
                print("Dealers Hand:",dealer_cards)
                print("ITS A TIE!")

            elif user_total < 21 and dealer_total < 21:
                if dealer_total > user_total:
                    clear_screen()
                    print("Your Hand:",user_cards)
                    print("Dealers Hand:",dealer_cards)
                    print("HOUSE WINS!")
                else:
                    clear_screen()
                    print("Your Hand:",user_cards)
                    print("Dealers Hand:",dealer_cards)
                    print("YOU WON!")
            else:
                if user_total > dealer_total:
                    clear_screen()
                    print("Your Hand:",user_cards)
                    print("Dealers Hand:",dealer_cards)
                    print("YOU WON!")
                else:
                    clear_screen()
                    print("Your Hand:",user_cards)
                    print("Dealers Hand:",dealer_cards)
                    print("HOUSE WINS!")
            break
        if(user_total>=21):
            execution_finished = 1
        if (execution_finished == 0):
            asking = input("Do you want to hit, stand or surrender? Type hit, stand or surrender:" + " ").lower()
        else:
            continue

        if (asking == "hit"):
            random_card = random.choice(cards)
            user_cards.append(random_card)
            cards.remove(random_card)
            print("Your Hand:",user_cards)
            if(len(dealer_cards) == 2):
                print("Dealer's Hand: ['" + dealer_cards[0] + "', '?']")
            elif (len(dealer_cards) > 2):
                dealer_cards.append("?")
                print(dealer_cards)
                dealer_cards.remove("?")

        elif (asking == "stand"):
            execution_finished = 1
            print("Your Hand:", user_cards)
            if dealer_total < 17:
                while dealer_total < 17:
                    random_dealer_card = random.choice(cards)
                    dealer_cards.append(random_dealer_card)
                    cards.remove(random_dealer_card)
                    for char in dealer_cards:
                        if(char == "A"):
                            dealer_ace_count += 1
                        elif(char != "A"):
                            dealer_total += card_values[char]
                    if(dealer_ace_count > 1):
                        if(21 >= (dealer_total + (11 + ((dealer_ace_count)-1) * 1))):
                            dealer_total += (1   + ((dealer_ace_count)-1) * 1)
                        elif((11 + ((dealer_ace_count)-1) * 1) >21):
                            dealer_total += (dealer_ace_count)
                    elif(dealer_ace_count == 1):
                        if(11 > dealer_total):
                            dealer_total += 11
                        elif(dealer_total >= 21):
                            dealer_total += (dealer_ace_count) * 1
            print("Dealers Hand:", dealer_cards)
            
        elif(asking == "surrender"):
            break
        
if(yes_or_no == "no"):
    None