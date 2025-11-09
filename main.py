from turtle import Screen, Turtle

from food import Food
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
#Define the starting position of the three objects to be created.
# starting_positions=[(0,0),(-20,0),(-40,0)]

#Define empty list.
# segments = []

#Cycle throught the start position tuples and create a turtle object.
# for position in starting_positions:
#     #Create a new segment.
#     new_segment=Turtle("square")
#     new_segment.penup()
#     new_segment.color("white")
#     #Send the segment to the position in the list
#     new_segment.goto(position)
#     #Add the segment to list.
#     segments.append(new_segment)

screen.listen()
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    #Update the screen.
    screen.update()
    #Sleep to affect the screen update speed\fluidity.
    time.sleep(0.1)

    snake.move_snake()



screen.exitonclick()