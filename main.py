from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


def pass_wall(xy_cord):
    shift = abs(xy_cord) - 20
    if abs(xy_cord) == xy_cord:
        shift = shift * (-1)
    return shift


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
snake_speed = 0.1
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(snake_speed)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        score_board.increase_score()
        snake.extend()
        food.refresh()
        snake_speed -= 0.0005

    # Detect collision with wall.
    x_cord = snake.head.xcor()
    if x_cord > 280 or x_cord < -280:
        shift_value = pass_wall(x_cord)
        snake.head.setx(shift_value)

    y_cord = snake.head.ycor()
    if y_cord > 280 or y_cord < -280:
        shift_value = pass_wall(y_cord)
        snake.head.sety(shift_value)

    # Detect collision with tail.
    for segment in snake.segments_list[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()
    # if head collides with any segment in the tail:
    # trigger game_over

screen.exitonclick()
