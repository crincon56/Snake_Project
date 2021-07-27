from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
# Grades for movement.
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
            Create the snake using the cardinal points
            indicated in the variable = STARTING_POSITIONS.
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """
            Create the body of the snake.
        """
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
            Move the parts of the snake using the length of the segments
            starting from the last position -1,
            as coordinates stored in the variables new_x and new_y.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
            The snake moves upwards,
            if it is at 90° it cannot go down to 270°.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
            The snake moves down,
            if it is at 270° it cannot go up 90°.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
            The snake moves to the left,
            if it is at 180° it cannot move 0°.
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
            The snake moves to the right,
            if it is at 0° it cannot move 180°.
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
