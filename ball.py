from turtle import Turtle


class Ball(Turtle):
    def __init__(self, game_board, game_platformes):
        super().__init__()
        self.game_platforms = game_platformes
        self.game_board = game_board
        self.color('white')
        self.shape('circle')
        self.penup()
        self.direction_x = 10
        self.direction_y = 10

    def ball_move(self):

        self.setpos(self.pos()[0] + self.direction_x, self.pos()[1] + self.direction_y)
        self.game_board.screen.update()

    def ball_colistion(self):
        # if collides with red platform
        for piece in self.game_platforms[0].platform_piece:
            if self.position()[0] + 20 == piece.pos()[0] and self.position()[1] == piece.pos()[1]:
                self.direction_x = -self.direction_x
        # if collides with blue platform
        for piece in self.game_platforms[1].platform_piece:
            if self.position()[0] - 20 == piece.pos()[0] and self.position()[1] == piece.pos()[1]:
                self.direction_x = -self.direction_x
        # if collides with up and down wall
        screensize = self.game_board.screen.screensize()
        if self.position()[1] == (screensize[1] / 2) - 10 or self.position()[1] == -(screensize[1] / 2) + 10:
            self.direction_y = -self.direction_y

        if self.position()[0] > (screensize[0] / 2) - 20 or self.position()[0] < -(screensize[0] / 2) + 20:
            if self.direction_x > 0:
                self.game_platforms[1].score += 1
                self.game_platforms[1].score_update()
            elif self.direction_x < 0:
                self.game_platforms[0].score += 1
                self.game_platforms[0].score_update()
            self.direction_x = -self.direction_x
