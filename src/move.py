from dataclasses import dataclass


def validateMoveWP(pos1row, pos1column, pos2row, pos2column, board):  # 0 = black, 1 = white
    flagleft = False
    flagright = False
    if board[pos1row][pos1column].piece == "P" and board[pos1row][
        pos1column].colour == "white":  # checks if its whitepawn
        if board[pos1row][pos1column].hasMoved == False:
            if board[pos2row][pos2column] == board[pos1row - 2][pos2column]:
                board[pos1row][pos1column].hasMoved = True
                return True
        else:
            print("has moved is true??")
        if board[pos1row - 1][pos1column - 1].colour == "black":  # checks if blackpiece is in capture  range
            flagleft = True
        if board[pos1row - 1][pos1column + 1].colour == "black":
            flagright = True
        if board[pos2row][pos2column].piece == "empty":
            if pos2row == pos1row - 1 and pos2column == pos1column:
                return True
    if flagleft or flagright:
        if board[pos2row][pos2column] == board[pos1row - 1][pos1column - 1] and flagleft:
            return True
        else:
            if board[pos2row][pos2column] == board[pos1row - 1][pos1column + 1] and flagright:
                return True
            else:
                return False
    else:
        return False


def validateMoveBP(pos1row, pos1column, pos2row, pos2column, board):
    flagleftB = False
    flagrightB = False

    if board[pos1row][pos1column].colour == 0 and board[pos1row][pos1column].piece == "P":
        if board[pos1row][pos1column].hasMoved == False:
            if board[pos2row][pos2column] == board[pos1row + 2][pos2column] and board[pos2row][pos2column].piece == \
                    "empty":
                board[pos1row][pos1column].hasMoved = True
                return True
        if board[pos1row+1][pos1column] == board[pos2row][pos2column] and board[pos2row][pos2column].piece == "empty":
            return True
        if board[pos1row + 1][pos1column - 1].piece == "P" and board[pos1row + 1][pos1column - 1].colour == "white":
            flagleftB = True
        if board[pos1row + 1][pos1column + 1].piece == "P" and board[pos1row + 1][pos1column + 1].colour == "white":
            flagrightB = True
        if board[pos2row][pos2column] == board[pos1row + 1][pos1column] and board[pos2row][pos2column].colour == "black":
            return False
        if board[pos2row][pos2column].piece == "empty":
            if pos2row == pos1row + 1 and pos2column == pos1column:
                return True
    if flagleftB or flagrightB:
        if board[pos2row][pos2column] == board[pos1row + 1][pos1column - 1] and flagleftB:
            print("yOU KILLED HIM POGGERS")
            return True
        else:
            if board[pos2row][pos2column] == board[pos1row + 1][pos1column + 1] and flagrightB:
                print("yOU KILLED HIM POGGERS")
                return True
            else:
                return False
    else:
        return False

# def validateMoveWK(pos1row, pos1column, pos2row, pos2column, board):

# WK = White knight, should work for BK aswell- can move in any direction// this function needs to be redone
