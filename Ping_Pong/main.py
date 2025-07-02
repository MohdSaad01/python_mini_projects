from turtle import Turtle, Screen
import paddle
import ball
import scoreboard
import time

screen=Screen()
screen.setup(800,600)
screen.bgcolor("blue")
screen.title("Ping Pong")
screen.tracer(0)

middle_line=Turtle()
middle_line.penup()
middle_line.color("white")
middle_line.shape("square")
middle_line.shapesize(30,1)

ball=ball.Ball()
l_paddle=paddle.Paddle(-350,0)
r_paddle=paddle.Paddle(350,0)

screen = Screen()
screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

score=scoreboard.Score()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    if ball.distance(r_paddle)<60 and ball.xcor()>320 or ball.distance(l_paddle)<60 and ball.xcor()<-320:
        ball.x_bounce()

    if ball.xcor()>380:
        ball.reset_ball()
        score.l_points()


    if ball.xcor()<-380:
        ball.reset_ball()
        score.r_points()