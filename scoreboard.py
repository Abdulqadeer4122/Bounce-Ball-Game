from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(position)
        self.write(self.score, align="center", font=("arial", 24, "normal"))



    def score_update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("arial", 24, "normal"))
