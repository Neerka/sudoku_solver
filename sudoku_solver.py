full_set = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

sudoku_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]


def com_val(list1, list2: list) -> list:
    '''
    Function gets two lists:
    - function returns a list with common values of both given lists.
    '''
    common = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2 and item1 not in common:
                common.append(item1)
    return common


def check_horizontal(array: list) -> list:
    '''
    Function gets a row of sudoku board:
    - function checks what values from full_set aren't in the following row;
    - function adds found values to the "possible" list;
    - function returns the "possible" list.
    '''
    possible = []
    for value in full_set:
        if value not in array:
            possible.append(value)
    return possible


def check_vertical(array: list, column: int) -> list:
    '''
    Function gets a whole sudoku board and an index of a column to check:
    - function makes a list based on values from given column;
    - function checks which of full_set values are not in the column;
    - function returns a list of possible results.
    '''
    checking_array = []
    possible = []
    for row in array:
        checking_array.append(row[column])
    for item in full_set:
        if item not in checking_array:
            possible.append(item)
    return possible


def check_square(array: list, row, column: int) -> list:
    '''
    Function gets a sudoku board, a number of a column and a row:
    - function searches for possible numbers based on given arguments;
    - function operates on a field defined by one of nine small sudoku squares;
    - function returns a list of possible results.
    '''
    sections = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    checking_array = []
    possible = []
    for x in range(3):
        if row in sections[x]:
            start_r, end_r = sections[x][0], sections[x][-1] + 1
        if column in sections[x]:
            start_c, end_c = sections[x][0], sections[x][-1] + 1
    for i in range(start_r, end_r):
        for j in range(start_c, end_c):
            checking_array.append(array[i][j])
    for item in full_set:
        if item not in checking_array:
            possible.append(item)
    return possible


def sudoku_solve(board: list) -> str:
    '''
    Function gets an unfinished 9x9 two-dimensional list (sudoku board):
    - function solves given sudoku;
    - function returns nothing, just edits given list;
    - works for lists with one possible solution only.
    '''
    while True:
        for row in range(9):
            for column in range(9):
                if board[row][column] == '.':
                    set1 = check_horizontal(board[row])
                    set2 = check_vertical(board, column)
                    set3 = check_square(board, row, column)
                    possible_args = com_val(com_val(set1, set2), set3)
                    if len(possible_args) == 1:
                        board[row][column] = possible_args[0]
        count = 0
        for row in board:
            for value in row:
                if value == '.':
                    count += 1
        if count == 0:
            break
    return 'Nothing'


sudoku_solve(sudoku_board)

for row in sudoku_board:
    print(row)
