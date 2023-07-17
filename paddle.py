from turtle import Turtle
import time

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 5)
        self.setheading(90)
        self.color("white")
        self.penup()
        self.goto(position)
        self.speed("fastest")

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)