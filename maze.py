
"""
This is a rat maze also solved using backtracking
The rules are simple:
    1.) The rat moves either right or down
    2.) The rat starts at index (0, 0) and shall end at
        last index of the last array
    3.) Path covered shall be marked using "2"
"""

maze = [
    [2, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
]


def printMaze():
    print('\nRat Maze\n')
    for row in maze:
        for element in row:
            print(element, ' ', end='')
        print('')
    print('')


"""
Base Case/Goal State:
    -Last index of last array
Choices:
    -right or down of current position
Constraints:
    -can't pass through a wall
"""



