import random

user_cards = []
dealer_cards = []
user_cards_values = []
dealer_cards_values = []
user_total = 0
dealer_total = 0
execution_finished = 0

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

        for char in dealer_cards:
            if(char == "A" and ((dealer_total + 11) > 21)): #TODO: her chari kontrol ederken if char a ise ayri yere gonder onlari orada topla ve bitince onlarin toplamini bul when char = dealer_cards[-1] check if a = 11 busts or not and then calculate the a prices and calculate this if there are couple a's.
                dealer_total += 1
            else:
                dealer_total += card_values[char]
        for char in user_cards:
            if(char == "A" and ((user_total + 11) > 21)):
                user_total += 1
            else:
                user_total += card_values[char] #TODO: this if else block is false. if you consider a as 11 always when user total is under 21 you could bust without the capabilites of a
        
        # if(user_total > 21):  #TODO: if user total is over 21 with the as exceptional situtaion end it here and dont let it go to the asking part where takes input. same as for dealer.
        #     if(dealer_total > 21):
        #         print("Draw!")
        #     elif(21 >= dealer_total):
        #         print("Bust! You Lost!")
        # if(dealer_total >21):
        #     if(user_total >21):
        #         print("Draw")
        #     elif(21 >= user_total):
        #         print("Bust! You Lost!") #TODO: i dont like these if else blocks they might be more decent. 

        if(execution_finished == 1):
            break
        

        asking = input("Do you want to draw a card, stand or exit? Type draw, stand or exit:" + " ").lower()


        if (asking == "draw"):
            random_card = random.choice(cards)
            user_cards.append(random_card)
            cards.remove(random_card)
            print("Your Hand:",user_cards)
            print("Dealer's Hand: ['" + dealer_cards[0] + "', '?']")

        elif (asking == "stand"):
            print("Your Hand:",user_cards)

            execution_finished += 1
            if(16 >= dealer_total):
                random_dealer_card = random.choice(cards)
                dealer_cards.append(random_dealer_card)
                cards.remove(random_dealer_card)
                print("Dealers Hand:",dealer_cards)
            elif(dealer_total >= 17):
                print("Dealers Hand:",dealer_cards)

        elif(asking == "exit"):
            break

if(yes_or_no == "no"):
    None