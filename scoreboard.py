FONT = ("Courier", 24, "normal")
FONT1 = ("Courier", 18, "normal")
ALIGNMENT='center'

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score=0
        self.level=1
        self.penup()
        self.goto(-280,260)
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Level {self.level}", align='left', font=FONT1)
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()
