from turtle import Turtle, Screen


class Ball(Turtle):
    def __init__(self, game_board, game_platformes):
        super().__init__()
        self.game_platforms = game_platformes
        self.game_board = game_board
        self.color('white')
        self.shape('circle')
        self.penup()
        self.diraction_x = 10
        self.diraction_y = 10
        # self.right(45)

    def ball_move(self):

        self.setpos(self.pos()[0] + self.diraction_x, self.pos()[1] + self.diraction_y)
        self.game_board.screen.update()

    def ball_colistion(self):
        # if collide with red platform
        for piece in self.game_platforms[0].platform_piece:
            if self.position()[0] + 10 == piece.pos()[0] and self.position()[1] == piece.pos()[1]:
                self.diraction_x = -self.diraction_x
        # if collide with blue platform
        for piece in self.game_platforms[1].platform_piece:
            if self.position()[0] - 10 == piece.pos()[0] and self.position()[1] == piece.pos()[1]:
                self.diraction_x = -self.diraction_x
        # if collide with walls
        screensize = self.game_board.screen.screensize()
        if self.position()[1] == (screensize[1] / 2) - 10 or self.position()[1] == -(screensize[1] / 2) + 10:
            self.diraction_y = -self.diraction_y
