from typing import List, Tuple

INFINITY = float('inf')

def print_board(board, indent):
    print(str(indent) + "---------------------------------")
    for i in range(3):
        print(indent*"   " + "|", end="")
        print(board[i])
        
def next_move(player):
    return 'o' if player == 'x' else 'x'

def is_best_value(player, current_value, best_value):
    if player == 'o': return current_value > best_value
    else: return current_value < best_value

def minimax(board: List[List[str]], depth: int, player: str, moves) -> float:
    print_board(board, moves)
    if game_over(board) or depth == 0:
        return score(board)
    best_value = -INFINITY if player =='o' else INFINITY
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                new_board = make_move(board, i, j, player)
                value = minimax(new_board, depth - 1, next_move(player=player), moves+1)
                # best_value = value if is_best_value(player=player, current_value=value, best_value=best_value) else best_value
                if(is_best_value(player=player, current_value=value, best_value=best_value)):
                    best_move = i, j
                    best_value = value
    return best_move, best_value

def find_best_move(board: List[List[str]], depth: int, player: str) -> Tuple[int, int]:
    best_value = -INFINITY if player == 'o' else INFINITY
    best_move = None
    print_board(board, 0)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                new_board = make_move(board, i, j, player)
                value = minimax(new_board, depth - 1, next_move(player=player), 1)
                if is_best_value(player, current_value=value, best_value=best_value):
                    best_value = value
                    best_move = (i, j)
    return best_move, best_value

def make_move(board: List[List[str]], i: int, j: int, player: str) -> List[List[str]]:
    new_board = [row[:] for row in board]
    new_board[i][j] = player
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
depth = 1
player = 'o'
best_move, best_value = minimax(board, depth, player, 0)
print(best_move, best_value)  # (0, 2)
