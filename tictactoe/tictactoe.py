from typing import List, Tuple
from board import Board
from player import Player
from npc_player import NpcPlayer


class TicTacToe:

    def __init__(self, size: int = 3):
        self.board = Board(size)
        self.p1 = Player(1, "X")
        self.p2 = NpcPlayer(2, "O")
        self._squares_filled: int = 0
        self._is_p1_turn: bool = True

    def is_game_over(self) -> bool:
        board_size = self.board.get_size() ** 2
        is_game_over = self._squares_filled == board_size
        if is_game_over:
            print("Game over! All the squares have been filled.")
        return is_game_over

    def play(self, player: Player, row: int, col: int) -> None:
        is_updated: bool = self.board.update(row, col, player.symbol)
        if not is_updated:
            print("Please provide a valid (row, column) entry.")
        else:
            self._squares_filled += 1
            self._is_p1_turn = not self._is_p1_turn
            self.board.print_grid()

    def is_winning_move(self, player: Player, row: int, col: int) -> bool:
        grid = self.board.get_grid()
        for direction in self.board.directions:
            row_dir, col_dir = direction
            new_row = row + row_dir
            new_col = col + col_dir
            matches = 1
            # continue checking the same direction and the opposite direction
            continue_checking: List[Tuple[int, int]] = [(new_row, new_col)]
            while continue_checking:
                n_row, n_col = continue_checking.pop()
                if self.board.is_inbounds(n_row, n_col) and \
                        grid[n_row][n_col] == player.symbol and \
                        matches < 3:
                    matches += 1
                    continue_checking.append(
                        (n_row + row_dir, n_col + col_dir))
                    continue_checking.append(
                        (row - row_dir, col - col_dir))
            if matches == 3:
                print("Game over!\n")
                print(f"Player {player.number} won!")
                return True
        return False

    def main():
        game = TicTacToe()
        while not game.is_game_over():
            if game._is_p1_turn:
                player = game.p1
            else:
                player = game.p2
            print(f"Player {player.number}'s turn.")
            game.board.print_grid()
            selected_square = player.select_square(game.board)
            if selected_square is not None:
                row = selected_square[0]
                col = selected_square[1]
                game.play(player, row, col)
                if game.is_winning_move(player, row, col):
                    break


if __name__ == "__main__":
    TicTacToe.main()
