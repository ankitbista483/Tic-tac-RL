import random 
import numpy as np



class QLearningAgent:
    def __init__(self,alpha =0.1, gamma =0.9, epsilon = 0.2):
        self.q_table = {}
        self.alpha = alpha
        self.gamma = gamma 
        self.epsilon = epsilon

    
    def get_q_values(self,state,action):
        return self.q_table.get((state,action),0)
    
    def choose_action(self,available_moves,state):
        if random.uniform(0,1) < self.epsilon:
            return random.choice(available_moves)
        else:
            q_values = [self.get_q_values(state, move) for move in available_moves]
            max_q = max(q_values)
            return available_moves[q_values.index(max_q)]
        
    def update_q_values(self,state,action,reward, next_state, next_available_move):
        max_q_values = max([self.get_q_values(next_state,a) for a in next_available_move],default=0)
        current_q_state = self.get_q_values(state,action)
        new_q = current_q_state + self.alpha*(reward + self.gamma * max_q_values -current_q_state)
        self.q_table[(state,action)] = new_q


