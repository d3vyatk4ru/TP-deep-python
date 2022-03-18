import unittest

from tictactoe import TicTacGame

class TestGameMethods(unittest.TestCase):

    def test_bad_validate_input(self):

        game = TicTacGame()

        self.assertTupleEqual(game._validate_input("a b"), (False, None, None))

    def test_good_validate_input(self):

        game = TicTacGame()

        self.assertTupleEqual(game._validate_input("1 2".split()), (True, 0, 1))

    def test_check_winner_in_init(self):

        game = TicTacGame()

        self.assertEqual(game._check_winner(), False)

    def test_check_winner_diag(self):
        
        game = TicTacGame()

        for i in range(3):
            game.board[i][i] = 'O'

        game.board[0][1] = 'X'
        game.board[0][2] = 'X'

        self.assertEqual(game._check_winner(), True)

    def test_check_winner_col(self):
        
        game = TicTacGame()

        for i in range(3):
            game.board[i][1] = 'O'

        game.board[1][2] = 'X'
        game.board[0][2] = 'X'

        self.assertEqual(game._check_winner(), True)

    def test_check_winner_raw(self):
        
        game = TicTacGame()

        for i in range(3):
            game.board[2][i] = 'O'

        game.board[1][2] = 'X'
        game.board[0][2] = 'X'

        self.assertEqual(game._check_winner(), True)

    def test_check_winner_inverse(self):

        game = TicTacGame()

        for i in range(3):
            game.board[i][3 - i - 1] = 'O'

        game.board[2][1] = 'X'
        game.board[2][2] = 'X'

        self.assertEqual(game._check_winner(), True)

    def test_check_winner_with_one_empty_raw(self):

        game = TicTacGame()

        game.board[0][0] = "O"
        game.board[0][1] = "X"
        game.board[0][2] = "O"
        game.board[1][0] = "X"
        game.board[1][1] = "O"   
        game.board[1][2] = "X"

        self.assertEqual(game._check_winner(), False)

    def test_check_winner_with_one_empty_col(self):

        game = TicTacGame()

        game.board[0][0] = "O"
        game.board[1][0] = "X"
        game.board[2][0] = "O"
        game.board[0][1] = "X"
        game.board[1][1] = "O"   
        game.board[2][1] = "X"

        self.assertEqual(game._check_winner(), False)

if __name__ == "__main__":

    unittest.main()