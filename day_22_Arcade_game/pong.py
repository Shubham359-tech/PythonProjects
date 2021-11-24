from turtle import Turtle


class Paddle_body(Turtle):
    def __init__(self, position):
        super().__init__()  # inherits the turtle class
        self.penup()  # so that it do not draw line
        self.shape("square")  # gives square shape
        self.color("white")  # giving white color because it wont show on black screen
        self.shapesize(stretch_wid=5, stretch_len=1)  # setting of pong
        self.goto(position)  # giving the position to the pong

    def go_up(self):  # function to go up
        new_y = self.ycor() + 20  # each time up key is pressed then +20 pixels gets added to new_y
        self.goto(self.xcor(), new_y)  # xcor remain the same as we want it on x axis

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
