import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
tim=Player()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(tim.move_forward,"Up")
screen.onkey(tim.move_back,"Down")
screen.onkey(tim.move_left,"Left")
screen.onkey(tim.move_right,"Right")

cars = []
for i in range(60):
    cars.append(CarManager())
game_is_on = True
s=0.1
while game_is_on:
    time.sleep(s)
    screen.update()
    for i in range(60):
        cars[i].car_move()
        cars[i].regenerate_cars()
        if tim.distance(cars[i])<20:
            game_is_on=False
    if tim.ycor()>300:
        tim.change_level()
        scoreboard.new_level()
        s*=0.5

screen.exitonclick()