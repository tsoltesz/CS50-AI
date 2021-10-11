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
    
    #ST
    
    num_X=0
    num_O=0
    for row in board:
        for players in row:
            if players==X:
                num_X+=1
            elif players==O:
                num_O+=1
    if (num_X>num_O):
        return O
    else:
        return X
    
    ###
    #raise NotImplementedError

    #/ST


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    #ST
    moves = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                moves.add((i,j))
    return moves
    ###
    #raise NotImplementedError

    #/ST


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    #ST
    if (board[action[0]][action[1]] is not None):
        raise NameError("Invalid action")
    else:
        new_board=copy.deepcopy(board)
        new_board[action[0]][action[1]]=player(new_board)
        return new_board
    
    ###
    #raise NotImplementedError
    #/ST

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    #ST
    for i in range (0,len(board)):
        if (board[i][0]!=EMPTY and board[i][0]==board[i][1] and board[i][0]==board[i][2]):
            return board[i][0]
    for j in range (0,len(board[0])):
        if (board[0][j]!=EMPTY and board[0][j]==board[1][j] and board[1][j]==board[2][j]):
            return board[0][j]
    if board[1][1]!=EMPTY and ((board[0][0]==board[1][1] and board[1][1]==board[2][2]) or (board[0][2]==board[1][1] and board[1][1]==board[2][0])):
        return board[1][1]
    return None
        
    ###
    #raise NotImplementedError
    #/ST

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    #ST

    if winner(board)is not None :
        return True
    for i in range (0,len(board)):
        for cell in board[i]:
            if cell==None:
                return False
    return True

    ###
    #raise NotImplementedError
    #/ST

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    #ST
    if terminal(board):
        if (winner(board)==X):
            return 1
        if (winner(board)==O):
            return -1
        else:
            return 0

    ###
    #raise NotImplementedError
    #/ST

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    #ST

    if terminal(board):
        return None
    if board==initial_state():
        return (1,1)
    moves=actions(board)
    results=[]
    for move in moves:
        new_board=result(board,move)
        results.append(minimax_utility(new_board))
    value=None
    index=None
    if player(board)==X:
        value=max(results)
        index=results.index(value)
    else:
        value=min(results)
        index=results.index(value)
    counter=0
    for move in moves:
        if (index==counter):
            return move
        counter+=1
    return None
def minimax_utility(board):
    if terminal(board):
        return utility(board)
    moves=actions(board)
    results=[]
    for move in moves:
        new_board=result(board,move)
        results.append(minimax_utility(new_board))
    value=None
    if player(board)==X:
        value=max(results)
    else:
        value=min(results)
    return value
    
    
    ###
    #raise NotImplementedError
    #/ST
