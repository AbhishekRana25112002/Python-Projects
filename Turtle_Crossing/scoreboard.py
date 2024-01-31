FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-270,240)
        self.write(f"Level: {self.level}", "center", font=("Courier", 20, "normal"))
    def new_level(self):
        self.clear()
        self.level+=1
        self.goto(-270, 240)
        self.write(f"Level:{self.level}", "center", font=("Courier", 20, "normal"))