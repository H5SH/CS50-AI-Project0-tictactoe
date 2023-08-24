"""
Tic Tac Toe Player
"""

import math
import copy

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
    Returns player who has the next turn on a board.
    """
    count_X = 0
    count_O = 0
    for row in board:
        count_X = count_X + row.count(X)
        count_O = count_O + row.count(O)

    # if there are more X then O then its O's turn
    if count_X > count_O:
        return O
    # if first turn or both equal
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                actions.append((i, j))
    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    new_board = copy.deepcopy(board)

    if new_board[action[0]][action[1]] != EMPTY:
        raise ValueError
    
    # to get the player whos turn it is
    new_board[action[0]][action[1]] = player(new_board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    if all(i == board[0][0] for i in board[0]):
        return board[0][0]
    elif all(i == board[1][0] for i in board[1]):
        return board[1][0]
    elif all(i == board[2][0] for i in board[2]):
        return board[2][0]
    # Check columns
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    # Check diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    game = winner(board)
    # no winner is decided and no box is empty in the board
    if game == None and board[0].count(EMPTY) == 0 and board[1].count(EMPTY) == 0 and board[2].count(EMPTY) == 0:
        return True
    # a winner is decided
    elif game == X or game == O:
        return True
    else:
        return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            v, action = Max_value(board)
        else:
            v, action = Min_value(board)

        return action


def Max_value(board):

    v = -10000
    Action = None
    if terminal(board):
        return utility(board), Action
    
    for action in actions(board):
      value, act = Min_value(result(board, action))
      if value > v:
          v = value
          Action = action
          # Player wins
          if v == 1:
              return v, Action

    return v, Action
    

def Min_value(board):

    Action = None
    v = 10000
    if terminal(board):
        return utility(board), Action
    for action in actions(board):
        value, act = Max_value(result(board, action))
        if value < v:
            v = value
            Action = act
            # Player wins
            if v == -1:
                return v, Action
            
    return v, Action
    

