from turtle import Turtle

# creating constants
ALIGNENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  # gets all properties of turtle super class
        self.score = 0  # initialized score to zero
        self.color("white")  # white color for visibility over black
        self.penup()  # so that turtle do not draw a line
        self.hideturtle()  # so that turtle is not visible on score
        self.goto(0, 260)  # setting turtle to up of the window
        self.update_score()  # initializing score , alignment, font , etc  to the turtle

    def update_score(self):
        self.write(f"Score ={self.score} ", align=ALIGNENT, font=FONT)  # writing on the turtle

    def increase_score(self):
        self.score += 1  # increasing of the score every time food is eaten
        self.clear()  # clearing of previous score
        self.update_score()  # Again writing of the new score.

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGNENT, font=FONT)
