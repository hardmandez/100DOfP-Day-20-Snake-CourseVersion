from turtle import Screen, Turtle
import random

class Food:

    def __init__(self):
        self.food_segment = []
        self.create_food()
        self.move_food()

    def create_food(self):
        self.food_segment = Turtle()
        self.food_segment.color("red")
        self.food_segment.shape("circle")
        self.food_segment.penup()

    def move_food(self):
        food_x = random.randrange(-280, 280)
        food_y = random.randrange(-280, 280)
        self.food_segment.goto(food_x, food_y)

