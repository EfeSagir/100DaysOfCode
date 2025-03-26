from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

is_on = True
while is_on == True:
    choice = input(f"What kind of coffee do you want? {menu.get_items()} ").lower()
    if(choice == "report"):
        coffee_maker.report()
        money.report()
    elif(choice == "off"):
        is_on = False
    else:
        drink = menu.find_drink(choice)
        if(coffee_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost)):
                coffee_maker.make_coffee(drink)