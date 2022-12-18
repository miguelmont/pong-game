from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_is_on = True
screen = Screen()
screen.bgcolor("black")
screen.setup(width=700, height=600)
screen.title("PONG GAME")
screen.tracer(0)
speed= 0.1
l_paddle = Paddle(330, 0)
r_paddle = Paddle(-330, 0)

ball = Ball()

score_board = Scoreboard()
winner_board = Turtle()



screen.listen()
screen.onkey(l_paddle.up, "o")
screen.onkey(l_paddle.down, "l")
screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")
screen.onkey(lambda: globals().update(game_is_on=False), "q")


def determine_winner():
    if score_board.get_left_score() == 10:
        winner_board.hideturtle()
        winner_board.goto(0,100)
        winner_board.color("white")
        winner_board.write("The Winner Is Left Paddle", align="center", font=("Verdana", 35, "bold"))
        ball.gameover()
        l_paddle.reset()
        r_paddle.reset()
    elif score_board.get_rigth_score() == 10:
        winner_board.hideturtle()
        winner_board.goto(0,100)
        winner_board.color("white")
        winner_board.write("The Winner Is Right Paddle", align="center", font=("Verdana", 35, "bold"))
        ball.gameover()
        l_paddle.reset()
        r_paddle.reset()



while game_is_on:
    time.sleep(speed)
    screen.update()
    
    ball.move()
    #print(f"cordenada x: {ball.xcor()}")
    #print(f"distancia paddle izquierdo: {ball.distance(l_paddle)}")
    #print(f"distancia paddle derecho: {ball.distance(r_paddle)}")
    if ball.ycor() in (280, -280):
        ball.bounce_y()
    elif (ball.xcor() > 320 and ball.distance(l_paddle) < 60) or (ball.xcor() < -320 and ball.distance(r_paddle) < 60):
        ball.bounce_x()
        speed -= 0.002
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.increse_score_paddle_l()
    elif ball.xcor() < -380:
        ball.reset_position()
        score_board.increse_score_paddle_r()
    determine_winner()

