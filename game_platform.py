from turtle import Turtle


class Platform(Turtle):
    def __init__(self, x_pos, kay_1, kay_2, color, score_pos, game_board):
        super().__init__()
        self.x_pos = x_pos
        self.kay_1 = kay_1
        self.kay_2 = kay_2
        self.plt_color = color
        self.score_pos = score_pos
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color(self.plt_color)
        self.setpos(score_pos)

        self.write(f"{self.score}", False, 'center', ("courier", 20, "bold"))
        self.game_board = game_board
        self.platform_piece = []
        self.platform_struct = [[x_pos, 0], [x_pos, 10], [x_pos, 20], [x_pos, 30], [x_pos, 40]]
        for piece in range(0, len(self.platform_struct)):
            self.platform_piece.append(Turtle())
            self.platform_piece[piece].penup()
            self.platform_piece[piece].color(self.plt_color)
            self.platform_piece[piece].shape('square')
            self.platform_piece[piece].setposition(self.platform_struct[piece])
            # self.platform_piece[piece].color('white')

    def platform_move(self):
        def move_up():
            for piece in self.platform_piece:
                piece.setpos(piece.pos()[0], piece.pos()[1] + 20)
            self.game_board.screen.update()

        def move_down():
            for piece in self.platform_piece:
                piece.setpos(piece.pos()[0], piece.pos()[1] - 20)
            self.game_board.screen.update()

        self.screen.onkeypress(move_up, self.kay_1)
        self.screen.onkeypress(move_down, self.kay_2)

    def score_update(self):
        self.clear()
        self.write(f"{self.score}", False, 'center', ("courier", 20, "bold"))
        self.screen.update()
