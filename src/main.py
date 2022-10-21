import user
import move
import bmove
import display
from display import *


def main():
    board = display.generate()
    display.show(board)
    print("")
    display.show_emoji(board)

    while True:
        p1moved = 0

        while p1moved == 0:
            pos1row = int(input("Enter the rank for piece to move:"))
            pos1col = int(input("Enter the file for piece to move:"))
            pos2row = int(input("Enter the rank for square to move:"))
            pos2col = int(input("Enter the file for square to move:"))

            match board[pos1row][pos1col].colour:
                case "W":
                    match board[pos1row][pos1col].piece:
                        case "P":
                            if move.validateMoveWP(pos1row, pos1col, pos2row, pos2col, board):
                                print("done")
                                board[pos2row][pos2col] = board[pos1row][
                                    pos1col]  # replaces square moved to with this piece chosen
                                board[pos1row][pos1col] = Empty
                                p1moved = 1
                                if pos2row == 0:
                                    board[pos2row][pos2col] = WQueen
                                continue
                            else:
                                print("invalid")
                        case "K":
                            if move.validateMoveKnight(pos1row, pos1col, pos2row, pos2col, board):
                                print("done")
                                board[pos2row][pos2col] = board[pos1row][pos1col]
                                board[pos1row][pos1col] = Empty
                                p1moved = 1
                                continue
                        case "R":
                            if move.validateMoveRK(pos1row, pos1col, pos2row, pos2col, board):
                                print("done")
                                board[pos2row][pos2col] = board[pos1row][pos1col]
                                board[pos1row][pos1col] = Empty
                                p1moved = 1
                                continue
                            else:
                                print("Invalid move")
        # bmove.blackmove(board)
        display.clear()
        # new_board = display.new_board(board)
        # display.show_debug(new_board)
        # display.show(board)
        display.show_emoji(board)


main()
# player 2
# knights
# show board func
# multiplayer
