import unittest

from tictactoe.tictactoe import TicTacToe


class TestBoard(unittest.TestCase):
    def test_is_game_over(self):
        g = TicTacToe()
        g.board.update(1, 1, "X")
        g.board.update(2, 0, "O")
        g.board.update(2, 1, "X")
        g.board.update(0, 1, "O")
        g.board.update(0, 0, "X")
        g.board.update(2, 2, "O")
        g.board.update(1, 0, "X")
        g.board.update(1, 2, "O")
        g.board.update(0, 2, "X")
        expected = True
        actual = g.is_game_over()
        self.assertEqual(actual, expected)

    def test_winning_move_middle(self):
        g = TicTacToe()
        g.play(g.p2, 2, 0)
        g.play(g.p2, 0, 0)
        self.assertEqual(g.is_winning_move(g.p2, 0, 0), False)
        g.play(g.p2, 1, 0)
        self.assertEqual(g.is_winning_move(g.p2, 1, 0), True)

    def test_winning_move_corner(self):
        g = TicTacToe()
        g.play(g.p1, 0, 0)
        g.play(g.p1, 0, 1)
        g.play(g.p1, 2, 0)
        g.play(g.p1, 1, 1)
        self.assertEqual(g.is_winning_move(g.p1, 1, 1), False)
        g.play(g.p1, 2, 2)
        self.assertEqual(g.is_winning_move(g.p1, 1, 0), True)


if __name__ == "__main__":
    unittest.main()
