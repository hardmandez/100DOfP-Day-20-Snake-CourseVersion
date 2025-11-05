from main import starting_positions
from turtle import Turtle, Screen

class Snake:

    def __init__(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        segments = []
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")

        # Define empty list.

    def move_snake(self):

        # Cycle throught the start position tuples and create a turtle object.
        for position in starting_positions:
            # Create a new segment.

            # Send the segment to the position in the list
            self.new_segment.goto(position)
            # Add the segment to list.
            self.segments.append(new_segment)