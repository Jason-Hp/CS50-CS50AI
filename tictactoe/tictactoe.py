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
    xs = 0
    os = 0

    for i in board:
        for j in i:
            if j == X:
                xs = xs + 1
            elif j == O:
                os = os + 1
    if xs>os:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionz = set()

    a = 0
    b = 0

    for i in board:
        b = 0
        for j in i:
            if j == EMPTY:
                actionz.add((a,b))
            b = b + 1
        a = a + 1

    return actionz

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]

    if not (0<=i<=2) or not(0<=j<=2):
         raise NameError(f"Action {action} is not a valid action for the board.")
    elif terminal(board):
         raise NameError(f"Action {action} is not a valid action for the board.")
    elif board[i][j]!=EMPTY:
         raise NameError(f"Action {action} is not a valid action for the board.")

    res = copy.deepcopy(board)
    turn = player(board)

    res[i][j] = turn
    return res


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in board:
        if i.count(X) == 3:
            return X
        elif i.count(O) == 3:
            return O
    res = copy.deepcopy(board)
    for x in range(3):
        for j in range(3):
            res[x][j] = board[j][x]
    for i in res:
        if i.count(X) == 3:
            return X
        elif i.count(O) == 3:
            return O
    checker = []
    checker.append(board[0][0])
    checker.append(board[1][1])
    checker.append(board[2][2])
    if checker.count(X) == 3:
        return X
    elif checker.count(O) == 3:
        return O
    checker = []
    checker.append(board[0][2])
    checker.append(board[1][1])
    checker.append(board[2][0])
    if checker.count(X) == 3:
        return X
    elif checker.count(O) == 3:
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board)!=None:
        return True

    for i in board:
        for j in i:
            if j == EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==None:
        return 0
    elif winner(board)==X:
        return 1

    return -1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        max = MAXVALUE(board)
        return max[0]
    else:
        min = MINVALUE(board)
        return min[0]

def MAXVALUE(board):
    if terminal(board):
        return [None,utility(board)]

    v = -99999999
    for a in actions(board):
        min = MINVALUE(result(board,a))
        if min[1]>v:
            v = min[1]
            act = a
    return [act,v]

def MINVALUE(board):
    if terminal(board):
        return [None,utility(board)]
    v = 99999999
    for a in actions(board):
        max = MAXVALUE(result(board,a))
        if max[1]<v:
            v = max[1]
            act = a
    return [act,v]

