import random

net_fortune = {
    "Neymar": "200000000",
    "Shakira": "300000000",
    "Pique": "80000000",
    "Messi": "400000000",
    "Ronaldo": "500000000",
    "Sergio Ramos": "80000000",
    "Eminem": "230000000",
    "Bruno Mars": "175000000",
    "Tarkan": "40000000",
    "Gabe Newell": "4500000000",
    "Notch": "2500000000"
}
point = 0
higher = 0
lower = 0
breaking = 0
def increment():
    global point
    point += 1
def YesNo():
        global yes_no, breaking, point
        if yes_no == "yes":
            if(int(net_fortune[itwo]) < int(net_fortune[ione])):
                point += 1
                print("+1 POINT!")
            else:
                breaking = 1
                print("GAME HAS ENDED. Your point is: "+str(point)) 

        elif yes_no == "no":
            if(int(net_fortune[itwo]) > int(net_fortune[ione])):
                point += 1
                print("+1 POINT!")
            else:
                breaking = 1
                print("GAME HAS ENDED. Your point is: "+str(point)) 
            
def net_worth_comparison():
    names = ["Neymar","Shakira","Pique","Messi","Ronaldo","Sergio Ramos","Eminem","Bruno Mars","Tarkan","Gabe Newell","Notch"]

    for i in names:
        global breaking, ione, itwo, yes_no
        if(breaking == 1):
                break
        if(point == 0):
            ione = random.choice(names)
            names.remove(ione)
            itwo = random.choice(names)
        elif(point >=1):
            ione = itwo
            names.remove(ione)
            itwo = random.choice(names)
        yes_no = input(f"Is {ione} richer than {itwo}?\n").lower()
        YesNo()
        if(breaking == 1):
            break
net_worth_comparison()