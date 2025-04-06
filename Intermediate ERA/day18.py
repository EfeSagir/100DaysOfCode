from turtle import Turtle as a 
from turtle import Screen as b
import heroes

print(heroes.gen())

TimmyTheTurtle = a()

TimmyTheTurtle.shape("turtle")
TimmyTheTurtle.color("green")
TimmyTheTurtle.forward(100)

def MakeSquare():
    TimmyTheTurtle.right(90)
    TimmyTheTurtle.forward(100)
    
MakeSquare()
MakeSquare()
MakeSquare()
MakeSquare()

for i in range(4):
    TimmyTheTurtle.forward(100)
    TimmyTheTurtle.right(90)

Screen = b()
Screen.exitonclick()