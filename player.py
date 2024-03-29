STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.movement()
        self.color("black")
        self.setheading(90)
    def movement(self):
        self.goto(STARTING_POSITION)
    def move_forward(self):
        self.forward(MOVE_DISTANCE)
