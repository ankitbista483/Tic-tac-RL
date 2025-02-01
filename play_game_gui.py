import tkinter as tk
from gui.tictacgui import TicTacToeGUI

def main():
    root = tk.Tk()
    gui = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
