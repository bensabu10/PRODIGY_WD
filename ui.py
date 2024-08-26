def display_board(board):
    print(f"""
    {board[0]} | {board[1]} | {board[2]}
    ---------
    {board[3]} | {board[4]} | {board[5]}
    ---------
    {board[6]} | {board[7]} | {board[8]}
    """)

def get_move():
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if 0 <= move <= 8:
                return move
            else:
                print("Move must be between 0 and 8.")
        except ValueError:
            print("Invalid input. Enter a number between 0 and 8.")

def display_result(message):
    print(message)
