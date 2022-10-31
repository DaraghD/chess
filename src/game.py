import user
from move import *
import bmove
from display import *

# bking_col = 4
# bking_row = 0
# wking_row = 7
# wking_col = 4
# initial king positions
def singleplayer():
    board = generate()

    while True:
        p1moved = 0

        show_emoji(board)
        while p1moved == 0:

            pos1row = (int(input("Enter the rank for piece to move:")) - 1)
            pos1col = input("Enter the file for piece to move:").upper()
            pos2row = (int(input("Enter the rank for square to move:")) - 1)
            pos2col = input("Enter the file for square to move:").upper()
            pos1col = col_dict[pos1col]
            pos2col = col_dict[pos2col]
            match board[pos1row][pos1col].colour:
                case "W":
                    match board[pos1row][pos1col].piece:
                        case "P":
                            if validate_MoveWP(pos1row, pos1col, pos2row, pos2col, board):
                                board[pos1row][pos1col].hasMoved = True
                                board[pos2row][pos2col] = board[pos1row][
                                    pos1col]  # replaces square moved to with this piece chosen
                                board[pos1row][pos1col] = Empty
                                p1moved = 1
                                if pos2row == 0:
                                    board[pos2row][pos2col] = WQueen
                                continue
                            else:
                                print("invalid")
                        case "N":
                            if validateMoveKnight(pos1row, pos1col, pos2row, pos2col, board):
                                print("done")
                                board[pos2row][pos2col] = board[pos1row][pos1col]
                                board[pos1row][pos1col] = Empty
                                p1moved = 1
                                continue
                        case "R":
                            if validateMoveRK(pos1row, pos1col, pos2row, pos2col, board):
                                board[pos2row][pos2col] = board[pos1row][pos1col]
                                board[pos1row][pos1col] = Empty
                                p1moved = 1
                                continue
                            else:
                                print("Invalid move")
                        case "Q":
                            if validate_queen(pos1row, pos1col, pos2row, pos2col, board):
                                board[pos2row][pos2col] = board[pos1row][pos1col]
                                board[pos1row][pos1col] = Empty
                                p1moved = 1
                                continue
                            else:
                                print("Invalid move")
                        case "B":
                            if validate_bishop(pos1row, pos1col, pos2row, pos2col, board):
                                board[pos2row][pos2col] = board[pos1row][pos1col]
                                board[pos1row][pos1col] = Empty
                                p1moved = 1
                                continue
                        case "K":
                            check_board = generate_checkboard(pos1row, pos1col, board)
                            if check_check(pos2row, pos2col, check_board,"B"):
                                print("Invalid move, would put in check")
                            else:
                                if king_move(pos1row, pos1col, pos2row, pos2col, board):
                                    wking_col = pos1col
                                    wking_row = pos1row
                                    board[pos2row][pos2col] = board[pos1row][pos1col]
                                    board[pos1row][pos1col] = Empty
                                    p1moved = 1
                                    continue
                                else:
                                    print("Invalid move")

        # bblackmove(board)

        clear()
        # new_board = display.new_board(board)
        # display.show_debug(new_board)
        # display.show(board)
        show_emoji_black(board)

        p2moved = 0

        while p2moved == 0:
            pos1row = (int(input("Enter the rank for piece to move:")) - 1)
            pos1col = input("Enter the file for piece to move:").upper()
            pos2row = (int(input("Enter the rank for square to move:")) - 1)
            pos2col = input("Enter the file for square to move:").upper()
            pos1col = col_dict[pos1col]
            pos2col = col_dict[pos2col]

            match board[pos1row][pos1col].colour:
                case "B":
                    match board[pos1row][pos1col].piece:
                        case "P":
                            if validateMoveBP(pos1row, pos1col, pos2row, pos2col, board):
                                board[pos1row][pos1col].hasMoved = True
                                board[pos2row][pos2col] = board[pos1row][
                                    pos1col]  # replaces square moved to with this piece chosen
                                board[pos1row][pos1col] = Empty

                                p2moved = 1
                                if pos2row == 7:
                                    board[pos2row][pos2col] = BQueen
                                continue
                            else:
                                print("invalid")
                        case "N":
                            if validateMoveKnight(pos1row, pos1col, pos2row, pos2col, board):
                                print("done")
                                board[pos2row][pos2col] = board[pos1row][pos1col]
                                board[pos1row][pos1col] = Empty
                                p2moved = 1
                                continue
                        case "R":
                            if validateMoveRK(pos1row, pos1col, pos2row, pos2col, board):
                                board[pos2row][pos2col] = board[pos1row][pos1col]
                                board[pos1row][pos1col] = Empty
                                p2moved = 1
                                continue
                            else:
                                print("Invalid move")
                        case "Q":
                            if validate_queen(pos1row, pos1col, pos2row, pos2col, board):
                                board[pos2row][pos2col] = board[pos1row][pos1col]
                                board[pos1row][pos1col] = Empty
                                p2moved = 1
                                continue
                            else:
                                print("Invalid move")
                        case "B":
                            if validate_bishop(pos1row, pos1col, pos2row, pos2col, board):
                                board[pos2row][pos2col] = board[pos1row][pos1col]
                                board[pos1row][pos1col] = Empty
                                p2moved = 1
                                continue
                        case "K":
                            check_board = generate_checkboard(pos1row, pos1col, board)
                            if check_check(pos2row, pos2col, check_board,"W"):
                                print("Invalid move, would put in check")
                            else:
                                if king_move(pos1row, pos1col, pos2row, pos2col, board):
                                    bking_col = pos1col
                                    bking_row = pos1row
                                    board[pos2row][pos2col] = board[pos1row][pos1col]
                                    board[pos1row][pos1col] = Empty
                                    p2moved = 1
                                    continue
                                else:
                                    print("Invalid move")
