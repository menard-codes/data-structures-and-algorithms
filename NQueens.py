
"""
Backtracking Algorithm:
1.) Brute Force Approach (Try out all possible solutions and pick up the desired ones.)
2.) Bounding function (needs to satisfy the constraint/condition)

Backtracking is not for optimization.
Backtracking is used when you have multiple solutions and you want all those solutions.

Choice, Constraints, Goal


##############################
Here's my thought of How to design a backtracking algorithm:
        Since it is a form of recursion, the first thing to do is define the base case
    and recursive case clearly.
        And from there, you tell the decision points on which affects the input for
    the next recursive call wherein based on that input, tells if it arrived already
    at the base case or not, or it needs to go back to a previous recursive call
    (hence, to backtrack). Because that's the essence of manipulating the input,
    to make it fall into the base case primarily (or backtrack from a certain decision
    point) so that the recursive case terminates.
#############################


"""


def print_board(board):
    for row in board:
        print(row)
    print('')


def safe_on_column(board, col):
    """
    :param board: accepts the current board
    :param col: accepts an int which represents an index position
                in an array to represent a column in the board.
                Also the X-Axis
    :return: Boolean value telling if a queen is found on a specific column
    """
    for row in board:
        if row[col] == 1:
            return False
    return True


def safe_on_diagonal(board, col, row):
    """
    :param board: Accepts a 2D array representing the current board
    :param col: Accepts an int value for an index position representing the column
                where the current queen is on the board. Also the X-Axis
    :param row: Accepts an int value for an index position representing the row
                where the current queen is on the board. Also the Y-Axis.
    :return: Boolean value telling if one or more queen were found on a diagonal
    """
    # This will be divided into 4 diagonals: top left, top right, bottom left, bottom right

    # first, the top left diagonal. Both row & column decreases
    for r, c in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[r][c] == 1:
            return False

    # second, the top right diagonal. Row decreasing, column increasing
    for r, c in zip(range(row-1, -1, -1), range(col+1, len(board))):
        if board[r][c] == 1:
            return False

    # third, the bottom left diagonal. Row increasing, column decreasing
    for r, c in zip(range(row+1, len(board)), range(col-1, -1, -1), ):
        if board[r][c] == 1:
            return False

    # lastly, the bottom right diagonal. Both row & column increases
    for r, c in zip(range(row+1, len(board)), range(col+1, len(board))):
        if board[r][c] == 1:
            return False

    return True


def safe_in(board, col, row):
    """
    Checks whether a coordinate within a board is safe.
    :param board: Accepts the current board as a 2D Array
    :param col: Accepts an int value which represents the index of a
                list representing a column of current position.
    :param row: Accepts an int value which represents the index of a
                list representing a row within 2D Array of current position.
    :return: Boolean value if a queen is safe on a given coordinate.
    """
    if safe_on_column(board, col):
        return safe_on_diagonal(board, col, row)
    return False


def NQueens(board, _row=0, _len_of_board=None):
    """
    Solves the N-Queens problem and prints all the possible
    solutions for a given NxN board.

    What is N-Queens problem?
        Given an NxN chess board, place N queens in the board
        without each queen attacking the other.
    :param board: Accepts the current board as a 2D Array.
                  Board size should be more than or equals to 4.
    :param _row: Accepts an int value representing an index
                 within a 2D array for current row. Private
                 argument, shouldn't be used outside the function.
    :param _len_of_board: Accepts length of current board.
                         Private Argument. Shouldn't be used outside
                         this function.
    :return: None. Just prints the solved boards.
    """
    if _len_of_board is None:
        _len_of_board = len(board)

    # The Base Case/Goal State
    if _row == _len_of_board:
        print_board(board)
        return

    # The recursive case. Scan each col of a row.
    for col in range(_len_of_board):
        # The constraint. If safe, place the queen and move on.
        if safe_in(board, col, _row):
            board[_row][col] = 1
            if NQueens(board, _row+1, _len_of_board):
                continue
            board[_row][col] = 0


myBoard = [[0 for _ in range(4)] for _ in range(4)]

print_board(myBoard)

NQueens(myBoard)
