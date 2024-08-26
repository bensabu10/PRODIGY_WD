from ui import display_board, get_move, display_result
from game_logic import check_winner, make_move, is_draw

def main():
    board = [' ' for _ in range(9)]
    current_player = 'X'
    
    while True:
        display_board(board)
        move = get_move()
        
        if make_move(board, move, current_player):
            if check_winner(board, current_player):
                display_board(board)
                display_result(f"Player {current_player} wins!")
                break
            elif is_draw(board):
                display_board(board)
                display_result("It's a draw!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()
