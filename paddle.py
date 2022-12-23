from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.setheading(0)
        self.color("white")
        self.speed("fastest")
        self.goto(0, -250)

    def move_left(self):
        if self.xcor() >= -360:
            self.setheading(180)
            self.forward(30)

    def move_right(self):
        if self.xcor() <= 360:
            self.setheading(0)
            self.forward(30)
