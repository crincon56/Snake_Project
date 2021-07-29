# Importa funcion Turtle de modulo turtle.
from turtle import Turtle
# Importa modulo random.
import random

# Crea objeto de comida.
class Food(Turtle):

    def __init__(self):
        """
            Hereda de la funcion Turtle,
            creando objeto de comida.
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
            Crea una nueva comida al azar,
            sobre la pantalla.
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
