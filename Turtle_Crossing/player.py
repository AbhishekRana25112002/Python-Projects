STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
    def move_forward(self):
        self.forward(MOVE_DISTANCE)
    def change_level(self):
        self.goto(STARTING_POSITION)
    def move_back(self):
        self.backward(MOVE_DISTANCE)
    def move_left(self):
        if self.xcor()>-280:
            self.setheading(180)
            self.forward(MOVE_DISTANCE)
            self.setheading(90)

    def move_right(self):
        if self.xcor()<280:

            self.setheading(0)
            self.forward(MOVE_DISTANCE)
            self.setheading(90)
