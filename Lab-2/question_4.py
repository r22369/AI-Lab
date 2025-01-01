def calculate_heuristic(board, player):
    opponent = 'O' if player == 'X' else 'X'
    player_open = 0
    opponent_open = 0

    for row in board:
        if all(cell == '' or cell == player for cell in row):
            player_open += 1
        if all(cell == '' or cell == opponent for cell in row):
            opponent_open += 1

    for col in range(3):
        if all(board[row][col] == '' or board[row][col] == player for row in range(3)):
            player_open += 1
        if all(board[row][col] == '' or board[row][col] == opponent for row in range(3)):
            opponent_open += 1

    if all(board[i][i] == '' or board[i][i] == player for i in range(3)):
        player_open += 1
    if all(board[i][i] == '' or board[i][i] == opponent for i in range(3)):
        opponent_open += 1

    if all(board[i][2 - i] == '' or board[i][2 - i] == player for i in range(3)):
        player_open += 1
    if all(board[i][2 - i] == '' or board[i][2 - i] == opponent for i in range(3)):
        opponent_open += 1

    return player_open - opponent_open

board1 = [
    ['X', '', ''],
    ['O', 'X', ''],
    ['', 'O', 'X']
]
print(f"Heuristic for board1 (X): {calculate_heuristic(board1, 'X')}")

board2 = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['', '', '']
]
print(f"Heuristic for board2 (X): {calculate_heuristic(board2, 'X')}")

board3 = [
    ['X', '', 'O'],
    ['', 'O', ''],
    ['O', '', 'X']
]
print(f"Heuristic for board3 (X): {calculate_heuristic(board3, 'X')}")

board4 = [
    ['X', 'O', ''],
    ['', 'X', ''],
    ['', '', 'X']
]
print(f"Heuristic for board4 (X): {calculate_heuristic(board4, 'X')}")

board5 = [
    ['O', 'X', ''],
    ['', 'O', ''],
    ['', '', 'O']
]
print(f"Heuristic for board5 (O): {calculate_heuristic(board5, 'O')}")

board6 = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['O', 'X', 'O']
]
print(f"Heuristic for board6 (X): {calculate_heuristic(board6, 'X')}")
