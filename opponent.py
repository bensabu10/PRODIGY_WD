import random

def get_ai_move(board):
    available_moves = [i for i, x in enumerate(board) if x == ' ']
    return random.choice(available_moves)
