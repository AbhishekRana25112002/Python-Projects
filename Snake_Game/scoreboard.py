from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()

        self.goto(-10,260)
        self.hideturtle()
        self.pscore()
    def increase_score(self):
        self.score+=1
        self.clear()
        self.pscore()
    def pscore(self):
        self.goto(-10,260)

        self.write(f"Score: {self.score} ", "center",font=("Arial",18,"normal"))
    def game_over(self):
        self.goto(-70,0)
        self.write("GAME OVER ", "center",font=("Arial",24,"normal"))
