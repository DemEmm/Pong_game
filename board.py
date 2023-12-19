from turtle import Turtle, Screen


class Board(Turtle):
    def __init__(self, size_x, size_y):
        super().__init__()
        self.size_x = size_x
        self.size_y = size_y
        self.screen.screensize(self.size_x, self.size_y)
        self.screen.setup(self.size_x + 100, self.size_y + 100)
        self.screen.bgcolor("black")

        # create arena
        self.penup()
        self.color('white')
        self.setpos(-size_x / 2, size_y / 2)
        self.pendown()
        self.forward(size_x)
        self.right(90)
        self.forward(size_y)
        self.right(90)
        self.forward(size_x)
        self.right(90)
        self.forward(size_y)
        self.hideturtle()

        self.screen.tracer(0)
        self.screen.listen()
