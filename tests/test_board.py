import unittest
from tictactoe import board


class TestBoard(unittest.TestCase):
    def test_update(self):
        b = board.Board(3)
        b.update(1, 1, "X")
        expected = [[' ', ' ', ' '],
                    [' ', 'X', ' '],
                    [' ', ' ', ' ']]
        actual = b.get_grid()
        self.assertEqual(actual, expected)

    def test_update_occupied(self):
        b = board.Board(3)
        b.update(1, 1, "X")
        b.update(1, 1, "O")
        expected = [[' ', ' ', ' '],
                    [' ', 'X', ' '],
                    [' ', ' ', ' ']]
        actual = b.get_grid()
        self.assertEqual(actual, expected)

    def test_update_out_of_bounds(self):
        b = board.Board(3)
        b.update(1, 1, "X")
        b.update(3, 1, "O")
        expected = [[' ', ' ', ' '],
                    [' ', 'X', ' '],
                    [' ', ' ', ' ']]
        actual = b.get_grid()
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
