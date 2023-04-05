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

    def is_open(self, row: int, col: int) -> bool:
        if self.is_inbounds(row, col):
            return self._grid[row][col] == " "
        print(f"({row}, {col}) - Error: out of bounds.")
        return False

    # Returns True if grid is updated successfully.
    def update(self, row: int, col: int, val: str) -> bool:
        if self.is_open(row, col):
            self._grid[row][col] = val
            return True
        else:
            print(f"({row}, {col}) - Invalid square: please select an open square.")
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

    def main():
        b = Board(3)
        b.update(1, 1, "X")
        b.update(0, 1, "O")
        b.update(0, 0, "X")
        b.update(2, 2, "O")
        b.update(2, 1, "O")
        b.print_grid()
        b.update(2, 1, "X")
        b.print_grid()


if __name__ == "__main__":
    Board.main()
