from turtle import Turtle, Screen

#Constants defined outside of class and in capitals.
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0



class Snake:

    def __init__(self):
        #Define empty list.
        self.segments = []

        #Call method to create snake.
        self.create_snake()
        # self.move_snake()
        self.head = self.segments[0]


    def create_snake(self):
        # Cycle throught the start position tuples and create a turtle object.
        for position in START_POSITIONS:
            # Create a new segment.
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()

            # Send the segment to the position in the list
            new_segment.goto(position)
            # Add the segment to list.
            self.segments.append(new_segment)

    def move_snake(self):
        # For each number in range(range is the size of the segments list - 1 to 0, this is the revers.  Step is -1 to go backwards in range
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Get the previous segment x and set as new x
            new_x = self.segments[seg_num - 1].xcor()
            # Get the previous segment y and set as new y.
            new_y = self.segments[seg_num - 1].ycor()
            # Send current segment to previous segments position.
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)