from turtle import Turtle
import random
import time

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        self.food_random_x = random.randrange(-280, 280)
        self.food_random_y = random.randrange(-280, 280)
        self.goto(self.food_random_x, self.food_random_y)
