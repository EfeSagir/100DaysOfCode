import random
            
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
    random_card2 = random.choice(cards)
    random_card1_value = card_values[random_card1]
    random_card2_value = card_values[random_card2]
    random_dealer_card1 = random.choice(cards)
    random_dealer_card2 = random.choice(cards)
    random_dealer_card1_value = card_values[random_dealer_card1]
    random_dealer_card2_value = card_values[random_dealer_card2]

    if(random_card1 == "A"):
        if(random_card2 == "A"):
            print("Your Number Is: [2-12]")
        elif(random_card2 != "A"):
            print("Your Number Is: ["+str(random_card2_value + 1) + "- " + str(random_card2_value + 11) + "]")
            your_total = "["+str(random_card2_value + 1) + "- " + str(random_dealer_card2_value + 11) + "]"
 
    elif(random_card2 == "A"):
        if(random_card1 == "A"):
            print("Your Number Is: [2, 12]")
        elif(random_card1 != "A"):
            print("Your Number Is: ["+str(int(random_card1_value) + 1) + "- " + str(int(random_card1_value) + 11) + "]") 
            your_total = "["+str(random_card1_value + 1) + "- " + str(random_card_value + 11) + "]"

if (random_card1 != "A" and random_card2 != "A"):
    print(random_card1)
    print(random_card2)
    print("Your Number Is:" + "[" + str(random_card1_value + random_card2_value) + "]")

while True:

    asking = input("Do you want to draw a card or pass or exit? Type draw or pass or exit:").lower()

    if (asking == "draw"):
        random_card = random.choice(cards)
        random_card_value = card_values[random_card]

        if(random_card1 == "A"):
            if(random_card2 == "A"):
                if((12 + random_card_value) > 21):
                    print("21i gecti simdi de 2 ile toplamina bakalim")

                elif((2 + random_card_value <= 2)):
                    print("a")
            elif(random_card2 != "A"):

        elif(random_card2 == "A"):
            if(random_card1 == "A"):
                if((12 + random_card_value) > 21):
                    pass
                    checking_if_it_exploded = 1
                elif((2 + random_card_value <= 2)):
                    checking_if_it_exploded = 1

                    print("a")
            elif(random_card2 != "A"):
                

    if (asking == "pass"):
        print("efe you are going to show the result in here about who won")
        break

    elif (asking == "exit"):
        break

    #TODO: i forgot to extract the cards i have choosen from the deck we will fix that later.