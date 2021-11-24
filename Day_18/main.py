# from turtle import Turtle, Screen

# # import turtle # we this type of method when we don't use from kerwords...
# # tim = turtle.Turtle()
#
# # for importing every thing use
# # from turtle import *    # less used in python community
#
# # Alias
# # import turtle as t -> here t is alias
#
# # installing the pacakages
# # import heroes #-> use pip install command from python website called as pypi
# # print(heroes.gen())
#
# tim = Turtle()  # creating the object of class turtle
#
# # changing the shape of the turtle
# tim.shape("turtle")  # Go to the documentations "turtle graphics docmentation-Goggle Search"
#
# # Changing the color of the turtle
# tim.color("red")  # Color Control->Color->pen color->Tk color specification string(Google search)
#
# # Move the turtle forward
# tim.forward(100)
#
# # challenge 1: Drawing the square using right and left function
# tim.right(90) # change the name of the object or variable : -> select the variable->rught click and click refactor and type
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)


# tim = Turtle()

# Challenge 2: Draw dash line
# for i in range(6):
#     tim.forward(9)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()

# Challenge 3: Draw different shapes after shapes
from random import *

# color = ["red", "green", "blue"]
#
#
# def drawshape(number_of_sides):
#     angle = 360 / number_of_sides
#     for i in range(number_of_sides):
#         tim.forward(100)
#         tim.left(angle)
#
#
# for sides in range(3, 11):
#     tim.color(choice(color))
#     drawshape(sides)
#


# # Challenge 4: Random Walk

# colours = ["cyan","pale turquoise","dark turquoise","yellow","maroon","dark magenta"]
# direction = [0, 90, 180, 270]
# # increasing the thickness of the turtle
# tim.pensize(9)
# for _ in range(201):
#     tim.color(choice(colours))
#     tim.forward(30)
#     # this function is used for moving turtle in all directions.
#     tim.setheading(choice(direction))

# # ******Use RGB values ******
# import turtle as t
# tim = t.Turtle()
#
# t.colormode(255)  # it sets the rgb value fro 0 to 255
#
#
# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     return (r, g, b)
#
#
# direction = [0, 90, 180, 270]
# # increasing the thickness of the turtle
# tim.pensize(9)
# for _ in range(201):
#     tim.color(random_color())  # Giving the color of rgb to the turtle
#     tim.forward(30)
#     # this function is used for moving turtle in all directions.
#     tim.setheading(choice(direction))
#
# screen = t.Screen()  # exits the screen when only we click
# screen.exitonclick()

import turtle as t

tim = t.Turtle()
t.colormode(255)  # it sets the rgb value fro 0 to 255


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")


def draw(size_of_gap):
    for _ in range(int(360 / size_of_gap)):  # this div gives answer of how many parts circle is divided using that
        # gap so as to stop after that much gap
        tim.color(random_color())
        tim.circle(100)  # Drawing of the circle
        current_heading = tim.heading()  # Gives current position of the turtle
        tim.setheading(current_heading + 10)  # moving the turtle 10 points forward.
        tim.circle(100)


draw(10)

screen = t.Screen()
screen.exitonclick()
