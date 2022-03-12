from turtle import Turtle
from random import choice

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_DIRECTION = choice([UP, DOWN, RIGHT])

class Snake:

    def __init__(self):
        self.segments_list = []
        self.create_snake()
        self.head = self.segments_list[0]
        self.customize_head()
        self.direction = STARTING_DIRECTION

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def customize_head(self):
        self.head.color("red")
        self.head.shape("circle")
        self.head.shapesize(0.9, 0.9)

    def add_segment(self, position):
        snake_segment = Turtle("square")
        snake_segment.color("green")
        snake_segment.penup()
        snake_segment.shapesize(0.8, 0.8)
        snake_segment.goto(position)
        self.segments_list.append(snake_segment)

    def extend(self):
        # Add a new segment to snake
        self.add_segment(self.segments_list[-1].position())

    def move(self):
        self.direction = False
        for seg_num in range(len(self.segments_list) - 1, 0, -1):
            new_x = self.segments_list[seg_num - 1].xcor()
            new_y = self.segments_list[seg_num - 1].ycor()
            self.segments_list[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.direction = self.head.heading()

    def up(self):
        if self.direction != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.direction != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.direction != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.direction != LEFT:
            self.head.setheading(RIGHT)

