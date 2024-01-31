from turtle import Turtle
import random
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lscore=0
        self.rscore=0
        self.penup()
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.lscore}", "center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(f"{self.rscore}", "center", font=("Courier", 80, "normal"))
    def l(self):
        self.lscore+=1
        self.update_scoreboard()
    def r(self):
        self.rscore+=1
        self.update_scoreboard()
    def game_over(self):
        self.goto(-100,0)
        self.write("GAME OVER", "center", font=("Courier", 40, "normal"))