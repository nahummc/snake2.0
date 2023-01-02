from turtle import Turtle
from snake import Snake
from turtle import Turtle

ALIGNMENT = "center"

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.update_score()
        self.tb = 70
        self.lr = 24
        self.goto(0, 260)


    def update_score(self):
        self.goto(0, 260)
        self.color("white")
        self.write(f"Score: {self.score} ", True, align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.penup()
        

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

