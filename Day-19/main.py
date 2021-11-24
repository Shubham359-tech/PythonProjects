# from turtle import Turtle, Screen
#
# new_turtle = Turtle()
#
# screen = Screen()  # Controls the screen.
#
#
# # fun to move fordward
# def move_fordward():
#     new_turtle.forward(10)
#
#
# # function to move backward
# def move_backward():
#     new_turtle.backward(10)
#
#
# # function to turn left direction
# def turn_left():
#     new_turtle.left(10)
#
#
# # function to turn right
# def turn_right():
#     new_turtle.right(10)
#
#
# # method to clear the drawing
# def clear():
#     new_turtle.clear()  # clears the drawing of the turtle
#     new_turtle.penup()  # to prevent the line drawn by turtle while comming back to origin
#     new_turtle.home()  # brings the turtle at the origin (0,0)
#     new_turtle.pendown()  # the turtle will be ready to draw the line again
#
#
# # Starts listening the event listeners
# screen.listen()
#
# # Using the event listener to bind the function on key stroke of keyboard
# # screen.onkey(key="space", fun=move_fordward)  # here for function we dont use "()"
# # space bar is a key and after key is pressed then the event is the function
# # In python there is a concept of higher order function , a function which can work with all other functions
#
# # Make a Etch-A-Sketch App
# screen.onkey(key="w", fun=move_fordward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear)
#
# screen.exitonclick()


# Turtle Game
from turtle import Turtle, Screen
import random

# new_turtle = Turtle(shape="turtle")  # we can also give shape to the turtle while creating the object
screen = Screen()
screen.setup(width=500, height=400)  # Setting the height and width of the screen

turtle_colors = ["orange", "blue", "yellow", "green", "red", "violet"]
y_positions = [-100, -70, -40, -10, 20, 50]  # here are only y-coordinates ,x cordinates remains same always as we -
# starting from same left side.

# list of the turtle
turtle_list = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle") # turtle object size is 40 * 40
    new_turtle.color(turtle_colors[turtle_index])  # accessing colors from the colors list
    # understanding turtle coordinate system
    # new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])  # goto function is used to set the coordinates of the turtle's -
    # position
    # we didn't use as x=-250 because it will hide below the line as -250 is the last coordinates

    # appending turtle to the turtle list so that each turtle moves
    turtle_list.append(new_turtle)

# Taking the input using prompt
user_bet = screen.textinput(title="turtle race", prompt="Bet the turtle ")
# print(user_bet)

# Creating of the flag
is_bet_off = False

# creating the while loop as we dont know which turtle will reach the final spot
while not is_bet_off:
    # creating the for loop so that every turtle moves
    for turtle in turtle_list:
        if turtle.xcor() > 230: # as turtle object is 40*40 so, 250-(40/2) = 230
            is_bet_off = True
            print(turtle.pencolor()) # we print here pencolor as we want pencolor from color function as -
            # color(fillcolor,pencolor)
            if turtle.pencolor() == turtle.color():
                print(f"hurray!!!!!!!!!!!!!!! you won the bet")
            else:
                print(f"sorry you lost the bet, the winner of the race is {turtle.pencolor()}")

        move_forward = random.randint(0, 10)
        turtle.forward(move_forward)

screen.exitonclick()