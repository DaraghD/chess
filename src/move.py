from dataclasses import dataclass

@dataclass
class Piece:
    colour: int
    piece: int
    hasMoved: bool
    rank: int


def validateMoveWP(pos1row, pos1column, pos2row, pos2column, board):
    flagleft = False
    flagright = False
    if board[pos1row][pos1column] == "WP":
        if board[pos1row - 1][pos1column - 1] == "BP":
            flagleft = True
        if board[pos1row - 1][pos1column + 1] == "BP":
            flagright = True
        if board[pos2row][pos2column] == 0:
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
    if board[pos1row][pos1column] == "BP":
        if board[pos1row + 1][pos1column - 1] == "WP":
            flagleftB = True
        if board[pos1row + 1][pos1column + 1] == "WP":
            flagrightB = True
        if board[pos2row][pos2column] == board[pos1row+1][pos1column] and isinstance(board[pos2row][pos2column],str):
            return False
        if board[pos2row][pos2column] == 0:
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

#enum with 0,1 -black or white, and piece. also isFirstmove boolean - for pawns
def validateMoveWK(pos1row, pos1column, pos2row, pos2column, board): #WK = White knight, should work for BK aswell- can move in any direction
    flagattack1 = False  # starts at 12 (up left) rotates clockwise
    flagattack2 = False
    flagattack3 = False
    flagattack4 = False
    flagattack5 = False
    flagattack6 = False
    flagattack7 = False
    flagattack8 = False

    if board[pos1row][pos1column] == "WK":
        #new data type / enum for black piece instead of wk or bp or ....
        # verifies that there is a white piece on the tile they want to move,possible attacking tiles for knight
        if board[pos1row - 2][pos1column - 1] == "BP":  # black piece e.g bp or bk or ...
            flagattack1 = True
        if board[pos1row - 2][pos1column + 1] == "BP":
            flagattack2 = True
        if board[pos1row + 1][pos1column + 2] == "BP":
            flagattack3 = True
        if board[pos1row - 1][pos1column + 2] == "BP":
            flagattack4 = True
        if board[pos1row+2][pos1column+1] == "BP":
            flagattack5 = True
        if board[pos1row+2][pos1column-1] == "BP":
            flagattack6 = True
        if board[pos1row+1][pos1column-2] == "BP":
            flagattack7 = True
        if board[pos1row-1][pos1column-2] == "BP":
            flagattack8 = True

