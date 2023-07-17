from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class ScoreBord(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x_pos, 250)
        self.color("white")
        self.score = 0
        self.count_score()

    def count_score(self):
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)
