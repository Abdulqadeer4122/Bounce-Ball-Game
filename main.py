from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
WIDTH = 800
HEIGHT = 600

sc = Screen()
sc.setup(WIDTH, HEIGHT)
sc.bgcolor("black")
sc.title("Bouncing Ball")
sc.tracer(0)

"""I am making the object of the paddle class to create two paddle one on the left side of the screen
and second on the right side of the screen"""
l_pd = Paddle((370, 0))
r_pd = Paddle((-370, 0))
ball = Ball()
l_score = ScoreBoard((80, 260))
r_score = ScoreBoard((-80, 260))


sc.listen()
sc.onkey(l_pd.go_up, "Up")
# My down button does not work so i used l
sc.onkey(l_pd.go_down, "l")

sc.onkey(r_pd.go_up, "w")
sc.onkey(r_pd.go_down, "s")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    sc.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(l_pd) < 70 and ball.xcor() > 340 or ball.distance(r_pd) < 70 and ball.xcor() < -340:
        ball.bounce_x()
    if ball.xcor() > 380:
        r_score.score_update()
        ball.reset_position()
    elif ball.xcor() < -380:
        ball.reset_position()
        l_score.score_update()



sc.exitonclick()
