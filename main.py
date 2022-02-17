from turtle import Screen
from ball import Ball
from paddle import Paddle
from bricks import Brick
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=650, height=800)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

ball = Ball()
paddle = Paddle()
panel = Brick()
scoreboard = Scoreboard()
bricks = []

def create_rows():
    x_start = -260
    for i in range(7):
        block = Brick()
        block.color("green")
        block.goto(x_start, 225)
        x_start += 85
        bricks.append(block)
    x_start = -260
    for i in range(7):
        block = Brick()
        block.color("yellow")
        block.goto(x_start, 250)
        x_start += 85
        bricks.append(block)
    x_start = -260
    for i in range(7):
        block = Brick()
        block.color("orange")
        block.goto(x_start, 275)
        x_start += 85
        bricks.append(block)
    x_start = -260
    for i in range(7):
        block = Brick()
        block.color("red")
        block.goto(x_start, 300)
        x_start += 85
        bricks.append(block)

create_rows()

screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

game_running = True

while game_running:
    time.sleep(0.05)
    screen.update()
    ball.move()
    if ball.xcor() > 305 or ball.xcor() < -305:
        ball.wall_bounce()
    if ball.ycor() > 290:
        ball.reverse()
    if ball.distance(paddle) < 45:
        ball.reverse()
    if ball.ycor() < -380:
        ball.reset_position()
        scoreboard.lose_life()
    for brick in bricks:
        if ball.distance(brick) < 45:
            ball.reverse()
            brick.hideturtle()
            bricks.remove(brick)
            scoreboard.update_score()
    if len(bricks) == 0:
        ball.reset_position()
        ball.move_speed = 0
        scoreboard.win()
    if scoreboard.lives == 0:
        ball.reset_position()
        ball.move_speed = 0
        scoreboard.game_over()


screen.exitonclick()