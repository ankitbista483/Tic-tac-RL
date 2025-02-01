import numpy as np 

class TicTacToe:
    def __init__(self):
        # Initialize a empty tic tac board
        self.board = np.zeros((3,3))
    
    def reset(self):
        # Reset after the board for the new game
        self.board = np.zeros((3,3))

    def display_board(self):
        # Displays the symbol in board
        symbols = {1 : 'X', -1 : 'O' , 0 : '.'}
        for row in self.board:
            print(' '.join(symbols[int(cell)] for cell in row))
        print()

    def make_move(self,row,col,player):
        # Helps to make a move if there is empty position
        if self.board[row,col] == 0:
            self.board[row,col] = player
            return True
        return False
    
    def available_moves(self):
        # Returns a list of empty position
        return [(r,c) for r in range(3) for c in range(3) if self.board[r, c] == 0]
    
    def check_winner(self):
        # Checks for the winner or for a draw

        for row in self.board:
            if abs(sum(row)) == 3:
                return np.sign(sum(row))
            
        for column in self.board.T:
            if abs(sum(column)) == 3:
                return np.sign(sum(column))
            
        if abs(sum(self.board[i,i] for i in range(3))) == 3:
            return np.sign(sum(self.board[i,i] for i in range(3)))
        
        if abs(sum(self.board[i,2-i] for i in range(3))) == 3:
            return np.sign(sum(self.board[i,2-i] for i in range(3)))
        
        if len(self.available_moves()) == 0:
            return 0
        
        return None
    






