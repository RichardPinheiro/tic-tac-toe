"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0

    for row in board:
        for cell in row:
            if cell is X:
                countX += 1
            if cell is O:
                countO += 1

    return X if countX == countO else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    condinates = set()

    for row_index, row in enumerate(board):
        for cell_index, cell in enumerate(row):
            if cell is EMPTY:
                condinates.add((row_index, cell_index))

    return condinates


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid move")

    board_copy = copy.deepcopy(board)
    current_player = player(board)
    row, col = action

    board_copy[row][col] = current_player

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for check in (check_row_winner, check_col_winner, check_diagonal_winner):
        result = check(board)
        if result is not None:
            return result

    return None


def check_row_winner(board):
    """
    Returns the winner in a row.
    """
    for row in board:
        unique_row = set(row)
        if len(unique_row) == 1 and EMPTY not in unique_row:
            return row[0]

    return None


def check_col_winner(board):
    """
    Returns the winner in a col.
    """
    for i in range(3):
        col = [board[0][i], board[1][i], board[2][i]]
        unique_col = set(col)
        if len(unique_col) == 1 and EMPTY not in unique_col:
            return col[0]

    return None


def check_diagonal_winner(board):
    """
    Returns the winner in a diagonal.
    """
    diagonal_1 = [board[0][0], board[1][1], board[2][2]] # Top-left to bottom-right
    diagonal_2 = [board[0][2], board[1][1], board[2][0]] # Top-right to bottom-left

    unique_diagonal_1 = set(diagonal_1)
    unique_diagonal_2 = set(diagonal_2)

    if len(unique_diagonal_1) == 1 and EMPTY not in unique_diagonal_1:
        return diagonal_1[0]

    if len(unique_diagonal_2) == 1 and EMPTY not in unique_diagonal_2:
        return diagonal_2[0]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or is_draw(board)


def is_draw(board):
    """
    Returns True if the board is full and no EMPTY cells, False otherwise.
    """
    for row in board:
        for cell in row:
            if cell is EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)

    if result == None:
        return 0

    return 1 if result == X else -1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return utility(board), None

    return maximize_score(board) if player(board) == X else minimize_score(board)


def maximize_score(board):
    """
    Evaluates all possible moves and returns the action
    that maximizes the utility score for player X.
    """
    best_score = float("-inf")
    best_action = None

    for action in actions(board):
        board_result = result(board, action)
        score, _ = minimax(board_result)
        if score > best_score:
            best_score = score
            best_action = action

    return best_score, best_action


def minimize_score(board):
    """
    Evaluates all possible moves and returns the action
    that minimizes the utility score for player O.
    """
    best_score = float("inf")
    best_action = None

    for action in actions(board):
        board_result = result(board, action)
        score, _ = minimax(board_result)
        if score < best_score:
            best_score = score
            best_action = action

    return best_score, best_action
