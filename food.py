from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        """
            Inherits from class turtle,
            creating food object.
        """
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color('green')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """
            Create a new food randomly.
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
