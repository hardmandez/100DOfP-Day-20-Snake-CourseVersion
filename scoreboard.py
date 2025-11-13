from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.score = 0
        self.refresh_score()



    def refresh_score(self):
        self.clear()
        self.score += 1
        self.write("Score = "str(self.score), True, align="left")
