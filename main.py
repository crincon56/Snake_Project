# Importa funcion Screen de la libreria turtle y los modulos que creados previamente.
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Crea pantalla en pixeles.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

# Se renombran funciones
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Control de la serpiente.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Activa el juego
game_is_on = True

# Mueve la serpiente.
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecta colision con la comida.
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detecta colision con la pared.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detecta colision con la cola.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# Cierra pantalla.
screen.exitonclick()
