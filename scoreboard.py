from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        """
            Inherits from class turtle,
            creating scoreboard object.
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
            Updates the table,
            clearing the score in the object.
        """
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
            Show a game over text.
        """
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
            Increase the punctuation
            on the object scoreboard.
        """
        self.score += 1
        self.clear()
        self.update_scoreboard()
