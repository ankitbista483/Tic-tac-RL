from agent import QLearningAgent
from game import TicTacToe
import random



def train_agent(episode = 10000):
    agent = QLearningAgent()
    for _ in range(episode):
        game = TicTacToe()
        current_player = 1 #Agent starts as X

        while True:
            state = tuple(map(tuple,game.board))
            available_moves = game.available_moves()

            if current_player == 1:
                action = agent.choose_action(available_moves,state)
            else:
                action = random.choice(available_moves)

            game.make_move(action[0],action[1],current_player)
            winner = game.check_winner()

            next_state = tuple(map(tuple,game.board))
            next_available_move = game.available_moves()

            if winner is not None:
                reward = 1 if winner == 1 else -1 if winner == -1 else 0
                agent.udpate_q_values(state,action,reward,next_state,next_available_move)
            else:
                agent.udpate_q_values(state,action,0,next_state,next_available_move)
            
            current_player *= -1
    return agent