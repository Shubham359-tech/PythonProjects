from turtle import Turtle
import random


# we will inherit Food class from turtle so that food class does what the turtle does.
class Food(Turtle):
    def __init__(self):
        super().__init__() # food has all the capabilities of turtle class
        self.shape("circle")  # shape of the food
        self.penup()  # penup so that it do not draw
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # so that the turtle is 10 by 10 ,0.5 because it is reduced
        # by half of its original 20 by 20 pixel

        self.color("yellow")  # sets the color of the food
        self.speed("fastest")  # so that we can avoid its animation effect
        self.refresh()  # refreshes for new location

    # this method is to give new location to the food
    def refresh(self):
        random_x = random.randint(-280, 280)  # -280,280 as turtle will die at screen edge
        # if the food appear at the edge as it is 300 by 300 matrix.
        random_y = random.randint(-280, 280)

        # using goto function for food to relocate
        self.goto(x=random_x, y=random_y)
