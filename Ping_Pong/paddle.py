from turtle import Turtle,Screen

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(x,y)
        self.shapesize(5,1)


    def move_up(self):
        y=self.ycor()
        if y<250:
            self.sety(y+20)

    def move_down(self):
        y=self.ycor()
        if y>-240:
            self.sety(y-20)




