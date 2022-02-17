from turtle import Turtle

class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.penup()

    def create_rows(self):
        x_start = -260
        for i in range(7):
            block = Brick()
            block.color("green")
            block.goto(x_start, 275)
            x_start += 85
        x_start = -260
        for i in range(7):
            block = Brick()
            block.color("yellow")
            block.goto(x_start, 300)
            x_start += 85
        x_start = -260
        for i in range(7):
            block = Brick()
            block.color("orange")
            block.goto(x_start, 325)
            x_start += 85
        x_start = -260
        for i in range(7):
            block = Brick()
            block.color("red")
            block.goto(x_start, 350)
            x_start += 85
