from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

# Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Initializing
paddleLeft = Paddle(-350, 0)
paddleLeft.color("red")
paddleRight = Paddle(350, 0)
paddleRight.color("blue")
ball = Ball()
score = Scoreboard()

screen.listen()

# Listeners for the paddles up/down
screen.onkey(paddleRight.up, "Up")
screen.onkey(paddleRight.down, "Down")

screen.onkey(paddleLeft.up, "w")
screen.onkey(paddleLeft.down, "s")

gameOn = True
while gameOn:
    screen.update()
    ball.move()
    time.sleep(ball.moveSpeed)

    # Collision with wall up/down
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounceY()

    # Collision with paddle
    if ball.xcor() > 320 and ball.distance(paddleRight) < 50 or ball.distance(paddleLeft) < 50 and ball.xcor() < -320:
        ball.bounceX()

    # Collision with wall right
    if ball.xcor() > 380:
        ball.resetPosition()
        score.lPoint()
        score.updateScore()

    # Collision with wall left
    if ball.xcor() < -380:
        ball.resetPosition()
        score.rPoint()
        score.updateScore()

screen.exitonclick()