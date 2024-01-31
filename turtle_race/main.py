from turtle import Turtle,Screen
from random import choice,randint
color=["blue","green","red","black","orange"]
turtles=[]

for i in range(5):
    tim=Turtle("turtle")
    tim.penup()
    tim.color(color[i])
    turtles.append(tim)

screen=Screen()
screen.setup(width=500,height=400)

bet=screen.textinput("Make your bet","Which turtle will win the race? ")
y_pos=[30,60,0,-30,-60]
distance=randint(0,10)
i=0
for turtle in turtles:
    turtle.goto(-230,y_pos[i])
    i+=1
is_race_on=True
while is_race_on:
    for tim in turtles:
        if tim.xcor()>230:
            is_race_on=False
            winner=tim.pencolor()
        tim.forward(randint(0,10))
if bet==winner:
    print("You won the bet")
else:
    print("You lost the bet")
print("Winner is",winner)

screen.exitonclick()