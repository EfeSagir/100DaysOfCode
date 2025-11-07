from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time,random

def relocate():
    new_X = random.randint(-330,330)
    new_Y = random.randint(-330,330)
    food.goto(new_X,new_Y)

screen = Screen()
screen.setup(700,700)
screen.listen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
screen.title("SNAKE GAME")

snake = Snake()

food = Food()

scoreboard = Scoreboard()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    print(snake.head.xcor())
    print(snake.head.ycor())
    snake.move()
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        relocate()
        scoreboard.increase_score()
    if snake.head.xcor() == -360 or snake.head.xcor() == 360 or  snake.head.ycor() == -360 or snake.head.ycor() == 360:
        game_is_on = False
        scoreboard.game_over()
    


screen.exitonclick()
