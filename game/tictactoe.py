
class TicTacGame:

    CHECK = tuple(range(1, 4))
    END_GAME = False

    def __init__(self) -> None:
        self.board = [["_" for _ in range(3)] for _ in range(3)]

    def _show_board(self) -> None:

        for i in range(3):
            raw = ""
            for j in range(3):
                raw += f"| {self.board[i][j]} "

            print("-------------")
            print(raw + f"| {i + 1}")

        print("-------------")
        print("  1   2   3  ")

    def _validate_input(self, data: str) -> tuple:

        try:
            x, y = tuple(map(int, data))
        except ValueError:
            return False, None, None

        return (True, x - 1, y - 1) if x in self.CHECK and y in self.CHECK else (False, None, None)

    def _input_data(self, sign: str) -> None:

        print("Input coordinate of your step [number from 1 to 3]: ", end="")

        while True:

            data: str = input().split()

            answer, x, y = self._validate_input(data)

            if answer and self.board[x][y] == "_":
                break

            print("Error!!! Input again: ", end ="")

        self.board[x][y] = sign

    def _check_winner(self) -> bool:

        count: int = sum([self.board[i].count('_') for i in range(len(self.board))])

        if not count:
            self.END_GAME = True

        # если на поле меньше 5 значений, не заходим
        if count < 5:

            # check raws
            for i, _ in enumerate(self.board):
                if self.board[i][0] != "_" and \
                    all(elem == self.board[i][0] for elem in self.board[i]):
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
                if  self.board[i][len(self.board) - i - 1] == "_":
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

    def start_game(self) -> None:

        while True:

            self._show_board()

            for sign in ("O", "X"):

                print(f"Step {sign}")
                self._input_data(sign)
                self._show_board()
                win = self._check_winner()

                if win:
                    print(f"Sign {sign} is winner!")
                    break

                if self.END_GAME:
                    break

            if win:
                break

            if self.END_GAME:
                print('Game over!')


if __name__ == "__main__":

    game = TicTacGame()

    game.start_game()
