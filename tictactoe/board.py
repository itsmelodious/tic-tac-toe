from typing import List


class Board:

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    def __init__(self, s: int):
        self._size = s
        self._grid: List[List[str]] = [[" "] * s for _ in range(s)]

    def is_inbounds(self, row: int, col: int) -> bool:
        return row >= 0 and row < self._size and col >= 0 and col < self._size

    def _is_open(self, row: int, col: int) -> bool:
        if self.is_inbounds(row, col):
            return self._grid[row][col] == " "
        print("Error: out of bounds.")
        return False

    # Returns True if grid is updated successfully.
    def update(self, row: int, col: int, val: str) -> bool:
        if self._is_open(row, col):
            self._grid[row][col] = val
            return True
        else:
            print("Invalid square: please select an open square.")
            return False

    def get_size(self) -> int:
        return self._size

    def get_grid(self) -> List[List[str]]:
        return self._grid

    def print_grid(self):
        lines = []
        for row_i, row in enumerate(self._grid):
            lines.append('|'.join(f' {str(x)} ' for x in row))
            if row_i // 2 != 1:
                lines.append('---+' * len(row))
        print('\n'.join(lines))
        print('\n')

        # # print column characters on top
        # columns = [chr(ord("a") + i) for i in range(self._size)]
        # print('   ', '   '.join([str(val) for val in columns]))

        # row_separator = f'  +{"---+" * len(columns)}'

        # for i_row, rows in enumerate(self._grid):
        #     print(row_separator)
        #     # print row number
        #     print(i_row, end="")

        #     for r in rows:
        #         print(f' | {r} |')
        #     # # depending on location of X, either print a row including X or an empty row
        #     # if i_row == x_loc[0]:
        #     #     print(
        #     #         f' |{"   |" * (x_loc[1])} {x_symbol} |{"   |" * (len(columns)-x_loc[1]-1)}')
        #     # else:
        #     #     print(f' |{"   |" * len(columns)}')
        #     # print closing row separator
        #     print(row_separator)

    def main():
        b = Board(3)
        b.update(1, 1, "X")
        b.update(0, 1, "O")
        b.update(0, 0, "X")
        b.update(2, 2, "O")
        b.update(2, 1, "O")
        b.update(2, 1, "X")
        b.print_grid()


if __name__ == "__main__":
    Board.main()
