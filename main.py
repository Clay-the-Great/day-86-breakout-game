from turtle import Turtle, Screen
from ball import Ball
import time
from paddle import Paddle
from brick import Brick
from scoreboard import Scoreboard

MOVE_DISTANCE = 10
x_move_distance = MOVE_DISTANCE
y_move_distance = MOVE_DISTANCE
delay_time = 0.05


def game():
    global game_on, x_move_distance, y_move_distance
    while game_on:

        time.sleep(delay_time)
        screen.update()
        ball.move(x_move_distance, y_move_distance)

        # collision with wall
        if ball.ycor() > 280:
            y_move_distance *= -1
        if ball.xcor() > 370 or ball.xcor() < -380:
            x_move_distance *= -1

        # collision with paddle
        if ball.distance(paddle) < 30 and ball.ycor() < -220:
            y_move_distance *= -1

        # collision with brick
        for brick in bricks:
            if ball.distance(brick) < 20 and brick.visible:
                # move_distance *= 1.01
                # x_move_distance = move_distance
                # y_move_distance = move_distance
                y_move_distance *= -1
                brick.disappear()
                scoreboard.decrease_brick()
                if scoreboard.brick_number == 0:
                    scoreboard.victory()
                    game_on = False

        # paddle missing ball
        if ball.ycor() <= -300:
            scoreboard.decrease_life()
            ball.goto(0, -230)
            x_move_distance = MOVE_DISTANCE
            y_move_distance = MOVE_DISTANCE
            if scoreboard.life_number == 0:
                scoreboard.defeat()
                game_on = False


def reset():
    global game_on, bricks
    game_on = True
    brick_positions = []
    bricks = []
    for i in range(3):
        for j in range(10):
            brick_positions.append([-320 + 70 * j, 230 - 50 * i])
    bricks = [Brick(position[0], position[1]) for position in brick_positions]
    # ball.goto(0, -230)
    scoreboard.life_number = 3
    scoreboard.brick_number = 30


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

ball = Ball()
paddle = Paddle()
bricks = []
scoreboard = Scoreboard()
reset()

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")
screen.onkey(game, "space")
screen.onkey(reset, "r")

game_on = True

# game()

screen.exitonclick()
