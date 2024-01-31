from turtle import Screen
from scoreboard import Score
from food import Food
from snake import Snake
import time
score=Score()
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My snake game")
snake=Snake()
food=Food()
screen.tracer(0)
screen.listen()
screen.onkey(snake.moveup,"Up")
screen.onkey(snake.movedown,"Down")
screen.onkey(snake.moveleft,"Left")
screen.onkey(snake.moveright,"Right")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food:
    if snake.turtles[0].distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()
    #detect collision with the wall
    if snake.turtles[0].xcor()>280 or snake.turtles[0].xcor()<-280 or snake.turtles[0].ycor()>280 or snake.turtles[0].ycor()<-280 :
        game_is_on = False
        score.game_over()
    #detect collision with itself
    for segment in snake.turtles[1:]:
        if snake.turtles[0].distance(segment)<10:
            game_is_on=False
            score.game_over()
screen.exitonclick()