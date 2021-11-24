from turtle import Turtle, Screen
# Constants are always are written in capital
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# constants for moving ,constants are taken because of changing it whenever we want
FORWARD_MOVE = 20
# creating the constants of the Directions
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()  # when we create object in main class create method id invoked
        self.head = self.segments[0]

    def create_snake(self):
        # creating the snake body using turtle
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # creting the add_segment function for adding turtle to the last of the snake body
    def add_segment(self, position):  # it takes position arguments to add that segment to that position of snake body
        new_segment = Turtle(shape="square")  # snake object is created each time till for loop exit
        new_segment.penup()  # prevents the drawing of the line
        new_segment.color("white")
        new_segment.goto(position)  # segment go to that position to get add
        # appending every object to the segments list as we have to take action on each object every time
        self.segments.append(new_segment)

    # creating the extend function to increase the length of the snake
    def extend(self):
        self.add_segment(self.segments[-1].position())  # we will get hold of last segment of the snake body so that
        # next segment to add there whereas .position is the method of turtle to get the position of the last turtle
        # i.e segment

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):  # -1 is to reverse traversing the list
            new_x = self.segments[seg - 1].xcor()  # getting the coordinates of the front turtle of the recent turtle
            # as traversing is from reverse direction so to get hold of its front turtle
            new_y = self.segments[seg - 1].ycor()
            # pushing the current turtle to the front trutle position
            self.segments[seg].goto(x=new_x, y=new_y)

        # now moving the 1st turtle forward
        self.segments[0].forward(FORWARD_MOVE)  # 20 because it is 20 by 20 turtle
        # segment_list[0].left(90)

    # creating the functions for moving in all four directions.
    def up(self):
        if self.segments[0].heading() != DOWN:  # snake cannot move reverse up when it is pointing to the down
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:  # snake cannot move reverse down when it is pointing to the up
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.segments[0].heading() != LEFT:
            # snake cannot move reverse left when it is pointing to the right
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            # snake cannot move reverse left when it is pointing to the right
            self.segments[0].setheading(LEFT)
