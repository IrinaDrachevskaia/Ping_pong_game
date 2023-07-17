from turtle import Turtle
import random
import time
ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1, 1)
        self.color("white")
        self.penup()
        self.reset_position()
        self.move_speed = 0.1

    def move(self):
        self.forward(20)

    def change_direction(self, minus_angel):
        angle = minus_angel - self.heading()
        self.setheading(angle)
        self.move()


    def game_over(self):
        self.goto(0, 0)
        self.write("Game over.", align=ALIGNMENT, font=FONT)

    def reset_position(self):
        self.goto(0, 0)
        heading = random.randint(-50, 50)
        self.setheading(heading)
        self.move_speed = 0.1
