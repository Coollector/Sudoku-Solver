def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        solved, board = solve(board)
                        if solved:
                            return [True, board]
                        board[i][j] = 0
                return [False, board]
    print_board(board)
    quit()

    
def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    for i in range(9):
        if board[i][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def print_board(bo):
    print("\n\n")
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" | ", end="")
            
            if j == 8:
                print(bo[i][j], end="\n")
            else:
                print(str(bo[i][j]) + " ", end="")

def replace_function(ctx:str):
    return [int(i) for i in ctx.replace(' ', '').split(',')]

def board_input():
    print('please enter the rows of the sudoku like this: 1, 2, 3, 4, 0(if the field is empty), 5, 6, 7, 8:\n\n')
    row_1 = replace_function(input())
    row_2 = replace_function(input())
    row_3 = replace_function(input())
    row_4 = replace_function(input())
    row_5 = replace_function(input())
    row_6 = replace_function(input())
    row_7 = replace_function(input())
    row_8 = replace_function(input())
    row_9 = replace_function(input())
    board_prev = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9]
    return board_prev


board = board_input()

solution = solve(board)
