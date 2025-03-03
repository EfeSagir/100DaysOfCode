def espresso():
    global profit, x, z, a, c
    x = resources["water"]
    z = resources["milk"]

    resources["water"] -= MENU["espresso"]["ingredients"]["water"]
    resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]

    if(resources["water"] <= 0 or resources["milk"] <= 0):
        resources["water"] += MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] += MENU["espresso"]["ingredients"]["coffee"]
        profit -= 1.5

    a = resources["water"]
    c = resources["coffee"]

    if(x == a or z == c):
        print("INSUFFICIENT INGREDIENTS")




    profit += 1.5

def latte():
    global profit, x, y, z, a, b,c

    x = resources["water"]
    y = resources["milk"]
    z = resources["coffee"]

    resources["water"] -= MENU["latte"]["ingredients"]["water"]
    resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
    resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]

    if(resources["water"] or resources["milk"] or resources["coffee"] <= 0):
        resources["water"] += MENU["latte"]["ingredients"]["water"]
        resources["milk"] += MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] += MENU["latte"]["ingredients"]["coffee"]
        profit -= 2.5


    a = resources["water"]
    b = resources["milk"]
    c = resources["coffee"]

    if(x == a or y== b or z == c):
        print("INSUFFICIENT INGREDIENTS")

    profit += 2.5

def cappucino():
    global profit, x, y, z, a, b,c

    x = resources["water"]
    y = resources["milk"]
    z = resources["coffee"]

    resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
    resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
    resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]

    if(resources["water"] or resources["milk"] or resources["coffee"] <= 0):
        resources["water"] += MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] += MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] += MENU["cappuccino"]["ingredients"]["coffee"]
        profit -= 3.0

    a = resources["water"]
    b = resources["milk"]
    c = resources["coffee"]

    if(x == a or y== b or z == c):
        print("INSUFFICIENT INGREDIENTS")

    profit += 3.0

        
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

while True:

    coffee = input("What do you want? (espresso, latte, cappucino)\n").lower()

    #TODO: suraya coin seyini yap ve bitti.
    if coffee == "espresso":
        espresso()
    elif coffee == "latte":
        latte()
    elif coffee == "cappucino":
        cappucino()
    elif coffee == "report":
        print(resources["water"], resources["milk"], resources["coffee"], profit)
    elif coffee == "off":
        break