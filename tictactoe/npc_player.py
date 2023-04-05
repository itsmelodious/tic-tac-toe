from typing import Tuple
from player import Player
from board import Board
import random


class NpcPlayer(Player):

    def select_square(self, board: Board) -> Tuple[int, int]:
        open_squares = []
        # Convert each (r,c) into 1d equivalent (call it k)
        for r in range(board.get_size()):
            for c in range(board.get_size()):
                # Add k for all open boxes to list
                if board.is_open(r, c):
                    open_squares.append(3 * r + c)
        print("open squares: ", open_squares)
        # Randomly pick one k
        cpu_move: int = random.choice(open_squares)
        # Convert k back to r,c
        cpu_move_r, cpu_move_c = cpu_move // 3, cpu_move % 3
        return (cpu_move_r, cpu_move_c)
