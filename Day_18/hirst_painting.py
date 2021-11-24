# from colorgram import *
#
# colours = colorgram.extract("image.jpg",12)
# # print(colours)
# # creating a list for storing the rgb values
# rgb_colours = []
# # here we get hcl and rgb two types of colors values so to get only rgb value that too in a list
# for colour in colours:
#     #      Appending of each colour rgb value to the list
#     # rgb_colours.append(colour.rgb) # this gives out put as rbg(123,255,144) type but we want tuple list
#     r = colour.rgb.r # accessing each of the value
#     g = colour.rgb.g
#     b = colour.rgb.b
#     # creating the tuple for these values
#     new_color = (r,g,b)
#     rgb_colours.append(new_color)
# print(rgb_colours)

# creating the list of the program output of the above code
import turtle as t
import random

# changing the mode of color of turtle
t.colormode(255)
tim = t.Turtle()
tim.penup()  # This avoids the line to be drawn in a fig.
color_list = [(225, 229, 237), (241, 234, 215), (242, 229, 238), (224, 239, 231), (191, 166, 121), (142, 165, 189),
              (136, 94, 57), (63, 100, 135), (219, 207, 130), (13, 23, 55), (183, 149, 168), (144, 175, 154)]

tim.setheading(225)  # it takes 45 degree angle to come to tne bottom left corner
tim.forward(300)  # turtle moves towards the 45 degree angle by 300
tim.setheading(0)  # Again the turtle heading is set to the zero degree
number_of_dots = 100  # number of dots to be drawn .
tim.speed("fastest")
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))  # draws the dot
    tim.forward(50)

    if dot_count % 10 == 0:  # Function to set the turtle at the starting point again
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
