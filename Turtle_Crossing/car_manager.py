COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.generate_cars()



    def generate_cars(self):
        self.shape("square")
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)

        self.goto(random.randint(310, 1500), random.randint(-200, 250))
    def car_move(self):
        self.forward(5)
    def regenerate_cars(self):
        if self.xcor()<-300:
            self.goto(random.randint(310, 1500), random.randint(-250, 250))
