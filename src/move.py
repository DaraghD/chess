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
