"""
Minimax Model
"""

from utils.game_logic import X, player, actions, result, utility, terminal

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    _, action = _minimax_internal(board)
    return action

def _minimax_internal(board):
    """
    Returns the optimal (score, action) tuple for the current player on the board.
    """
    if terminal(board):
        return utility(board), None
    return maximize_score(board) if player(board) == X else minimize_score(board)

def maximize_score(board):
    """
    Evaluates all possible moves and returns (score, action) tuple
    that maximizes the utility score for player X.
    """
    best_score = float("-inf")
    best_action = None
    for action in actions(board):
        board_result = result(board, action)
        score, _ = _minimax_internal(board_result)
        if score > best_score:
            best_score = score
            best_action = action
    return best_score, best_action

def minimize_score(board):
    """
    Evaluates all possible moves and returns (score, action) tuple
    that minimizes the utility score for player O.
    """
    best_score = float("inf")
    best_action = None
    for action in actions(board):
        board_result = result(board, action)
        score, _ = _minimax_internal(board_result)
        if score < best_score:
            best_score = score
            best_action = action
    return best_score, best_action
