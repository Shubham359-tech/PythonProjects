from turtle import Screen
import time  # we are importing time as animation is turnes off so we cannot use turtle.speed() function
from snake import Snake  # importing snake class from the main1
from food import Food
from scoreboard import Scoreboard

# creating of the screen
screen = Screen()
# setting of the screen size
screen.setup(width=600, height=600)
# changing the background color
screen.bgcolor("black")
# setting of the title of the window
screen.title("My snake game")
# setting the turtle animation off
screen.tracer(0)

# creating the snake object
snake = Snake()

# creating the food object
food = Food()

# creating the Scoreboard object
score = Scoreboard()

# Adding key listeners
screen.listen()
screen.onkey(snake.up, "Up")  # will determine the movements of the snake
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# setting of the flag
game_is_on = False

while not game_is_on:
    # updates the screen
    screen.update()
    # delay of 1 sec
    time.sleep(0.1)
    # Every time the screen refreshes the snake moves
    snake.move()

    # detect the collision between snake and food
    if snake.head.distance(food) < 15:  # snake.head is used to get position hold & .distance methos determines the
        # distance between two turtles
        food.refresh()
        # update score
        score.increase_score()
        # each time snake eat the food snake extends
        snake.extend()

    # detect the collision of the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = True  # exits while loop and in turn exits the game
        score.game_over()

    # detecting the collision between segments
    for segment in snake.segments[1:]:  # it checks for every segment
        if snake.head.distance(segment) < 10:  # if the distance btwn snake head and body is less than 10 px
            # then it is assume to be collided

            game_is_on = True
            score.game_over()

screen.exitonclick()
