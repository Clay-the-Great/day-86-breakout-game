from turtle import Turtle


class Brick(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color("white")
        self.speed("fastest")
        self.goto(x, y)
        self.visible = True

    def disappear(self):
        self.hideturtle()
        self.visible = False
