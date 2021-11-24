from turtle import Screen, Turtle
from pong import Paddle_body
from ball import Ball
import time
from scoreboard import Scoreboard
# creating the screen object
screen = Screen()
# setting up the screen width and height
screen.setup(width=800, height=600)
# setting up the screen background color
screen.bgcolor("black")
# setting up the title of screen
screen.title("ping-pong game")
# setting the turtle animation off
screen.tracer(0)

# creating the paddle objects
r_paddle = Paddle_body((350, 0))
l_paddle = Paddle_body((-350, 0))

# creating the ball objects
ball = Ball()

#creating the scoreboard objects
scoreboard = Scoreboard()

screen.listen()  # used to listen key events
screen.onkey(r_paddle.go_up, "Up")  # here each paddle is calling up and down function from class Paddle_body
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()  # it refreshes the screen so that paddle is shown on the screen otherwise it will not show due to
    # tracer set to 0
    time.sleep(ball.move_speed)  # gap of sec  decreases while each iteration of while.
    # calling move function of ball class so that it avoids animation and continues till while loop ends
    ball.move()

    # Detecting the collision of the wall
    if ball.ycor() > 280 or ball.ycor() < -280:  # as ball is 20 pixel
        # ball bounce back
        ball.bounce_y()

    # detecting collision with r-paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:  #
        # 340 as it is long paddle and distance function only
        # measures the distance from yhe center
        ball.bounce_x()

    # detect  when the right paddle misses
    if ball.xcor() > 380:  # if ball passes above 380 then it definitely misses
        ball.reset_position() # ball comes to the center of the screen
        scoreboard.l_point() # increases the score by 1

    # detect when the left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# exit screen on click
screen.exitonclick()
