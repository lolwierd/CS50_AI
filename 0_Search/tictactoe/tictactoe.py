"""
Tic Tac Toe Player
"""

import math
import copy

# states of a block
X = "X"
O = "O"
E = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[E, E, E], [E, E, E], [E, E, E]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    # Number of X's on the board
    num_x = 0
    # Number of O's on the board
    num_o = 0
    # Number of empty tiles on the board
    num_empty = 0

    # Checks if the board is empty
    is_empty = all(state == E for row in board for state in row)

    if is_empty:
        return X
    for row in board:
        for state in row:
            if state is X:
                num_x += 1
            elif state is O:
                num_o += 1
            else:
                num_empty += 1
    if num_empty == 0:
        return None
    return X if num_x <= num_o else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    set_of_actions = set()
    # Return None if the board is terminal
    if terminal(board):
        return None

    for row_index, row in enumerate(board):
        for cell_index, state in enumerate(row):
            if state == E:
                set_of_actions.add((row_index, cell_index))
    return set_of_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]
    # Make a deep copy of the board
    board_copy = copy.deepcopy(board)
    # Get whose turn it is
    turn = player(board)
    # Invalid action on the board
    if board_copy[i][j] != E:
        raise Exception("Invalid Action on Board!!")
    # Update the board state with action
    board_copy[i][j] = turn
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check if the board is empty
    is_empty = all(state == E for row in board for state in row)
    if is_empty:
        return None

    # Check diagonals
    diagonals = get_diagonals(board)
    if diagonals[0].count(X) == 3 or diagonals[0].count(O) == 3:
        return diagonals[0][0]
    if diagonals[1].count(X) == 3 or diagonals[1].count(O) == 3:
        return diagonals[1][1]

    # Check rows
    for row in board:
        if row.count(X) == 3 or row.count(O) == 3:
            return row[0]

    # Check columns
    # zip(*board) returns the transpose of board
    for column in zip(*board):
        if column.count(X) == 3 or column.count(O) == 3:
            return column[0]

    # This means no winner found
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Return True if all tiles are not Empty
    is_not_empty = all(state != E for row in board for state in row)
    if is_not_empty:
        return True

    # Check if winner exists, If it exists, game is over.
    return True if winner(board) else False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return 1 if winner(board) is X else -1 if winner(board) is O else 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    actions_for_board = actions(board)
    return actions_for_board.pop()


def get_diagonals(board):
    return [(board[0][0], board[1][1], board[2][2]), (board[0][2], board[1][1], board[2][0])]
