from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(x=x, y=y)
        self.speed("fastest")

    def up(self):
        newY = self.ycor() + 30
        self.goto(x=self.xcor(), y=newY)

    def down(paddle):
        newY = paddle.ycor() - 30
        paddle.goto(x=paddle.xcor(), y=newY)