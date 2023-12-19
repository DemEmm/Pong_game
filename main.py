from board import Board
from ball import Ball
from game_platform import Platform
import time

battle_frame_size_x = 1000
battle_frame_size_y = 500
my_board = Board(battle_frame_size_x, battle_frame_size_y)

red_platform = Platform((battle_frame_size_x / 2) - 60, 'Up', 'Down', 'red',[+100, battle_frame_size_y / 2 + 10], my_board)
red_platform.platform_move()

blue_platform = Platform((-battle_frame_size_x / 2) + 60, 'w', 's', 'blue',[-100, battle_frame_size_y / 2 + 10], my_board)
blue_platform.platform_move()

my_ball = Ball(my_board, [red_platform, blue_platform])

while True:
    time.sleep(0.05)
    my_ball.ball_move()
    my_ball.ball_colistion()

# score_board.screen.mainloop()
