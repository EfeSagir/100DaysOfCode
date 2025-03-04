def espresso():
    global x, z, a, c
    x = resources["water"]
    z = resources["milk"]
    resources["water"] -= MENU["espresso"]["ingredients"]["water"]
    resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    if(resources["water"] < 0 or resources["milk"] < 0):
        resources["water"] += MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] += MENU["espresso"]["ingredients"]["coffee"]

    a = resources["water"]
    c = resources["coffee"]

    if(x == a or z == c):
        print("INSUFFICIENT INGREDIENTS")
    else:
        print("There is your espresso. Enjoy!")
    if(total_money >= MENU["espresso"]["cost"]):
        print(f"This is your change: {round(total_money - float(MENU['espresso']["cost"]),2)}$")

def latte():
    global x, y, z, a, b,c
    x = resources["water"]
    y = resources["milk"]
    z = resources["coffee"]
    resources["water"] -= MENU["latte"]["ingredients"]["water"]
    resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
    resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
    if(resources["water"] < 0 or  resources["milk"] < 0 or resources["coffee"] < 0):
        resources["water"] += MENU["latte"]["ingredients"]["water"]
        resources["milk"] += MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] += MENU["latte"]["ingredients"]["coffee"]
    a = resources["water"]
    b = resources["milk"]
    c = resources["coffee"]
    if(x == a or y== b or z == c):
        print("INSUFFICIENT INGREDIENTS")
    else:
        print("There is your latte. Enjoy!")
    if(total_money >= MENU["espresso"]["cost"]):
        print(f"This is your change: {round(total_money - float(MENU['espresso']["cost"]),2)}$")
    
def cappuccino():
    global x, y, z, a, b,c
    x = resources["water"]
    y = resources["milk"]
    z = resources["coffee"]
    resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
    resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
    resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
    if(resources["water"] < 0 or resources["milk"] < 0 or resources["coffee"] < 0):
        resources["water"] += MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] += MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] += MENU["cappuccino"]["ingredients"]["coffee"]

    a = resources["water"]
    b = resources["milk"]
    c = resources["coffee"]
    if(x == a or y== b or z == c):
        print("INSUFFICIENT INGREDIENTS")
    else:
        print("There is your coffee cappuccino. Enjoy!")
    if(total_money >= MENU["espresso"]["cost"]):
        print(f"This is your change: {round(total_money - float(MENU['espresso']["cost"]),2)}$")
    
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

while True:

    total_money = 0
    i = 0

    try:
        coffee = input("What do you want? (espresso, latte, cappuccino): ").lower()
        
        if coffee == "off":
            break
        elif coffee == "report":
            print(resources["water"], resources["milk"], resources["coffee"], total_money)
            continue
        elif coffee not in ["espresso", "latte", "cappuccino"]:
            raise ValueError("Invalid coffee choice. Please choose from espresso, latte, cappuccino.")
        
    except ValueError:
        print("Invalid coffee choice. Please choose from espresso, latte, cappuccino.")
        i = 1

    if i != 1:

        try:
            quarter_count = int(input("How many quarters are you going to insert? "))
            dime_count = int(input("How many dimes are you going to insert? "))
            nickle_count = int(input("How many nickels are you going to insert? "))
            penny_count = int(input("How many pennies are you going to insert? "))
            total_money = (quarter_count * 0.25) + (dime_count * 0.10) + (nickle_count * 0.05) + (penny_count * 0.01)
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            i = 1
        match coffee:
            case "espresso":
                if total_money >= MENU["espresso"]["cost"]:
                    espresso()
                    print(f"This is your change: {round(total_money - MENU['espresso']['cost'], 2)}$")
                else:
                    print("INSUFFICIENT MONEY")
            case "latte":
                if total_money >= MENU["latte"]["cost"]:
                    latte()
                    print(f"This is your change: {round(total_money - MENU['latte']['cost'], 2)}$")
                else:
                    print("INSUFFICIENT MONEY")
            case "cappuccino":
                if total_money >= MENU["cappuccino"]["cost"]:
                    cappuccino()
                    print(f"This is your change: {round(total_money - MENU['cappuccino']['cost'], 2)}$")
                else:
                    print("INSUFFICIENT MONEY")