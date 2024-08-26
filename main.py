from ui import display_board, get_move, display_result
from game_logic import check_winner, make_move, is_draw

def main():
    board = [' ' for _ in range(9)]  # Initialize an empty board
    current_player = 'X'  # Starting player

    while True:
        display_board(board)
        move = get_move()  # Get the player's move
        
        if make_move(board, move, current_player):  # Make the move
            if check_winner(board, current_player):  # Check for a winner
                display_board(board)
                display_result(f"Player {current_player} wins!")  # Display the result
                break
            elif is_draw(board):  # Check for a draw
                display_board(board)
                display_result("It's a draw!")
                break
            current_player = 'O' if current_player == 'X' else 'X'  # Switch player
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()
