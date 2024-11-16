"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Count X's and O's on the board,because X goes first
    so if they have the same count,it's X's turn,otherwise
    it's O's turn
    """
    
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board
    """

    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    if board[i][j] is not EMPTY:
        raise ValueError("Invalid Action: Cell is already occupied")
    
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)

    return new_board
    


def winner(board):
    """
    Returns the winner of the game, if there is one
    """

    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not EMPTY:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        if EMPTY in row:
            return False;
        
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winning_player = winner(board)

    if winning_player == X:
        return 1
    elif winning_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    
    current_player = player(board)

    if current_player == X:
        value, best_action = max_value(board)
    else:
        value, best_action = min_value(board)

    return best_action

def max_value(board):
    if terminal(board):
        return utility(board), None
    
    max_eval = -math.inf
    best_action = None

    for action in actions(board):
        eval, _ = min_value(result(board, action))
        if eval > max_eval:
            max_eval = eval
            best_action = action
    
    return max_eval, best_action


def min_value(board):
    """
    Returns the minimum utility and the best action for player O.
    """
    if terminal(board):
        return utility(board), None

    min_eval = math.inf
    best_action = None
    
    for action in actions(board):
        eval, _ = max_value(result(board, action))
        if eval < min_eval:
            min_eval = eval
            best_action = action
    
    return min_eval, best_action