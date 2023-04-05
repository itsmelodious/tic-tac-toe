from typing import List


class Board:
    def __init__(self, s: int):
        self._size = s
        self._grid: List[List[str]] = [[" "] * s for _ in range(s)]

    def _is_open(self, row: int, col: int) -> bool:
        if row >= 0 and row < self._size and col >= 0 and col < self._size:
            return self._grid[row][col] == " "
        return False

    def update(self, row: int, col: int, val: str) -> str:
        if self._is_open(row, col):
            self._grid[row][col] = val
            return str(self._grid)
        else:
            return "Please provide a valid (row, column) entry, e.g. (1,a)."

    def get_size(self) -> int:
        return self._size

    def print_grid(self):
        lines = []
        for row in self._grid:
            lines.append('|'.join(f' {str(x)} ' for x in row))
            lines.append('---+' * len(row))
        print('\n'.join(lines))

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
        # b.update(1, 1, "X")
        # b.update(0, 1, "O")
        # b.update(0, 0, "X")
        # b.update(2, 2, "O")
        # b.update(2, 1, "O")
        # b.print_grid()


if __name__ == "__main__":
    Board.main()
