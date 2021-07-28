from turtle import Turtle
ALIGNMENT = "center"
# Letra para puntos.
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        """
            Hereda de la funcion Turtle,
            creando objeto de marcador.
        """
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
            Actualiza la tabla.
        """
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
            Muestra game over sobre texto.
        """
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
            Aumenta la puntuación
            en el marcador de objetos,
            limpiando el puntaje anterior.
        """
        self.score += 1
        self.clear()
        self.update_scoreboard()
