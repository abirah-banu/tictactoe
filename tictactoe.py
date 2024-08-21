import math

# Function to print the board
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

# Function to check for a winner
def check_winner(board, player):
    win_conditions = [
        # Horizontal
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Vertical
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Diagonal
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    for condition in win_conditions:
        if all(board[x][y] == player for x, y in condition):
            return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# Function to find the best move for the AI
def find_best_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# Main function to play the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'  # Human starts first

    while True:
        print_board(board)

        if current_player == 'X':
            # Human move
            move = input("Enter your move (row and column): ")
            x, y = map(int, move.split())
            if board[x][y] == ' ':
                board[x][y] = 'X'
                if check_winner(board, 'X'):
                    print_board(board)
                    print("Congratulations! You win!")
                    break
                current_player = 'O'
        else:
            # AI move
            move = find_best_move(board)
            if move:
                board[move[0]][move[1]] = 'O'
                if check_winner(board, 'O'):
                    print_board(board)
                    print("AI wins! Better luck next time.")
                    break
                current_player = 'X'

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

play_game()