from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0,290)
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}",font=("Courier", 16, "normal")
)
