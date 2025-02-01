def board_to_tuple(board):
    """Converts a NumPy board to a hashable tuple."""
    return tuple(map(tuple, board))