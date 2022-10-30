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
    if board[pos1row][pos1column].colour != board[pos2row][pos2column].colour:
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
                    if board[pos1row + row][pos1column].piece == "empty":
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
    if not abs(pos1row - pos2row) == abs(pos1col - pos2col):
        return False
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
        if not abs(pos1row - pos2row) == abs(pos1col - pos2col): #queen moves were not working, might be a bad fix
            return False
        if diagonal_move(pos1row, pos1col, pos2row, pos2col, board):
            return True
        else:
            return False


def king_move(pos1row, pos1col, pos2row, pos2col, board):
    if board[pos2row][pos2col].colour == board[pos1row][pos1col].colour:
        return False
    # check_board = generate_checkboard(pos1row, pos1col, board)
    #    if check_check(pos2row, pos2col, check_board): moved this to main after king move
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


# the problem with this function is that as soon as we find one piece the function returns true, and does not check the rest
# first 2 arguments can be any position/future/present, returns true if any piece can move to the pos2row,pos2col given
def find_piece(piece:str,colour:str,check_board): #piece and colour passed in as strings
    piece_list = []
    for row in range(0, 8, 1):
        for col in range(0, 8, 1):
            if check_board[row][col].piece == piece and check_board[row][col].colour == colour:
                piece_list.append(row)
                piece_list.append(col)
            if row == 7 and col == 7:
                return piece_list # finds piece, returns list of the coordinates

def check_check(pos2row, pos2col, check_board,colour):# colour for check_check determines which pieces will try to move
    pawn_list = find_piece("P",colour,check_board)
    for i in range(0, len(pawn_list),2):
        if colour == "W":
            if validate_MoveWP(pawn_list[i],pawn_list[i+1],pos2row,pos2col,check_board):
                return True
            else:
                if validateMoveBP(pawn_list[i],pawn_list[i+1],pos2row,pos2col,check_board):
                    return True
    bishop_list = find_piece("B",colour,check_board)
    for i in range(0,len(bishop_list),2):
        if validate_bishop(bishop_list[i],bishop_list[i+1],pos2row,pos2col,check_board):
            return True
    rook_list = find_piece("R",colour,check_board)
    for i in range(0,len(rook_list),2):
        if validateMoveRK(rook_list[i],rook_list[i+1],pos2row,pos2col,check_board):
            return True
    knight_list = find_piece("N",colour,check_board)
    for i in range(0,len(knight_list),2):
        if validateMoveKnight(knight_list[i],knight_list[i+1],pos2row,pos2col,check_board):
            return True
    queen_list = find_piece("Q",colour,check_board)
    for i in range(0,len(knight_list),2):
        if validate_queen(queen_list[i], queen_list[i + 1], pos2row, pos2col, check_board):
            return True
    else:
        return False

def find_king_w(board):
    for row in range(0, 8, 1):
        for col in range(0, 8, 1):
            if board[row][col].piece == "K" and board[row][col].colour == "W":
                print(row)
                print(col)
                return row, col


def find_king_b(board):
    for row in range(0, 8, 1):
        for col in range(0, 8, 1):
            if board[row][col].piece == "K" and board[row][col].colour == "B":
                print(row)
                print(col)
                return row, col

def check_win(board,colour:str): #colour passed in as string, if white passed in we will check if white won
    check = False
    if colour == "W":
        king_list = find_piece("K","B",board)
    else:
        king_list = find_piece("K","W",board)
    if colour == "W":
        colour2 = "B"
    else:
        colour2 = "W"

    king_row = king_list[0]
    king_col = king_list[1]
    print(king_list)
    print(f"we are trying to move to {king_row},{king_col}")
    counter = 0
    checkboard = generate_checkboard(king_row,king_col,board)
    if check_check(king_row,king_col,checkboard,colour):
        check = True
    if king_row -1 > 7 or king_col-1 > 7 or king_row -1 < 0 or king_col-1 < 0:
        counter += 1
    else:
        checkboard = generate_checkboard(king_row - 1, king_col - 1, board)
        if check_check(king_row - 1, king_col - 1, checkboard,colour):
            counter += 1

    if king_row > 7 or king_col-1 > 7 or king_row < 0 or king_col-1 < 0:
        counter += 1
    else:
        checkboard = generate_checkboard(king_row, king_col - 1, board)
        if check_check(king_row, king_col - 1, checkboard,colour):
            counter += 1

    if king_row + 1 > 7 or king_col-1 > 7 or king_row + 1 < 0 or king_col-1 < 0:
        counter += 1
    else:
        checkboard = generate_checkboard(king_row + 1, king_col - 1, board)
        if check_check(king_row + 1, king_col - 1, checkboard,colour):
            counter += 1

    if king_row + 1 > 7 or king_col > 7 or king_row + 1 < 0 or king_col < 0:
        counter += 1
    else:
        checkboard = generate_checkboard(king_row + 1, king_col, board)
        if check_check(king_row + 1, king_col, checkboard,colour):
            counter += 1

    if king_row - 1 > 7 or king_col > 7 or king_row - 1 < 0 or king_col < 0:
        counter += 1
    else:
        checkboard = generate_checkboard(king_row - 1, king_col, board)
        if check_check(king_row - 1, king_col, checkboard,colour):
            counter += 1

    if king_row - 1 > 7 or king_col+1 > 7 or king_row -1  < 0 or king_col +1 < 0:
        counter += 1
    else:
        checkboard = generate_checkboard(king_row - 1, king_col + 1, board)
        if check_check(king_row - 1, king_col + 1, checkboard,colour):
            counter += 1


    if king_row > 7 or king_col+1 > 7 or king_row < 0 or king_col+1 < 0:
        counter += 1
    else:
        checkboard = generate_checkboard(king_row, king_col + 1, board)
        if check_check(king_row, king_col + 1, checkboard,colour):
            counter += 1

    if king_row + 1 > 7 or king_col +1 > 7 or king_row + 1 < 0 or king_col+1 < 0:
        counter += 1
    else:
        checkboard = generate_checkboard(king_row + 1, king_col + 1, board)
        if check_check(king_row + 1, king_col + 1, checkboard,colour):
            counter += 1

    if counter == 8 and  check == True:
        print(f"{colour} WINS")
        return True
    if counter == 8 and not check:
        print("Stalemate")
        return False
    else:
        print("hello")
        print(counter)
        return False
