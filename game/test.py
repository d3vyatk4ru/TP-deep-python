import unittest

from tictactoe import TicTacGame

class TestGameMethods(unittest.TestCase):

    def test_bad_validate_input_comma(self):

        game = TicTacGame()

        self.assertTupleEqual(game.validate_input("1,2".split()), (False, None, None))

    def test_bad_validate_input_under_line(self):

        game = TicTacGame()

        self.assertTupleEqual(game.validate_input("1_2".split()), (False, None, None))

    def test_bad_validate_input_dot(self):

        game = TicTacGame()

        self.assertTupleEqual(game.validate_input("1.2".split()), (False, None, None))

    def test_bad_validate_input_char(self):

        game = TicTacGame()

        self.assertTupleEqual(game.validate_input("a b".split()), (False, None, None))

    def test_bad_validate_input_out_of_range1(self):

        game = TicTacGame()

        self.assertTupleEqual(game.validate_input("1 4"), (False, None, None))

    def test_bad_validate_input_out_of_range2(self):

        game = TicTacGame()

        self.assertTupleEqual(game.validate_input("-1 1"), (False, None, None))

    def test_bad_validate_input_out_of_range3(self):

        game = TicTacGame()

        self.assertTupleEqual(game.validate_input("5 5"), (False, None, None))

    def test_bad_validate_input_out_of_range4(self):

        game = TicTacGame()

        self.assertTupleEqual(game.validate_input("-3 -3"), (False, None, None))

    def test_good_validate_input_left_bound(self):
        
        game = TicTacGame()

        self.assertTupleEqual(game.validate_input("1 1".split()), (True, 0, 0))

    def test_good_validate_input_right_bound(self):
        
        game = TicTacGame()

        self.assertTupleEqual(game.validate_input("3 3".split()), (True, 2, 2))

    def test_good_validate_input(self):
        
        game = TicTacGame()

        for i in range(1, 4):
            for j in range(1, 4):

                self.assertTupleEqual(game.validate_input(f"{i} {j}".split()), (True, i - 1, j - 1))

    def test_check_winner_in_init(self):

        game = TicTacGame()

        self.assertEqual(game.check_winner(), False)

    def test_check_winner_main_diag(self):
        
        game = TicTacGame()

        for i in range(3):
            game.board[i][i] = 'O'

        game.board[0][1] = 'X'
        game.board[0][2] = 'X'

        self.assertTrue(game.check_winner())

    def test_check_winner_inverse_diag(self):

        game = TicTacGame()

        for i in range(3):
            game.board[i][3 - i - 1] = 'O'

        game.board[2][1] = 'X'
        game.board[2][2] = 'X'

        self.assertTrue(game.check_winner())

    def test_check_winner_col_first(self):
        
        game = TicTacGame()

        for i in range(3):
            game.board[i][0] = 'O'

        game.board[1][2] = 'X'
        game.board[2][2] = 'X'

        self.assertTrue(game.check_winner())

    def test_check_winner_col_second(self):
        
        game = TicTacGame()

        for i in range(3):
            game.board[i][1] = 'O'

        game.board[1][2] = 'X'
        game.board[0][2] = 'X'

        self.assertTrue(game.check_winner())

    def test_check_winner_col_third(self):
        
        game = TicTacGame()

        for i in range(3):
            game.board[i][2] = 'O'

        game.board[1][0] = 'X'
        game.board[0][0] = 'X'

        self.assertTrue(game.check_winner())

    def test_check_winner_row_first(self):
        
        game = TicTacGame()

        for i in range(3):
            game.board[0][i] = 'O'

        game.board[1][2] = 'X'
        game.board[2][2] = 'X'

        self.assertTrue(game.check_winner())

    def test_check_winner_row_second(self):
        
        game = TicTacGame()

        for i in range(3):
            game.board[1][i] = 'O'

        game.board[0][2] = 'X'
        game.board[2][2] = 'X'

        self.assertTrue(game.check_winner())

    def test_check_winner_row_third(self):
        
        game = TicTacGame()

        for i in range(3):
            game.board[2][i] = 'O'

        game.board[1][2] = 'X'
        game.board[0][2] = 'X'

        self.assertTrue(game.check_winner())

    def test_check_winner_with_one_empty_raw(self):

        game = TicTacGame()

        game.board[0][0] = "O"
        game.board[0][1] = "X"
        game.board[0][2] = "O"
        game.board[1][0] = "X"
        game.board[1][1] = "O"   
        game.board[1][2] = "X"

        self.assertEqual(game.check_winner(), False)

    def test_check_winner_with_one_empty_col(self):

        game = TicTacGame()

        game.board[0][0] = "O"
        game.board[1][0] = "X"
        game.board[2][0] = "O"
        game.board[0][1] = "X"
        game.board[1][1] = "O"   
        game.board[2][1] = "X"

        self.assertEqual(game.check_winner(), False)

    def test_draw(self):

        game = TicTacGame()
        
        game.board[0][0] = "O"
        game.board[0][1] = "X"
        game.board[0][2] = "O"
        game.board[2][0] = "O" 
        game.board[2][1] = "X"
        game.board[2][2] = "O"  
        game.board[1][0] = "X"
        game.board[1][1] = "O"
        game.board[1][2] = "X"

        game._check_draw(0)

        self.assertTrue(game.draw_game)

    def test_occupied_cell(self):

        game = TicTacGame()

        for i in range(3):
            for j in range(3):
                game.board[i][j] = "O"

                self.assertFalse(game._check_occupied_cell(i, j))

if __name__ == "__main__":

    unittest.main()