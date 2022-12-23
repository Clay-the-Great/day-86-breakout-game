from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(45)
        self.speed("fastest")
        self.goto(0, -230)

    def move(self, x_move_distance, y_move_distance):
        new_x = self.xcor() + x_move_distance
        new_y = self.ycor() + y_move_distance
        self.goto(new_x, new_y)
