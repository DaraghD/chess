def validateMoveWP(pos1row, pos1column, pos2row, pos2column, board):
    if board[pos1row][pos1column].hasMoved and pos2row == pos1row - 2 and pos1column == pos2column:
        return False
    if board[pos1row][pos1column].hasMoved == False and pos2row == pos1row - 2 and \
            board[pos2row][pos2column].piece == "empty":
        board[pos1row][pos1column].hasMoved = True
        return True  # this is for "double jump"
    elif pos2row == pos1row - 1 and board[pos2row][pos2column].piece == "empty":
        board[pos1row][pos1column].hasMoved = True
        return True  # this is for moving 1 up, checks if piece moving to is 1 from the pawn, and if its empty
    elif board[pos2row][pos2column].colour == "B" and board[pos2row][pos2column] == board[pos1row - 1][
        pos1column + 1]:  # right attack
        board[pos1row][pos1column].hasMoved = True
        return True
    elif board[pos2row][pos2column].colour == "B" and board[pos2row][pos2column] == board[pos1row - 1][
        pos1column - 1]:  # left attack
        board[pos1row][pos1column].hasMoved = True
        return True
    else:
        return False


def validateMoveBP(pos1row, pos1column, pos2row, pos2column, board):
    # assuming it is a blackpawn{not checking this}
    if board[pos1row][
        pos1column].hasMoved and pos2row == pos1row - 2 and pos1column == pos2column:  # check column aswell?
        return False
    elif board[pos1row][pos1column].hasMoved == False and board[pos2row][pos2column] == board[pos1row + 2][
        pos2column] and \
            board[pos2row][pos2column].piece == "empty":
        board[pos1row][pos1column].hasMoved = True
        return True  # this is for "double jump"
    elif board[pos2row][pos2column] == board[pos1row + 1][pos1column] and board[pos2row][pos2column].piece == "empty":
        board[pos1row][pos1column].hasMoved = True
        return True  # this is for moving 1 up, checks if piece moving to is 1 from the pawn, and if its empty
    elif board[pos2row][pos2column].colour == "W" and board[pos2row][pos2column] == board[pos1row + 1][
        pos1column + 1]:  # right attack
        board[pos1row][pos1column].hasMoved = True
        return True
    elif board[pos2row][pos2column].colour == "W" and board[pos2row][pos2column] == board[pos1row + 1][
        pos1column - 1]:  # left attack
        board[pos1row][pos1column].hasMoved = True
        return True
    else:
        return False


def validateMoveKnight(pos1row, pos1column, pos2row, pos2column,  # pycharm formatting is why \
                       board):  # not seperate colour, can do this in the function
    # checks if piece moving to is not friendly or its empty
    if board[pos2row][pos2column].colour != board[pos1row][pos1column].colour:
        # 8 possible moves, using or operator to check, we know its empty cause of above^
        # up move /left right
        if board[pos2row][pos2column] == board[pos1row - 2][pos1column - 1] or board[pos2row][pos2column] == \
                board[pos1row - 2][pos1column + 1]:
            return True
        # right move , up down
        if board[pos2row][pos2column] == board[pos1row + 1][pos1column + 2] or board[pos2row][pos2column] == \
                board[pos1row - 1][pos1column + 2]:
            return True
        # down move, left right
        if board[pos2row][pos2column] == board[pos1row + 2][pos1column - 1] or board[pos2row][pos2column] == \
                board[pos1row + 2][pos1column + 1]:
            return True
        # left move, up , down
        if board[pos2row][pos2column] == board[pos1row - 1][pos1column - 2] or board[pos2row][pos2column] == \
                board[pos1row + 1][pos1column - 2]:
            return True
        else:
            return False
    else:
        return False


# for row in abs(pos1row, pos2row):
def validateMoveRK(pos1row, pos1column, pos2row, pos2column,
                   board):  # CASTLING NOT TAKEN INTO ACCOUNT (YET) .hasMoved with king.hasMoved mb

    if board[pos1row][pos1column].colour != board[pos2row][
        pos2column].colour:
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

        if pos1column > pos2column:  #  moving <-
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
def validate_bishop(pos1row,pos1col,pos2row,pos2col,board): # maybe redundant - might help with readability in main.
    if diagonal_move(pos1row,pos1col,pos2row,pos2col,board):
        return True
    else:
        return False

def validate_queen(pos1row,pos1col,pos2row,pos2col,board):
    if pos1row == pos2row or pos1col == pos2col:
        if line_move(pos1row,pos1col,pos2row,pos2col,board):
            return True
        else:
            return False
    if not pos1row == pos2row or pos1col == pos2col:
        if diagonal_move(pos1row,pos1col,pos2row,pos2col,board):
            return True
        else:
            return False

def king_move(pos1row, pos1col, pos2row, pos2col, board):
    if board[pos2row][pos2col].colour == board[pos1row][pos1col].colour:
        return False
    if check_check(pos2row,pos2col,board):
        print("MOVE WOULD PUT IN CHECK")
        return False
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
def check_check(pos2row, pos2col, board):
    for row in board:
        for col in row:
            col1 = enumerate(col)
            row1 =enumerate(row)
            if col.colour == "B":
                if col.piece == "Q":
                        if validate_queen(row1,col1,pos2row,pos2col,board):
                            print(1)
