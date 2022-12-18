from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Verdana", 25, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_paddle_l = 0
        self.score_paddle_r = 0
        self.hideturtle()
        self.goto(0,270)
        self.color("white")
        self.write("0 - 0 ", align=ALIGNMENT, font=FONT)

    def increse_score_paddle_l(self):
        self.clear()
        self.score_paddle_l += 1
        self.write(f"{self.score_paddle_l} - {self.score_paddle_r} ", align=ALIGNMENT, font=FONT)

    def increse_score_paddle_r(self):
        self.clear()
        self.score_paddle_r += 1
        self.write(f"{self.score_paddle_l}  - {self.score_paddle_r} ", align=ALIGNMENT, font=FONT)

    def get_left_score(self):
        return self.score_paddle_l
    
    def get_rigth_score(self):
        return self.score_paddle_r