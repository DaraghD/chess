from display import generate_checkboard


def validate_MoveWP(pos1row, pos1column, pos2row, pos2column, board):
    flagleft = 0
    flagright = 0
    if board[pos2row][pos2column].colour != "W":
        if not board[pos1row][pos1column].hasMoved:
            if pos2row == pos1row - 2:
                return True
        if board[pos1row - 1][pos1column - 1].colour == "B":
            flagleft = 1
        if board[pos1row - 1][pos1column + 1].colour == "B":
            flagright = 1
        if pos2row == pos1row - 1 and pos2column == pos1column - 1 and flagleft == 1:
            return True
        if pos2row == pos1row - 1 and pos2column == pos1column + 1 and flagright == 1:
            return True
        if pos2row == pos1row - 1:
            return True
        else:
            return False


def validateMoveBP(pos1row, pos1column, pos2row, pos2column, board):
    flagleft = 0
    flagright = 0
    if board[pos2row][pos2column].colour != "B":
        if not board[pos1row][pos1column].hasMoved:
            if pos2row == pos1row + 2:
                return True
        if board[pos1row + 1][pos1column - 1].colour == "W":
            flagleft = 1
        if board[pos1row + 1][pos1column + 1].colour == "W":
            flagright = 1
        if pos2row == pos1row + 1 and pos2column == pos1column - 1 and flagleft == 1:
            return True
        if pos2row == pos1row + 1 and pos2column == pos1column + 1 and flagright == 1:
            return True
        if pos2row == pos1row + 1:
            return True
        else:
            return False


def validateMoveKnight(pos1row, pos1column, pos2row, pos2column,  # pycharm formatting is why \
                       board):  # not seperate colour, can do this in the function
    # checks if piece moving to is not friendly or its empty

    if board[pos2row][pos2column].colour != board[pos1row][pos1column].colour:
        # 8 possible moves, using or operator to check, we know its empty cause of above^
        # up move /left right
        if pos2row == pos1row - 2 and pos2column == pos1column - 1 or pos2row == pos1row - 2 and pos2column == pos1column + 1:
            return True
        # right move , up down
        if pos2row == pos1row + 1 and pos2column == pos1column + 2 or pos2row == pos1row - 1 and pos2column == pos1column + 2:
            return True
        # down move, left right
        if pos2row == pos1row + 2 and pos2column == pos1column - 1 or pos2row == pos1row + 2 and pos2column == pos1column + 1:
            return True
        # left move, up , down
        if pos2row == pos1row - 1 and pos2column == pos1column - 2 or pos2row == pos1row + 1 and pos2column == pos1column - 2:
            return True
        else:
            return False
    else:
        return False


# for row in abs(pos1row, pos2row):
def validateMoveRK(pos1row, pos1column, pos2row, pos2column,
                   board):  # CASTLING NOT TAKEN INTO ACCOUNT (YET) .hasMoved with king.hasMoved mb

    if board[pos1row][pos1column].colour != board[pos2row][pos2column].colour:
        if abs(pos1row - pos2row) - 1 == 0:
            return True
        if abs(pos1column - pos2column) - 1 == 0:
            return True
        if pos1column == pos2column:  # we know if this is true its moving vertically
            if pos1row > pos2row:  # if this is true its moving "up" , white to black
                row = 0
                while row < abs(pos1row - pos2row) - 1:
                    row = row + 1
                    if board[pos1row - row][pos1column].piece == "empty":
                        if row == abs(pos1row - pos2row) - 1:
                            return True
                        continue
                    else:
                        return False

            if pos1row < pos2row:  # its moving down
                row = 0
                while row < abs(pos1row - pos2row) - 1:
                    row = row + 1
                    if board[pos1row + row][
                        pos1column].piece == "empty":  # empty as we already checked for attacking in first if statement
                        if row == abs(pos1row - pos2row) - 1:
                            return True
                        continue
                    else:
                        return False

        if pos1column < pos2column:  # its moving vertically and in this case right ->
            col = 0
            while col < abs(pos1column - pos2column) - 1:
                col = col + 1
                if board[pos1row][pos1column + col].piece == "empty":
                    if col == abs(pos1column - pos2column) - 1:
                        return True
                    continue
                else:
                    return False

        if pos1column > pos2column:  # moving <-
            col = 0
            print("test1")
            while col < abs(pos1column - pos2column) - 1:  #
                col = col + 1
                if board[pos1row][pos1column - col].piece == "empty":
                    print("first if")
                    if col == abs(pos1column - pos2column) - 1:
                        return True
                    continue
                else:
                    return False


"""""
def validateMoveB(pos1row,pos1column,pos2row,pos2column,board):
    if board[pos1row][pos1column].colour != board[pos2row][pos2column].colour or board[pos2row][
        pos2column].piece == "empty":
        if 
    else:
        return False
"""


# using snake case
# purpose of this function is too make bishop,rook,queen validate move functions more readable by isolating these checks in their own function
def line_move(pos1row, pos1column, pos2row, pos2column, board):  # this is a complete copy of the rk function
    if board[pos1row][pos1column].colour != board[pos2row][
        pos2column].colour:
        if abs(pos1row - pos2row) - 1 == 0:
            return True
        if abs(pos1column - pos2column) - 1 == 0:
            return True
        if pos1column == pos2column:
            if pos1row > pos2row:
                row = 0
                while row < abs(pos1row - pos2row) - 1:
                    row += 1
                    if board[pos1row - row][pos1column].piece == "empty":
                        if row == abs(pos1row - pos2row) - 1:
                            return True
                        continue
                    else:
                        return False

            if pos1row < pos2row:
                row = 0
                while row < abs(pos1row - pos2row) - 1:
                    row += 1
                    if board[pos1row + row][
                        pos1column].piece == "empty":
                        if row == abs(pos1row - pos2row) - 1:
                            return True
                        continue
                    else:
                        return False

        if pos1column < pos2column:
            col = 0
            while col < abs(pos1column - pos2column) - 1:
                col += 1
                if board[pos1row][pos1column + col].piece == "empty":
                    if col == abs(pos1column - pos2column) - 1:
                        return True
                    continue
                else:
                    return False

        if pos1column > pos2column:
            col = 0
            print("hello")
            while col < abs(pos1column - pos2column) - 1:  #
                col += 1
                if board[pos1row][pos1column - col].piece == "empty":
                    print("first if")
                    if col == abs(pos1column - pos2column) - 1:
                        return True
                    continue
                else:
                    return False


def diagonal_move(pos1row, pos1col, pos2row, pos2col, board):
    tile_gap = abs(pos1row - pos2row) - 1
    if board[pos1row][pos1col].colour != board[pos2row][pos2col].colour:
        if tile_gap == 0 and pos1row != pos2row and pos1col != pos2col:
            return True
        # 4 possibilites for direction
        if pos1row > pos2row and pos1col > pos2col:  # up and left
            for i in range(1, tile_gap, 1):  # starts at 1, tile_gap times, 1 increment
                if board[pos1row - i][pos1col - i].piece == "empty":
                    continue
                else:
                    return False
            return True
        if pos1row > pos2row and pos1col < pos2col:  # up and right
            for i in range(1, tile_gap, 1):
                if board[pos1row - i][pos1col + i].piece == "empty":
                    continue
                else:
                    return False
            return True
        if pos1row < pos2row and pos1col > pos2col:  # down and left
            for i in range(1, tile_gap, 1):
                if board[pos1row + i][pos1col - i].piece == "empty":
                    continue
                else:
                    return False
            return True
        if pos1row < pos2row and pos1col < pos2col:  # down and right
            for i in range(1, tile_gap, 1):
                if board[pos1row + i][pos1col + i].piece == "empty":
                    continue
                else:
                    return False
            return True

    else:
        return False


def validate_bishop(pos1row, pos1col, pos2row, pos2col,
                    board):  # maybe redundant - might help with readability in main.
    if diagonal_move(pos1row, pos1col, pos2row, pos2col, board):
        return True
    else:
        return False


def validate_queen(pos1row, pos1col, pos2row, pos2col, board):
    if pos1row == pos2row or pos1col == pos2col:
        if line_move(pos1row, pos1col, pos2row, pos2col, board):
            return True
        else:
            return False
    if not pos1row == pos2row or pos1col == pos2col:
        if diagonal_move(pos1row, pos1col, pos2row, pos2col, board):
            return True
        else:
            return False


def king_move(pos1row, pos1col, pos2row, pos2col, board):
    if board[pos2row][pos2col].colour == board[pos1row][pos1col].colour:
        return False
    check_board = generate_checkboard(pos1row, pos1col, board)
    #    if check_check(pos2row, pos2col, check_board):
    #       print("MOVE WOULD PUT IN CHECK")
    #      return False
    if abs(pos1row - pos2row) == 1:
        if abs(pos1col - pos2col) == 1:
            return True

    elif pos1row == pos2row:
        if abs(pos1col - pos2col) == 1:
            return True

    elif pos1col == pos2col:
        if abs(pos1row - pos2row) == 1:
            return True

    return False


def check_check(pos2row, pos2col,
                check_board):  # first 2 arguments can be any position/future/present, returns true if any piece can move to the pos2row,pos2col given
    i = 0
    x = 0
    for row in check_board:
        for col in row:
            match col.colour:
                case 'B':
                    match col.piece:
                        case 'Q':
                            if validate_queen(i, x, pos2row, pos2col, check_board):
                                return True
                        case 'B':
                            if validate_bishop(i, x, pos2row, pos2col, check_board):
                                return True
                        case 'P':
                            if validateMoveBP(i, x, pos2row, pos2col, check_board):
                                return True
                        case 'N':
                            if validateMoveKnight(i, x, pos2row, pos2col, check_board):
                                return True
                        case 'R':
                            if validateMoveRK(i, x, pos2row, pos2col, check_board):
                                return True
                        case 'K':
                            if king_move(i, x, pos2row, pos2col, check_board):
                                return True


def find_king_w(board):
    for row in range(0, 9, 1):
        for col in range(0, 8, 1):
            if board[row][col].piece == "K" and board[row][col].colour == "W":
                print(row)
                print(col)
                return row, col


def find_king_b(board):
    for row in range(0, 9, 1):
        for col in range(0, 8, 1):
            if board[row][col].piece == "K" and board[row][col].colour == "B":
                print(row)
                print(col)
                return row, col


def check_win_black(board):  # checks legal moves for king, 8 possible moves with king, checks if black won
    king_pos = find_king_w(board)
    king_row = king_pos[0]
    king_col = king_pos[1]
    print(king_pos)
    if check_check(king_row, king_col,board):  # checking all 8 possible moves for king, if any are true return false as king is not in checkmate
        if check_check(king_row - 1, king_col - 1, board):
            return False
        if check_check(king_row, king_col - 1, board):
            return False
        if check_check(king_row + 1, king_col - 1, board):
            return False
        if check_check(king_row + 1, king_col, board):
            return False
        if check_check(king_row - 1, king_col, board):
            return False
        if check_check(king_row - 1, king_col + 1, board):
            return False
        if check_check(king_row, king_col + 1, board):
            return False
        if check_check(king_row + 1, king_col + 1, board):
            return False
        else:
            return True  # if king has no possible moves and check== true , checkmate

    else:
        return False


"""""
def check_win_white(board): checks if white won
    king_pos = find_king_b(board)
    king_row = king_pos[0]
    king_col = king_pos[1]
    print(king_pos)

    if check_check(wking_row, wking_col, board):
        if check_check(king_row - 1, king_col - 1, board):
            return False
        if check_check(king_row, king_col - 1, board):
            return False
        if check_check(king_row + 1, king_col - 1, board):
            return False
        if check_check(king_row + 1, king_col, board):
            return False
        if check_check(king_row - 1, king_col, board):
            return False
        if check_check(king_row - 1, king_col + 1, board):
            return False
        if check_check(king_row, king_col + 1, board):
            return False
        if check_check(king_row + 1, king_col + 1, board):
            return False
        else:
            return True  # if king has no possible moves and check== true , checkmate

    else:
        return False
"""""
