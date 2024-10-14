# Function to print the Tic Tac Toe board

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
 
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

                                                                           # Main function to run the game
def tic_tac_toe():
   
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")

                                                                           # Get row and column from the player
        
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
        except ValueError:
            print("Please enter a valid number!")
            continue

        
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid position! Choose row and column from 1 to 3.")
            continue
        if board[row][col] != ' ':
            print("Position already taken! Choose another.")
            continue

        
        board[row][col] = current_player

      
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

       
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
tic_tac_toe()
