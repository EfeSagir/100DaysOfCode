import random

user_cards = []
dealer_cards = []
user_cards_values = []
dealer_cards_values = []
user_total = 0
dealer_total = 0

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
            dealer_total += card_values[char]
        if(char == "A"):
            print("efe eger 21i geciyorsa dealer totale 11 eklemek o zaman ayi 1 kabul et diceksin ama eger 21i gecmezse 11 eklenmesi 11 kabul ettireceksin direkt directly. astan sonraki kart 21i gecerse ayi 1 yapiyosun.")
        

        asking = input("Do you want to draw a card, pass or exit? Type draw, pass or exit:" + " ").lower()


        if (asking == "draw"):
            random_card = random.choice(cards)
            user_cards.append(random_card)
            cards.remove(random_card)

            
            dealer_cards.append("?")
            print("Your Hand:",user_cards)
            print("Dealer's Hand:",dealer_cards)
            dealer_cards.remove("?")
            if (dealer_total < 18):
                random_dealer_card = random.choice(cards)
                dealer_cards.append(random_dealer_card)

        elif (asking == "pass"):

            random_dealer_card = random.choice(cards)
            cards.remove(random_dealer_card)
            random_dealer_card_value = card_values[random_dealer_card]

        elif(asking == "exit"):
            break

if(yes_or_no == "no"):
    None

    #TODO: 18den sonra dealer daha acmiyor orada elinde ne varsa toplayip sonuca gidilecek pass dendiginde napildigini ogrenip ona gore yine bir seyler yapilacak
    #TODO: as istisnasi puan toplarken algoritmasi yazilacak sen soru isaretini string koydun aslinda onun yerine value koydurman lazim bak dealer icin o yuzden yanlis topluyor

    #TODO: kazanma olayi, anin kac kabul edilecegi duruma gore ne zaman bitis talimati verilecegi belirlenilip oyun bitirilecektir kodlari.