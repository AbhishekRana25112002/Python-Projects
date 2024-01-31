UP=90
DOWN=270
LEFT=180
RIGHT=0


from turtle import Screen,Turtle
class Snake():
    def __init__(self):
        self.turtles = []
        self.index=3
        self.directions = [(0, 0), (-20, 0), (-40, 0),]
        self.make_snake()
    def make_snake(self):
        for i in range(3):
            t = Turtle("square")
            t.color("yellow")
            t.penup()
            self.turtles.append(t)
            t.goto(self.directions[i])
    def extend(self):
        self.turtles.append(Turtle("square"))
        self.turtles[self.index].color("white")
        self.turtles[self.index].penup()
        self.index+=1
    def move(self):
        for tim in range(len(self.turtles) - 1, 0, -1):
            x = self.turtles[tim - 1].xcor()
            y = self.turtles[tim - 1].ycor()
            self.turtles[tim].goto(x, y)
        self.turtles[0].forward(20)
    def moveup(self):
        if self.turtles[0].heading()!=DOWN:
            self.turtles[0].setheading(90)
    def movedown(self):
        if self.turtles[0].heading() != UP:
            self.turtles[0].setheading(270)
    def moveleft(self):
        if self.turtles[0].heading() != RIGHT:
            self.turtles[0].setheading(180)
    def moveright(self):
        if self.turtles[0].heading() != LEFT:
            self.turtles[0].setheading(0)
