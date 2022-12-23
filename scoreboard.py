from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.life_number = 3
        self.brick_number = 30
        self.display()

    def decrease_life(self):
        self.life_number -= 1
        self.display()

    def decrease_brick(self):
        self.brick_number -= 1
        self.display()

    def victory(self):
        self.clear()
        self.goto(-160, 260)
        self.write("You Win! Press 'r' to reset, and then 'space' to start again.", font=("Courior", 10, "normal"))

    def defeat(self):
        self.clear()
        self.goto(-160, 260)
        self.write("You Lose! Press 'r' to reset, and then 'space' to start again.", font=("Courior", 10, "normal"))

    def display(self):
        self.clear()
        self.goto(-160, 260)
        self.write(f"Lives Remaining: {self.life_number}, Bricks Remaining: {self.brick_number}. "
                   f"Press 'space' to begin",
                   font=("Courior", 10, "normal"))
