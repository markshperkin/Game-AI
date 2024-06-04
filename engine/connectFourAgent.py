import numpy as np
from environments.connect_four import ConnectFourState, ConnectFour
'''
strategy link:
https://identity.pub/2019/10/16/minimax-connect4.html
https://roadtolarissa.com/connect-4-ai-how-it-works/
'''
def make_move(state: ConnectFourState, env: ConnectFour) -> int:
    best_move, best_score = minimax_search(env, state)
    print(f"Best move: {best_move} with score: {best_score}")
    return best_move


def minimax_search(game: ConnectFour, state: ConnectFourState) -> tuple:
    #determine the current player based on the player_turn attribute of the state
    player = state.player_turn
    _, move = max_value(game, state)
    #get the score for the resulting state after making the best move
    score = heuristic(game, game.next_state(state, move), player)
    return move, score


 
def max_value(game: ConnectFour, state: ConnectFourState, depth=4) -> tuple:
    if game.is_terminal(state) or depth <= 0:
        return heuristic(game, state, state.player_turn), None

    v = -np.inf
    best_move = None

    for move in game.get_actions(state):
        new_state = game.next_state(state, move)
        v2, _ = min_value(game, new_state, depth - 1)
        v2 = v2 if v2 is not None else -np.inf
        if v2 > v:
            v, best_move = v2, move

    return v, best_move

def min_value(game: ConnectFour, state: ConnectFourState, depth=4) -> tuple:
    if game.is_terminal(state) or depth <= 0:
        return heuristic(game, state, -state.player_turn), None

    v = np.inf
    best_move = None

    for move in game.get_actions(state):
        new_state = game.next_state(state, move)
        v2, _ = max_value(game, new_state, depth - 1)
        v2 = v2 if v2 is not None else np.inf
        if v2 < v:
            v, best_move = v2, move

    return v, best_move

def can_be_completed(grid, i, j, player):
    #get the grid shape
    rows, cols = grid.shape

    #define the directions for horizontal, vertical, and diagonal sets
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1), #horizontal and vertical
        (-1, -1), (-1, 1), (1, -1), (1, 1) #diagonal
    ]

    #check each direction for the possibility of completion
    for dx, dy in directions:
        #skip if moving out of bounds
        if not (0 <= i+dx < rows and 0 <= j+dy < cols):
            continue

        #check if the next space is empty
        if grid[i+dx][j+dy] == 0:
            #check if the space after that is occupied by the player
            if 0 <= i+2*dx < rows and 0 <= j+2*dy < cols and grid[i+2*dx][j+2*dy] == player:
                return True

        #check if the next space is empty and the space after that is also empty
        if grid[i+dx][j+dy] == 0 and 0 <= i+2*dx < rows and 0 <= j+2*dy < cols and grid[i+2*dx][j+2*dy] == 0:
            #check if the space after the second empty space is occupied by the player
            if 0 <= i+3*dx < rows and 0 <= j+3*dy < cols and grid[i+3*dx][j+3*dy] == player:
                return True

    return False
def heuristic(game: ConnectFour, state: ConnectFourState, player: int) -> float:
    #define the weights for 2 and 3 pieces in a row
    weight_2 = 1
    weight_3 = 10

    #get the grid shape
    rows, cols = state.grid.shape

   #calculate the score for the current player
    max_score = 0
    for i in range(rows):
        for j in range(cols):
            #check horizontal sets
            if j <= cols - 3:
                if all(state.grid[i][k] == player for k in range(j, j+3)):
                    max_score += weight_3
                elif all(state.grid[i][k] == player for k in range(j, j+2)) and not can_be_completed(state.grid, i, j, player):
                    max_score += weight_2
            #check vertical sets
            if i <= rows - 3:
                if all(state.grid[k][j] == player for k in range(i, i+3)):
                    max_score += weight_3
                elif all(state.grid[k][j] == player for k in range(i, i+2)) and not can_be_completed(state.grid, i, j, player):
                    max_score += weight_2
            #check forward diagonal sets
            if i <= rows - 3 and j <= cols - 3:
                if all(state.grid[i+k][j+k] == player for k in range(3)):
                    max_score += weight_3
                elif all(state.grid[i+k][j+k] == player for k in range(2)) and not can_be_completed(state.grid, i, j, player):
                    max_score += weight_2
            #check backward diagonal sets
            if i <= rows - 3 and j >= 2:
                if all(state.grid[i+k][j-k] == player for k in range(3)):
                    max_score += weight_3
                elif all(state.grid[i+k][j-k] == player for k in range(2)) and not can_be_completed(state.grid, i, j, player):
                    max_score += weight_2

    #calculate the score for the opponent
    min_score = 0
    for i in range(rows):
        for j in range(cols):
            #check horizontal sets
            if j <= cols - 3:
                if all(state.grid[i][k] == -player for k in range(j, j+3)):
                    min_score += weight_3
                elif all(state.grid[i][k] == -player for k in range(j, j+2)) and not can_be_completed(state.grid, i, j, player):
                    min_score += weight_2
            #check vertical sets
            if i <= rows - 3:
                if all(state.grid[k][j] == -player for k in range(i, i+3)):
                    min_score += weight_3
                elif all(state.grid[k][j] == -player for k in range(i, i+2)) and not can_be_completed(state.grid, i, j, player):
                    min_score += weight_2
            #check forward diagonal sets
            if i <= rows - 3 and j <= cols - 3:
                if all(state.grid[i+k][j+k] == -player for k in range(3)):
                    min_score += weight_3
                elif all(state.grid[i+k][j+k] == -player for k in range(2)) and not can_be_completed(state.grid, i, j, player):
                    min_score += weight_2
            #check backward diagonal sets
            if i <= rows - 3 and j >= 2:
                if all(state.grid[i+k][j-k] == -player for k in range(3)):
                    min_score += weight_3
                elif all(state.grid[i+k][j-k] == -player for k in range(2)) and not can_be_completed(state.grid, i, j, player):
                    min_score += weight_2
    # print("max score is")
    # print(max_score)
    # print("min score is")
    # print(min_score)

    score_diff = max_score - min_score

    return score_diff