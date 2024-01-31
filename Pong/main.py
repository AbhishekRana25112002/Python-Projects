from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(800,600)
screen.bgcolor("orange")

screen.title("Pong")
screen.tracer(0)
score=Scoreboard()


r_paddle=Paddle()
l_paddle=Paddle()
l_paddle.goto(-360, 0)
t_points=screen.numinput("Welcome to the PONG Game","Input the total no of points")

screen.listen()
screen.onkey(r_paddle.go_up, "8")
screen.onkey(r_paddle.go_down, "5")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball=Ball()

game_on=True

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()

    if ball.distance(r_paddle)<50 and ball.xcor()>340 or ball.distance(l_paddle)<50 and ball.xcor()<-340:
        ball.bounce_paddle()
    if ball.xcor()>390:
        ball.reset()
        score.l()
    if ball.xcor()<-399:
        ball.reset()
        score.r()
    if score.lscore==t_points or score.rscore==t_points:
        game_on=False
        score.game_over()
screen.exitonclick()