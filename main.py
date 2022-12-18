from turtle import Screen, Turtle
from paddle import Paddle


screen = Screen()
screen.bgcolor("black")
screen.setup(width=700, height=700)
screen.title("PONG GAME")
screen.tracer(0)

l_paddle = Paddle(330, 0)
r_paddle = Paddle(-330, 0)




screen.listen()
screen.onkey(l_paddle.up, "o")
screen.onkey(l_paddle.down, "l")
screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")


game_is__on = True
while game_is__on:
    screen.update()

screen.exitonclick()