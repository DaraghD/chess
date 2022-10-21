import display
import user
import move
import bmove

from display import *


def main():
    board = display.generate()
    display.show(board)
    print("")
    display.show_emoji(board)

    while True:
        p1moved = 0

        while p1moved == 0:
            pfile = int(input("Enter the rank for piece to move:"))
            prank = int(input("Enter the file for piece to move:"))
            mfile = int(input("Enter the rank for square to move:"))
            mrank = int(input("Enter the file for square to move:"))

            match board[pfile][prank].colour:
                case "W":
                    match board[pfile][prank].piece:
                        case "P":
                            if move.validateMoveWP(pfile, prank, mfile, mrank, board):
                                print("done")
                                board[mfile][mrank] = board[pfile][prank]  # replaces square moved to with this piece chosen
                                board[pfile][prank] = Empty
                                p1moved = 1
                                continue
                            else:
                                print("invalid")
                        case "K":
                            if move.validateMoveKnight(pfile, prank, mfile, mrank, board):
                                print("done")
                                board[mfile][mrank] = board[pfile][prank]  
                                board[pfile][prank] = Empty
                                p1moved = 1
                                continue
                        case "R":
                            if move.validateMoveRK(pfile, prank, mfile, mrank, board):
                                print("done")
                                board[mfile][mrank] = board[pfile][prank]
                                board[pfile][prank] = Empty
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
