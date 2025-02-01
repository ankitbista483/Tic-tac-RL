import os
import pickle


def ensure_directory(directory="models"):
    """Ensures that the given directory exists."""
    os.makedirs(directory, exist_ok=True)

def save_q_table(q_table, save_path="models/q_table.pkl"):
    """Saves the Q-table to a file."""
    ensure_directory(os.path.dirname(save_path))  # Ensure directory exists
    with open(save_path, "wb") as f:
        pickle.dump(q_table, f)
    print(f"Q-table saved to {save_path}")

def load_q_table(load_path="models/q_table.pkl"):
    """Loads the Q-table from a file, if it exists. Returns None if not found."""
    if os.path.exists(load_path):
        with open(load_path, "rb") as f:
            q_table = pickle.load(f)
        print(f"Loaded Q-table from {load_path}")
        return q_table
    else:
        print("No trained Q-table found!")
        return None


