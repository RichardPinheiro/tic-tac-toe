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
    countX = sum(row.count(X) for row in board)
    countO = sum(row.count(O) for row in board)
    return X if countX == countO else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {
        (i, j)
        for i, row in enumerate(board)
        for j, cell in enumerate(row)
        if cell is EMPTY
    }

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid move")
    row, col = action
    board_copy = copy.deepcopy(board)
    board_copy[row][col] = player(board)
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
        unique = set(row)
        if len(unique) == 1 and EMPTY not in unique:
            return row[0]
    return None

def check_col_winner(board):
    """
    Returns the winner in a col.
    """
    for i in range(3):
        col = [board[0][i], board[1][i], board[2][i]]
        unique = set(col)
        if len(unique) == 1 and EMPTY not in unique:
            return col[0]
    return None

def check_diagonal_winner(board):
    """
    Returns the winner in a diagonal.
    """
    diagonal_1 = [board[i][i] for i in range(3)]
    diagonal_2 = [board[i][2 - i] for i in range(3)]
    for diagonal in (diagonal_1, diagonal_2):
        unique = set(diagonal)
        if len(unique) == 1 and EMPTY not in unique:
            return diagonal[0]
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
    return all(cell is not EMPTY for row in board for cell in row)

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result is None:
        return 0
    return 1 if result == X else -1
