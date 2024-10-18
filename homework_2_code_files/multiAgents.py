from GameStatus_5120 import GameStatus

def minimax(game_state: GameStatus, depth: int, maximizingPlayer: bool, alpha=float('-inf'), beta=float('inf')):
    terminal = game_state.is_terminal()
    if (depth==0) or (terminal):
        newScores = game_state.get_scores(terminal)
        return newScores, None
    if maximizingPlayer:
        bestVal = float('-inf')
        best_move = None
        for child in game_state.get_children():
            value = minimax(child, depth - 1, False, alpha, beta)
            if value > bestVal:
                bestVal = value
                best_move = child
            alpha = max(alpha, bestVal)
            if beta <= alpha:
                break
    else:
        bestVal = float('inf')
        best_move = None
        for child in game_state.get_children():
            value, _ = minimax(child, depth - 1, True, alpha, beta)
            if value < bestVal:
                bestVal = value
                bestMove = child
            beta = min(beta, bestVal)
            if beta <= alpha:
                break

    """
    YOUR CODE HERE TO FIRST CHECK WHICH PLAYER HAS CALLED THIS FUNCTION (MAXIMIZING OR MINIMIZING PLAYER)
    YOU SHOULD THEN IMPLEMENT MINIMAX WITH ALPHA-BETA PRUNING AND RETURN THE FOLLOWING TWO ITEMS
    1. VALUE
    2. BEST_MOVE
    
    THE LINE TO RETURN THESE TWO IS COMMENTED BELOW WHICH YOU CAN USE
    """
    return value, best_move

def negamax(game_status: GameStatus, depth: int, turn_multiplier: int, alpha=float('-inf'), beta=float('inf')):
    terminal = game_status.is_terminal()
    if (depth==0) or (terminal):
        scores = game_status.get_negamax_scores(terminal)
        return scores, None
    score = float('-inf')
    best_move = None
    for child in game_status.get_children():
        value, _ = negamax(child, depth - 1, -turn_multiplier, -beta, -alpha)
        value = -value
        if value > score:
            score = value
            best_move = child
        alpha = max(alpha, score)
        if alpha >= beta:
            break
    return score, best_move
    

    """
    YOUR CODE HERE TO CALL NEGAMAX FUNCTION. REMEMBER THE RETURN OF THE NEGAMAX SHOULD BE THE OPPOSITE OF THE CALLING
    PLAYER WHICH CAN BE DONE USING -NEGAMAX(). THE REST OF YOUR CODE SHOULD BE THE SAME AS MINIMAX FUNCTION.
    YOU ALSO DO NOT NEED TO TRACK WHICH PLAYER HAS CALLED THE FUNCTION AND SHOULD NOT CHECK IF THE CURRENT MOVE
    IS FOR MINIMAX PLAYER OR NEGAMAX PLAYER
    RETURN THE FOLLOWING TWO ITEMS
    1. VALUE
    2. BEST_MOVE
    
    THE LINE TO RETURN THESE TWO IS COMMENTED BELOW WHICH YOU CAN USE
    
    """
