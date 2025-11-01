from turtle import Screen, Turtle
import time

#Set up game screen.
screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
#Switch of the screen update so can update screen manually
screen.tracer(0)

#Define the starting position of the three objects to be created.
starting_positions=[(0,0),(-20,0),(-40,0)]

#Define empty list.
segments = []

#Cycle throught the start position tuples and create a turtle object.
for position in starting_positions:
    #Create a new segment.
    new_segment=Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    #Send the segment to the position in the list
    new_segment.goto(position)
    #Add the segment to list.
    segments.append(new_segment)


game_is_on = True
while game_is_on:
    #Update the screen.
    screen.update()
    #Sleep to affect the screen update speed\fluidity.
    time.sleep(0.1)

    #For each number in range(range is the size of the segments list - 1 to 0, this is the revers.  Step is -1 to go backwards in range
    for seg_num in range(len(segments)-1,0,-1):
        #Get the previous segment x and set as new x
        new_x=segments[seg_num-1].xcor()
        #Get the previous segment y and set as new y.
        new_y=segments[seg_num-1].ycor()
        #Send current segment to previous segments position.
        segments[seg_num].goto(new_x,new_y)

    #move segments.
    segments[0].forward(20)
    segments[0].left(10)




screen.exitonclick()