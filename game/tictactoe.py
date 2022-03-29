""" class TicTacGame """
class TicTacGame:
    """
    Класс реализует игру в крестики-нолики
    """

    CHECK = tuple(range(1, 4))
    draw_game = False

    def __init__(self) -> None:
        self.board = [["_" for _ in range(3)] for _ in range(3)]

    def show_board(self) -> None:

        """ Show the game board """

        for i in range(3):
            raw = ""
            for j in range(3):
                raw += f"| {self.board[i][j]} "

            print("-------------")
            print(raw + f"| {i + 1}")

        print("-------------")
        print("  1   2   3  ")

    def validate_input(self, data: str) -> tuple:

        """ Check input data """

        try:
            x_c, y_c = tuple(map(int, data))
        except ValueError:
            return False, None, None

        return (True, x_c - 1, y_c - 1) if x_c in self.CHECK and \
            y_c in self.CHECK else (False, None, None)

    def _input_data(self, sign: str) -> None:

        print("Input coordinate of your step [number from 1 to 3]: ", end="")

        while True:

            data: str = input().split()

            answer, x_c, y_c = self.validate_input(data)

            if answer and self._check_occupied_cell(x_c, y_c):
                break

            print("Error!!! Input again: ", end="")

        self.board[x_c][y_c] = sign

    def check_winner(self) -> bool:

        """ Check winner player"""

        count: int = \
            sum([self.board[i].count('_')for i in range(len(self.board))])

        self._check_draw(count)

        # если на поле меньше 5 значений, не заходим
        if count < 5:

            # check raws
            for i, _ in enumerate(self.board):
                if self.board[i][0] != "_" and \
                        all(elem == self.board[i][0] for elem in
                            self.board[i]):
                    return True

            # check col
            for i, _ in enumerate(self.board):
                for j in range(len(self.board) - 1):
                    if self.board[j][i] != self.board[j + 1][i]:
                        break
                    if self.board[j][i] == "_":
                        break
                else:
                    return True

            # check inverse diag
            for i in range(len(self.board) - 1):
                if self.board[i][len(self.board) - i - 1] !=\
                        self.board[i + 1][len(self.board) - i - 2]:
                    break
                if self.board[i][len(self.board) - i - 1] == "_":
                    break
            else:
                return True

            # check diag
            for i in range(len(self.board) - 1):
                if self.board[i][i] != self.board[i + 1][i + 1]:
                    break
                if self.board[i][i] == "_":
                    break
            else:
                return True

        return False

    def _check_draw(self, count: int) -> None:

        if not count:
            self.draw_game = True

    def _check_occupied_cell(self, x_c: int, y_c: int) -> bool:

        return bool(self.board[x_c][y_c] == "_")

    def start_game(self) -> None:
        """
        Функция начинает игру, посредством запуска
        """

        while True:

            self.show_board()

            for sign in ("O", "X"):

                print(f"Step {sign}")
                self._input_data(sign)
                self.show_board()
                win = self.check_winner()

                if win:
                    print(f"Sign {sign} is winner!")
                    break

                if self.draw_game:
                    break

            if win:
                break

            if self.draw_game:
                print('Game over!')
                break


if __name__ == "__main__":

    game = TicTacGame()

    game.start_game()
