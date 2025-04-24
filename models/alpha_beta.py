"""
Alpha-Beta Model
"""

from utils.game_logic import X, player, actions, result, utility, terminal

prune_count = 0
turn = 0

def alpha_beta_move(board):
    """
    Returns the optimal move for the current player using Alpha-Beta Pruning.
    This is the public entry point that initializes alpha and beta bounds
    and triggers the pruning-aware recursive evaluation engine.
    """
    alpha = float("-inf")
    beta = float("inf")
    global prune_count
    prune_count = 0  # Reset count for this turn
    global turn
    turn += 1

    if terminal(board):
        return None
    _, action = alpha_beta_search(board, alpha, beta)
    print(f"Total branches pruned in turn {turn}: {prune_count}")
    return action


def alpha_beta_search(board, alpha, beta):
    """
    Returns the optimal (score, action) tuple for the current player on the board.
    """
    if terminal(board):
        return utility(board), None
    return maximize_alpha_beta(board, alpha, beta) if player(board) == X else minimize_alpha_beta(board, alpha, beta)


def maximize_alpha_beta(board, alpha, beta):
    """
    Evaluates the best possible move and returns the (score, action) tuple
    that maximizes the utility score for player X.
    """
    best_score = float("-inf")
    best_action = None
    global prune_count

    for action in actions(board):
        board_result = result(board, action)
        score, _ = alpha_beta_search(board_result, alpha, beta)
        if score > best_score:
            best_score = score
            best_action = action
        alpha = max(alpha, best_score)
        if alpha >= beta:
            prune_count += 1
            break
    return best_score, best_action


def minimize_alpha_beta(board, alpha, beta):
    """
    Evaluates the best possible move and returns the (score, action) tuple
    that minimizes the utility score for playe.
    """
    best_score = float("inf")
    best_action = None
    global prune_count

    for action in actions(board):
        board_result = result(board, action)
        score, _ = alpha_beta_search(board_result, alpha, beta)
        if score < best_score:
            best_score = score
            best_action = action
        beta = min(beta, best_score)
        if beta <= alpha:
            prune_count += 1
            break
    return best_score, best_action
