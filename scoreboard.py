from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.show_stats()

    def show_stats(self):
        self.clear()
        self.goto(-290, 325)
        self.write(f"Score: {self.score}", align="left", font=("Arial", 36, "normal"))
        self.goto(280, 325)
        self.write(f"Lives: {self.lives}", align="right", font=("Arial", 36, "normal"))

    def update_score(self):
        self.score += 1
        self.show_stats()

    def lose_life(self):
        self.lives -= 1
        self.show_stats()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 48, "normal"))

    def win(self):
        self.goto(0, 0)
        self.write("You win!", align="center", font=("Arial", 48, "normal"))