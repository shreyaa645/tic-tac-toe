def initialize_board():
    return [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

def display_board(board):
    print("  1   2   3")
    for i, row in enumerate(board):
        print(f"{i + 1} {' | '.join(row)}")
        if i < 2:
            print(" ---|---|---")

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def get_valid_input(message, valid_values):
    while True:
        try:
            value = input(message)
            if value.lower() == "reset":
                return "reset"
            value = int(value)
            if value in valid_values:
                return value
            else:
                print("Invalid input. Please enter a valid value.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_tic_tac_toe():
    x_score = 0
    o_score = 0

    while True:
        print(f"\nCurrent Scores - Player X: {x_score}, Player O: {o_score}")
        print("Type 'reset' during your turn to reset scores and the game board.")

        current_player = "X"
        board = initialize_board()

        while True:
            display_board(board)

            move = get_valid_input(f"Player {current_player}, enter row (1, 2, or 3) or 'reset': ", [1, 2, 3, "reset"])

            if move == "reset":
                print("Scores and the game board have been reset.")
                break

            col = get_valid_input("Enter column (1, 2, or 3): ", [1, 2, 3])

            row = move - 1
            col -= 1

            if board[row][col] == " ":
                board[row][col] = current_player

                if check_winner(board, current_player):
                    display_board(board)
                    print(f"Player {current_player} wins! Congratulations!")
                    if current_player == "X":
                        x_score += 1
                    else:
                        o_score += 1
                    break
                elif is_board_full(board):
                    display_board(board)
                    print("It's a tie! The game is over.")
                    break
                current_player = "O" if current_player == "X" else "X"
            else:
                print("Invalid move! The cell is already occupied. Try again.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

# Start the game
play_tic_tac_toe()