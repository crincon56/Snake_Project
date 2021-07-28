from turtle import Turtle

# Puntos cardinales para la base del cuerpo.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# Cantidad de pixeles en cada cuadro de la serpiente.
MOVE_DISTANCE = 20
# Grados de movimiento.
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
            Crea la serpiente usando los puntos cardinales.
            indicado en la variable = STARTING_POSITIONS.
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """
            Crea el cuerpo de la serpiente.
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
            mueve las partes de la serpiente usando la longitud de los segmentos
            a partir de la última posición -1,
            como coordenadas almacenadas en las variables new_x and new_y.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
            La serpiente se mueve hacia arriba
            si está a 90° no puede bajar a 270°.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
            La serpiente se mueve hacia abajo
            si está a 270° no puede subir 90°.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
            La serpiente se mueve hacia la izquierda
            si está a 180° no puede moverse 0°.
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
            La serpiente se mueve hacia la derecha
            si está a 0° no puede moverse 180°.
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
