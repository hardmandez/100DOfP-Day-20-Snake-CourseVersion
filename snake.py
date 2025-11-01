class Snake:
    starting_positions = [(0, 0), (-20, 0), (-40, 0)]

    def __init__(self):


        # Define empty list.
        segments = []

        # Cycle throught the start position tuples and create a turtle object.
        for position in starting_positions:
            # Create a new segment.
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            # Send the segment to the position in the list
            new_segment.goto(position)
            # Add the segment to list.
            segments.append(new_segment)