class TicTacToe:
    def __init__(self, board, player_symbol, opponent_symbol):
        self.board = board  # Board as a 2D list
        self.player = player_symbol
        self.opponent = opponent_symbol

    def is_open(self, line, symbol):
        return all(cell == symbol or cell == "-" for cell in line)

    def heuristic(self):
        rows = self.board
        cols = [[self.board[i][j] for i in range(3)] for j in range(3)]
        diag1 = [self.board[i][i] for i in range(3)]
        diag2 = [self.board[i][2 - i] for i in range(3)]

        lines = rows + cols + [diag1, diag2]

        player_score = sum(1 for line in lines if self.is_open(line, self.player))
        opponent_score = sum(1 for line in lines if self.is_open(line, self.opponent))

        return player_score - opponent_score


if __name__ == "__main__":
    board = [
        ["X", "O", "X"],
        ["-", "X", "O"],
        ["O", "-", "-"]
    ]
    player_symbol = "X"
    opponent_symbol = "O"

    ttt = TicTacToe(board, player_symbol, opponent_symbol)
    heuristic_value = ttt.heuristic()
    print(f"Heuristic Value: {heuristic_value}")

