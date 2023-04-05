from board import Board
from player import Player
from npc_player import NpcPlayer


class TicTacToe:

    def __init__(self):
        self.board = Board(3)
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
            while self.board.is_inbounds(new_row, new_col) and grid[new_row][new_col] == player.symbol and matches < 3:
                new_row += row_dir
                new_col += col_dir
                matches += 1
            if matches == 3:
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
