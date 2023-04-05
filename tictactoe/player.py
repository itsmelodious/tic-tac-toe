from typing import Optional, Tuple
from board import Board


class Player:
    def __init__(self, number: int, symbol: str):
        self.number = number
        self.symbol = symbol

    def select_square(self, board: Board) -> Optional[Tuple[int, int]]:
        input_successful = False
        board_size = board.get_size()
        while not input_successful:
            row_input = input(
                f"Select a row from 0 to {board_size - 1}, inclusive. The top-most row starts at 0. \n")
            col_input = input(
                f"Select a column from 0 to {board_size - 1}, inclusive. The left-most column starts at 0. \n")
            try:
                row_num = int(row_input)
                col_num = int(col_input)
                input_successful = True
                return (row_num, col_num)
            except ValueError:
                print("Invalid input. Please enter in a valid square number.")
