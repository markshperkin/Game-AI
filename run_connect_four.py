from typing import Dict
from argparse import ArgumentParser
from environments.connect_four import ConnectFourState, ConnectFour
from visualizer.connect_four_visualizer import ConnectFourVisualizer
import numpy as np
from engine.connectFourAgent import make_move as make_move_import
from importlib import import_module

def main():
    # Create an argument parser object
    parser: ArgumentParser = ArgumentParser()
    # Add argument for specifying the opponent type (default is "computer")
    parser.add_argument('--opponent', type=str, default="computer", help="computer or random")
    # Add argument for specifying the module name (optional)
    parser.add_argument('--module', type=str, default=None)

    # Parse the arguments provided via command line
    args = parser.parse_args()

    # If a module is specified, import the make_move function from it
    if args.module is not None:
        make_move = import_module(args.module).make_move
    else:
        # Otherwise, use the default make_move function
        make_move = make_move_import

    # Initialize the ConnectFour environment
    env: ConnectFour = ConnectFour()

    if args.opponent == "computer":
        # Define an AI agent that uses the make_move function
        def ai_agent(state_func: ConnectFourState):
            return make_move(state_func, env)

        # Initialize the visualizer with the environment and AI agent
        viz = ConnectFourVisualizer(env, ai_agent)
        # Start the visualizer main loop
        viz.mainloop()

    elif args.opponent == "random":
        num_itrs: int = 4

        # Define a random move function for the opponent
        def make_move_opp(_, env_in):
            return np.random.choice(env_in.get_actions(state))

        player_order_names: Dict[int, str] = {-1: "MIN", 1: "MAX"}
        winner_names: Dict[int, str] = {-1: "MIN", 0: "DRAW", 1: "MAX"}
        grid_dim_x = 7
        grid_dim_y = 6

        num_wins: int = 0
        num_games: int = 0

        # Iterate through the specified number of iterations
        for _ in range(num_itrs):
            # Test both player orders
            for player_order in [[1, -1], [-1, 1]]:
                # Initialize the game state
                state: ConnectFourState = ConnectFourState(np.zeros((grid_dim_x, grid_dim_y)), True)

                # Loop until the game reaches a terminal state
                while not env.is_terminal(state):
                    for player in player_order:
                        # Prepare the state for the current player
                        state_choose = ConnectFourState(state.grid * player_order[0], True)
                        if player == 1:
                            # Use the AI agent's move for player 1
                            action: int = make_move(state_choose, env)
                        else:
                            # Use the random opponent's move for player -1
                            action: int = make_move_opp(state_choose, env)
                        # Get the next state based on the chosen action
                        state = env.next_state(state, action)

                        # Check if the game has reached a terminal state
                        if env.is_terminal(state):
                            # Calculate the utility and determine the winner
                            utility: float = env.utility(state)
                            winner: int
                            if utility * player_order[0] > 0:
                                winner = 1
                            elif utility == 0:
                                winner = 0
                            else:
                                winner = -1

                            if winner == 1:
                                num_wins += 1

                            # Print the results for the current game
                            print("Player_First: %s, Winner: %s" % (player_order_names[player_order[0]], winner_names[winner]))

                            num_games += 1
                            break

        # Print the overall win rate
        print("Win Rate: %.1f%% (%i/%i)" % (100 * num_wins / num_games, num_wins, num_games))

    else:
        # Raise an error for unknown opponent types
        raise ValueError("Unknown opponent type %s" % args.opponent)

if __name__ == "__main__":
    # Execute the main function when the script is run
    main()
