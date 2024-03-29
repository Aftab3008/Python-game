FONT = ("Courier", 24, "normal")
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.initial_level=1
        self.penup()
        self.hideturtle()
        self.goto(-280,260)
        self.write(f"Level:{self.initial_level}",align='left',font=FONT)

    def increase_level(self):
        self.initial_level+=1
        self.clear()
        self.write(f"Level:{self.initial_level}",align='left',font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align='center',font=FONT)
