from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lScore = 0
        self.rScore = 0
        self.updateScore()

    def updateScore(self):
        self.goto(-100, 200)
        self.write(self.lScore, align="center", font=("Courier", 70, "normal"))
        self.goto(100, 200)
        self.write(self.rScore, align="center", font=("Courier", 70, "normal"))

    def lPoint(self):
        self.clear()
        self.lScore += 1
        self.updateScore()

    def rPoint(self):
        self.clear()
        self.rScore += 1
        self.updateScore()