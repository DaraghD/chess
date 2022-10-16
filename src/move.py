def validateMoveWP(pos1row, pos1column, pos2row, pos2column, board):
    if board[pos1row][pos1column] == "WP":
        if board[pos2row][pos2column] == 0:
            if pos2row == pos1row - 1 and pos2column == pos1column:
                return True
    else:
        return False
