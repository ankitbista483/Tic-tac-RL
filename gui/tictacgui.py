import tkinter as tk
from tkinter import messagebox
from game.game import TicTacToe
from agent.agent import QLearningAgent
from utils.utils import load_q_table


class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")

        self.game = TicTacToe()
        self.agent = QLearningAgent()
        self.current_player = 1  # 1 is X, -1 is O

        # Create the 3x3 grid of buttons
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_grid()

        # Display current player
        self.label = tk.Label(self.master, text="Player X's Turn", font=('Arial', 14))
        self.label.grid(row=3, column=0, columnspan=3)

    def create_grid(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(self.master, text=' ', width=10, height=3,
                                                   font=('Arial', 24), command=lambda r=row, c=col: self.on_click(r, c))
                self.buttons[row][col].grid(row=row, column=col)

    def on_click(self, row, col):
        if self.game.board[row][col] != 0:
            return  # Skip if the cell is already filled

        self.game.make_move(row, col, self.current_player)
        self.update_board()

        winner = self.game.check_winner()
        if winner is not None:
            self.end_game(winner)
        else:
            self.switch_player()

    def update_board(self):
        symbols = {1: 'X', -1: 'O', 0: ' '}
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=symbols[int(self.game.board[row][col])])

    def switch_player(self):
        self.current_player *= -1  # Switch players
        if self.current_player == 1:
            self.label.config(text="Player X's Turn")
        else:
            self.label.config(text="Player O's Turn")
            self.agent_turn()

    def agent_turn(self):
        available_moves = self.game.available_moves()
        if available_moves:
            action = self.agent.choose_action(available_moves, tuple(map(tuple, self.game.board)))
            self.game.make_move(action[0], action[1], self.current_player)
            self.update_board()

            winner = self.game.check_winner()
            if winner is not None:
                self.end_game(winner)
            else:
                self.switch_player()

    def end_game(self, winner):
        if winner == 1:
            winner_text = "Player X wins!"
        elif winner == -1:
            winner_text = "Player O wins!"
        else:
            winner_text = "It's a draw!"

        messagebox.showinfo("Game Over", winner_text)
        self.reset_game()

    def reset_game(self):
        self.game.reset()
        self.current_player = 1
        self.label.config(text="Player X's Turn")
        self.update_board()

def load_agent():
    agent = QLearningAgent()
    q_table = load_q_table("models/q_table.pkl")
    agent.q_table = q_table  # Assign the loaded Q-table to the agent
    return agent
