from turtle import Turtle as a 
from turtle import Screen as b
import heroes
import random
print(heroes.gen())

TimmyTheTurtle = a()

TimmyTheTurtle.shape("turtle")
TimmyTheTurtle.color("green")


def MakeSquare():
    TimmyTheTurtle.right(90)


# for i in range(15):
#     TimmyTheTurtle.forward(10)
#     TimmyTheTurtle.penup()
#     TimmyTheTurtle.forward(10)
#     TimmyTheTurtle.pendown()

        
colors = [
    "red", "blue", "green", "orange", "purple",
    "yellow", "pink", "brown", "cyan", "magenta",
    "lime", "gold", "turquoise", "violet", "gray"
]

for SidesNumber in range(3,11):
    for i in range(SidesNumber):
        TimmyTheTurtle.forward(100)
        TimmyTheTurtle.right(360/(SidesNumber))
        TimmyTheTurtle.color(random.choice(colors))
    
# MakeSquare()
# MakeSquare()
# MakeSquare()
# MakeSquare()

# for i in range(4):
#     TimmyTheTurtle.forward(100)
#     TimmyTheTurtle.right(90)

Screen = b()
Screen.exitonclick()