import turtle
import pandas
screen=turtle.Screen()
screen.title("US States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
text=turtle.Turtle()
text.penup()
text.hideturtle()
data=pandas.read_csv("50_states.csv")
states=pandas.Series(data.state)

def locate(str):

    x=int(data[data["state"]==str].x)
    y=int(data[data["state"]==str].y)

    text.goto(x,y)
    text.write(str, "center")
states=list(states)
n=0
while n<50:
    user_answer=screen.textinput(f"{n}/50 US states guessed","Guess a US State").title()
    if user_answer in states:
        n+=1
        locate(user_answer)
    if user_answer=="Exit":
        break
