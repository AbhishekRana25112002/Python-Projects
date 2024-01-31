from turtle import Turtle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(5, 1)
        self.goto(360, 0)
    def go_up(self):
        y_pos = self.ycor() + 50
        self.goto(self.xcor(), y_pos)

    def go_down(self):
        y_pos = self.ycor() - 50
        self.goto(self.xcor(), y_pos)