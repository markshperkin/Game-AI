import numpy as np
from environments.connect_four import ConnectFourState, ConnectFour

def make_move(state: ConnectFourState, env: ConnectFour) -> int:
    # Perform a minimax search to determine the best move
    best_move, best_score = minimax_search(env, state)
    # Print the best move and its score for debugging purposes
    print(f"Best move: {best_move} with score: {best_score}")
    # Return the best move
    return best_move

def minimax_search(game: ConnectFour, state: ConnectFourState, depth=4) -> tuple:
    # Determine the current player
    player = state.player_turn
    # Call max_value to start the minimax algorithm and get the best move and score
    best_score, best_move = max_value(game, state, depth, -np.inf, np.inf)
    # Return the best move and its score
    return best_move, best_score

def max_value(game: ConnectFour, state: ConnectFourState, depth, alpha, beta) -> tuple:
    # If the game is in a terminal state or depth limit is reached, return the heuristic value
    if game.is_terminal(state) or depth <= 0:
        return heuristic(game, state, state.player_turn), None

    v = -np.inf  # Initialize the maximum value
    best_move = None  # Initialize the best move

    # Iterate over all possible actions
    for move in game.get_actions(state):
        # Get the next state after making the move
        new_state = game.next_state(state, move)
        # Recursively call min_value to evaluate this move
        v2, _ = min_value(game, new_state, depth - 1, alpha, beta)
        # Update the maximum value and best move if a better move is found
        if v2 > v:
            v, best_move = v2, move
        # Update alpha
        alpha = max(alpha, v)
        # Alpha-beta pruning
        if alpha >= beta:
            break

    return v, best_move  # Return the maximum value and the best move

def min_value(game: ConnectFour, state: ConnectFourState, depth, alpha, beta) -> tuple:
    # If the game is in a terminal state or depth limit is reached, return the heuristic value
    if game.is_terminal(state) or depth <= 0:
        return heuristic(game, state, -state.player_turn), None

    v = np.inf  # Initialize the minimum value
    best_move = None  # Initialize the best move

    # Iterate over all possible actions
    for move in game.get_actions(state):
        # Get the next state after making the move
        new_state = game.next_state(state, move)
        # Recursively call max_value to evaluate this move
        v2, _ = max_value(game, new_state, depth - 1, alpha, beta)
        # Update the minimum value and best move if a better move is found
        if v2 < v:
            v, best_move = v2, move
        # Update beta
        beta = min(beta, v)
        # Alpha-beta pruning
        if alpha >= beta:
            break

    return v, best_move  # Return the minimum value and the best move

def can_be_completed(grid, i, j, player):
    rows, cols = grid.shape  # Get the grid shape
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]  # Define directions

    # Check each direction for the possibility of completion
    for dx, dy in directions:
        if not (0 <= i+dx < rows and 0 <= j+dy < cols):
            continue

        # Check if the next space is empty
        if grid[i+dx][j+dy] == 0:
            if 0 <= i+2*dx < rows and 0 <= j+2*dy < cols and grid[i+2*dx][j+2*dy] == player:
                return True

        # Check if the next space is empty and the space after that is also empty
        if grid[i+dx][j+dy] == 0 and 0 <= i+2*dx < rows and 0 <= j+2*dy < cols and grid[i+2*dx][j+2*dy] == 0:
            if 0 <= i+3*dx < rows and 0 <= j+3*dy < cols and grid[i+3*dx][j+3*dy] == player:
                return True

    return False  # Return False if no completion is possible

def heuristic(game: ConnectFour, state: ConnectFourState, player: int) -> float:
    weight_2 = 1  # Define the weight for 2 in a row
    weight_3 = 10  # Define the weight for 3 in a row
    weight_4 = 1000  # Define the weight for 4 in a row

    rows, cols = state.grid.shape  # Get the grid shape
    max_score = 0  # Initialize the score for the current player
    min_score = 0  # Initialize the score for the opponent

    # Calculate the score for the current player and the opponent
    for i in range(rows):
        for j in range(cols):
            if state.grid[i][j] == player:
                max_score += evaluate_position(state.grid, i, j, player, weight_2, weight_3, weight_4)
            elif state.grid[i][j] == -player:
                min_score += evaluate_position(state.grid, i, j, -player, weight_2, weight_3, weight_4)

    score_diff = max_score - min_score  # Calculate the score difference
    return score_diff  # Return the heuristic value

def evaluate_position(grid, i, j, player, weight_2, weight_3, weight_4):
    rows, cols = grid.shape  # Get the grid shape
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # Define directions
    score = 0  # Initialize the score

    # Check each direction for potential scores
    for dx, dy in directions:
        count = 0
        for k in range(4):
            x, y = i + k*dx, j + k*dy
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == player:
                count += 1
            else:
                break

        # Add scores based on the count of pieces in a row
        if count == 2:
            score += weight_2
        elif count == 3:
            score += weight_3
        elif count == 4:
            score += weight_4

    return score  # Return the score for this position
