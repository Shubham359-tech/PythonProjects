from turtle import Turtle


class Ball(Turtle):  # turtle class is inherited
    def __init__(self):
        super().__init__()  # all functionality of turtle is now also of Ball
        self.penup()  # so that it do not draw line
        self.color("white")  # changing the color of the turtle
        self.shape("circle")  # changing the shape of the turtle
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move  # moves 10 pixels at a time at x axis
        new_y = self.ycor() + self.y_move  # moves 10 pixels at a time at y axis
        self.goto(new_x, new_y)

    # function to bounce back for walls top and bottom
    def bounce_y(self):
        self.y_move *= -1  # if it is bounce on opposite side of y-axis then it will bounce in -ve side and if it is
        # bounce on negative side it will bounce on positive side as (minus into minus =+)

    # function to bounce back from right paddle
    def bounce_x(self):
        self.x_move *= -1  # if it is bounce on opposite side of x-axis then it will bounce in -ve side and if it is
        # bounce on negative side it will bounce on positive side as (minus into minus =+)

        # each time ball bounces back on x - axis speed should be increase and sleep time should be reduced
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
