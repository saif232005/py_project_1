
import random

def print_board(board):
    """Display the board."""
    print("\n")
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")
    print("\n")

def check_winner(board, player):
    """Check if a player has won."""
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def tic_tac_toe():
    # 1) Create empty board
    board = [str(i) for i in range(1, 10)]

    # 2) Show Board
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    # 3) Set Players Randomly
    players = ['X', 'O']
    current_player = random.choice(players)
    print(f"{current_player} starts first!\n")

    # 4) Game loop
    for turn in range(9):  # max 9 moves
        # Take input
        while True:
            try:
                move = int(input(f"Player {current_player}, choose a cell (1-9): ")) - 1
                if 0 <= move < 9 and board[move] not in ['X', 'O']:
                    board[move] = current_player
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter a valid number (1-9).")

        # Show board after move
        print_board(board)

        # 6) Check win
        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            return

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

    # 5) If full board and no winner → Draw
    print("🤝 It's a draw!")

# Run the game
tic_tac_toe()