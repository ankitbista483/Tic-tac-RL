import random
from game.game import TicTacToe
from agent.agent import QLearningAgent
from utils.utils import load_q_table

def load_agent(q_table_path="models/q_table.pkl"):
    """Loads a trained Q-learning agent from the saved Q-table or trains a new one if missing."""
    agent = QLearningAgent()
    q_table = load_q_table(q_table_path)

    agent.q_table = q_table  # Assign the loaded Q-table to the agent

    return agent


def play_game():
    agent = load_agent()  # Load the trained agent
    game = TicTacToe()
    current_player = 1  # Agent starts as X

    for _ in range(9):  # Maximum of 9 moves
        game.display_board()

        state = tuple(map(tuple, game.board))
        available_moves = game.available_moves()

        if current_player == 1:
            # Agent's turn (Player 1)
            print("Agent's turn (X)")
            action = agent.choose_action(available_moves, state)
            game.make_move(action[0], action[1], current_player)
        else:
            # Player's turn (Player 2)
            print("Your turn (O)")
            while True:
                try:
                    # Prompt the user for input
                    row = int(input("Enter the row (0, 1, 2): "))
                    col = int(input("Enter the column (0, 1, 2): "))

                    # Check if the move is valid
                    if (row, col) in available_moves:
                        game.make_move(row, col, current_player)
                        break
                    else:
                        print("Invalid move! Try again.")
                except ValueError:
                    print("Invalid input! Please enter numbers between 0 and 2.")

        # Check for winner after the move
        winner = game.check_winner()
        if winner is not None:
            game.display_board()
            if winner == 1:
                print("Agent (X) wins!")
            elif winner == -1:
                print("You (O) win!")
            else:
                print("It's a draw!")
            break

        current_player *= -1  # Switch players


if __name__ == "__main__":
    play_game()
