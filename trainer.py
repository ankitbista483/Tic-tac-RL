import random


from agent.agent import QLearningAgent
from game.game import TicTacToe
from utils.utils import save_q_table

def train_agent(episode=150000, save_path="models/q_table.pkl"):
    agent = QLearningAgent()
    
    for _ in range(episode):
        game = TicTacToe()
        current_player = 1  # Agent starts as X
        
        while True:
            state = tuple(map(tuple, game.board))
            available_moves = game.available_moves()

            if current_player == 1:
                action = agent.choose_action(available_moves, state)
            else:
                # If there are no available moves, break the loop (draw or error state)
                if not available_moves:
                    print("No available moves left! Something went wrong.")
                    break  # Exiting the loop in case of an error state
                action = random.choice(available_moves)
            
            # Make the move
            move_success = game.make_move(action[0], action[1], current_player)
            
            # If move wasn't successful, continue without making a move
            if not move_success:
                print(f"Failed to make move: {action} for player {current_player}.")
                break  # Exit on failure
            
            # Check the winner
            winner = game.check_winner()
            
            # Define reward based on the winner
            next_state = tuple(map(tuple, game.board))
            next_available_move = game.available_moves()

            if winner is not None:
                reward = 1 if winner == 1 else -1 if winner == -1 else 0
                agent.update_q_values(state, action, reward, next_state, next_available_move)
                break  # End the game if there's a winner
            else:
                # If no winner yet, continue with a reward of 0
                agent.update_q_values(state, action, 0, next_state, next_available_move)
            
            # Switch player for the next turn
            current_player *= -1  # Switch players

        # Reset the game after each episode
        game.reset()

    # Save the trained Q-table
    save_q_table(agent.q_table, save_path)

    return agent

if __name__ == "__main__":
    print("Training started...")
    train_agent()
    print("Training complete. Q-table saved.")

