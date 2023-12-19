from turtle import Turtle, Screen
from board import Board
from ball import Ball
from game_platform import Platform
import time

my_board = Board(1000, 500)

red_platform = Platform((my_board.screen.screensize()[0] / 2) - 60, 'Up', 'Down', my_board)
red_platform.platform_move()

blue_platform = Platform((-my_board.screen.screensize()[0] / 2) + 60, 'w', 's', my_board)
blue_platform.platform_move()

my_ball = Ball(my_board, [red_platform, blue_platform])

while True:
    time.sleep(0.05)
    my_ball.ball_move()
    my_ball.ball_colistion()

# score_board.screen.mainloop()
