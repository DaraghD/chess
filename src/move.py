from dataclasses import dataclass


def validateMoveWP(pos1row, pos1column, pos2row, pos2column, board):
    if board[pos1row][pos1column].hasMoved == False and board[pos2row][pos2column] == board[pos1row - 1][pos2column] and \
            board[pos2row][pos2column].piece == "empty":
        board[pos1row][pos1column].hasMoved = True
        return True  # this is for "double jump"
    elif board[pos2row][pos2column] == board[pos1row - 1][pos1column] and board[pos2row][pos2column].piece == "empty":
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


# def validateMoveWK(pos1row, pos1column, pos2row, pos2column, board):

# WK = White knight, should work for BK aswell- can move in any direction// this function needs to be redone
def validateMoveBP(pos1row, pos1column, pos2row, pos2column, board):
    # assuming it is a blackpawn{not checking this}
    if board[pos1row][pos1column].hasMoved == False and board[pos2row][pos2column] == board[pos1row + 2][pos2column] and \
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
