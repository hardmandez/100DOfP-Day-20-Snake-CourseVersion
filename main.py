from turtle import Screen, Turtle

from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time


#Set up game screen.
screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
#Switch off the screen update so can update screen manually
screen.tracer(0)


#Setup snake.
snake  = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")


game_is_on = True
while game_is_on:
    #Update the screen.
    screen.update()
    #Sleep to affect the screen update speed\fluidity.
    time.sleep(0.1)

    snake.move_snake()

    #Detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_segment()
        scoreboard.refresh_score()



screen.exitonclick()