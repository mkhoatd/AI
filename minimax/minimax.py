from typing import List, Tuple

INFINITY = float('inf')

def print_board(board, indent):
    print(str(indent) + "---------------------------------")
    for i in range(3):
        print(indent*"   " + "|", end="")
        print(board[i])
        
def next_move(player):
    return 'o' if player == 'x' else 'x'

def is_better_value(player, current_value, best_value):
    if player == 'o': return current_value > best_value
    else: return current_value < best_value
    
def get_valid_move(board):
    res = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                res.append((i, j))
    return res

def is_better_value(player: str, current_value: int, best_value: int) -> bool:
    """Returns true if the current value is better than the best value for the given player. 
    The player is either 'x' or 'o'. 
    The current value is better if it is higher for 'x' and lower for 'o'.
    """
    if player == 'x':
        return current_value > best_value
    else:
        return current_value < best_value

def minimax(board: List[List[str]], depth: int, player: str, num_moves):
    # Print the board
    print_board(board, num_moves)
    # Check if the game is over or if we've reached our depth limit
    if game_over(board) or depth == 0:
        # Return None for the move and the score for the board
        return None, score(board)
    # Set the best value to -infinity if the player is 'o' and infinity if the player is 'x'
    best_value = -INFINITY if player =='o' else INFINITY
    # Initialize the best move to None
    best_move = None
    # Get all the valid moves for the current board
    valid_moves = get_valid_move(board)           
    # Iterate through each of the valid moves
    for move in valid_moves:
        # Make a move on the board
        new_board = make_move(board, move, player)
        # Get the minimax score for the new board
        _, value = minimax(new_board, depth - 1, next_move(player=player), num_moves+1) 
        # Check if this move is better than the current best move
        if(is_better_value(player=player, current_value=value, best_value=best_value)):
            # Update the best move and best value
            best_move = move
            best_value = value
    # Return the best move and best value
    return best_move, best_value

def make_move(board: List[List[str]], move: Tuple[int, int], player: str) -> List[List[str]]:
    new_board = [row[:] for row in board]
    new_board[move[0]][move[1]] = player
    return new_board

def game_over(board: List[List[str]]) -> bool:
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '':
            return True
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return True
    # Check for a draw
    for row in board:
        for cell in row:
            if cell == '':
                return False
    return True

def score(board: List[List[str]]) -> float:
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '':
            if row[0] == 'o':
                return 1.0
            else:
                return -1.0
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            if board[0][col] == 'o':
                return 1.0
            else:
                return -1.0
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        if board[0][0] == 'o':
            return 1.0
        else:
            return -1.0
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        if board[0][2] == 'o':
            return 1.0
        else:
            return -1.0
    # Game is a draw
    return 0.0

# Example usage
board = [['o', '', 'x'], ['o', '', 'x'], ['', '', '']]
depth = 10000
player = 'x'
best_move, best_value = minimax(board, depth, player, 0)
print(best_move, best_value)  # (0, 2)
