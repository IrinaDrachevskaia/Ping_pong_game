from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBord
import time

screen = Screen()
ball = Ball()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

l_scoreboard = ScoreBord(-50)
r_scoreboard = ScoreBord(50)

screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

t = 0.1

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    #detect a colision with a wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_direction(360)

    #detect a colision with a paddle
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.change_direction(180)
        ball.move_speed *= 0.9
        # time.sleep(ball.move_speed)

    elif ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.change_direction(180)
        ball.move_speed *= 0.9
        # time.sleep(ball.move_speed)

    #Defect R paddle misses
    elif ball.xcor() > 390:
        l_scoreboard.count_score()
        ball.reset_position()
        ball.setheading(ball.heading() + 180)

        if l_scoreboard.score == 15:
            game_is_on = False
            ball.game_over()
            l_scoreboard.update_score()

            # Defect L paddle misses
    elif ball.xcor() < -390:
        r_scoreboard.count_score()
        ball.reset_position()

        if r_scoreboard.score == 15:
            game_is_on = False
            ball.game_over()
            r_scoreboard.update_score()

#game_is_on = False
#ball.game_over()


screen.exitonclick()