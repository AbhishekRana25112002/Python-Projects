from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x=10
        self.y=10
        self.move_speed=0.09
    def move(self):
        x=self.xcor()+self.x
        y=self.ycor()+self.y
        self.goto(x,y)
    def bounce(self):
        self.y*=-1
    def bounce_paddle(self):
        self.x*=-1
        self.move_speed*=0.8
    def reset(self):
        self.goto(0,0)
        self.move_speed=0.08
        self.bounce_paddle()