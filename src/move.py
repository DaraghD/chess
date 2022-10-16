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
        if board[pos1row+1][pos1column-1] == "WP":
            flagleftB = True
        if board[pos1row+1][pos1column+1] == "WP":
            flagrightB = True
        if board[pos2row][pos2column] == 0:
            if pos2row == pos1row+1 and pos2column == pos1column:
                return True
    if flagleftB or flagrightB:
        if board[pos2row][pos2column] == board[pos1row +1][pos1column-1] and flagleftB:
            return True
        else:
            if board[pos2row][pos2column] == board[pos1row +1][pos1column +1] and flagrightB:
                return True
            else:
                return False
    else:
        return False
