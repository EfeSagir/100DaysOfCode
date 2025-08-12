from turtle import Turtle,Screen
import random
is_race_on = None
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []
for i in range(6):
    t = Turtle()
    t.color(colors[i])
    t.shape("turtle")
    t.penup()
    t.goto(-300,200 -(i*50))
    t.pendown()
    all_turtles.append(t)



screen = Screen()
user_bet = screen.textinput("MAKE YOUR GUESS", "WHICH TURTLE WILL WIN?")
screen.setup(600,500)


def Forwards():
    Turtle_One.fd(10)
def Backwards():
    Turtle_One.bd(10)
def Counter_Clockwise():
    Turtle_One.left(10)
def Clockwise():
    Turtle_One.right(10)
def Clear():
    Turtle_One.clear()
    Turtle_One.penup()
    Turtle_One.home()
    Turtle_One.pendown()


if user_bet:
    is_race_on = True
while is_race_on:   
    
    for turtle in all_turtles:
        turtle.penup()
        rand_distance = random.randint(0,10)
        turtle.fd(rand_distance)
        if turtle.xcor() > 230:
            print(turtle.color())
            is_race_on = False
            if(str(user_bet) == turtle.color()):
                print("YOU WON")
            else:
                print("YOU LOSE")
screen.exitonclick()