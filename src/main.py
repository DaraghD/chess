import display
import user
import move
import bmove

from display import *
def main():

    board = display.generate()
    display.show(board)
##print(move.validateMoveBP(1,0,2,0,board))
    print(move.validateMoveWP(6,0,5,0,board))
    print(move.validateMoveWP(6,3,4,3,board)) 
    print(move.validateMoveWP(6,7,5,6,board))
    while True:
        p1moved = 0

        while p1moved == 0:
            pfile = int(input("Enter the file for piece to move:"))
            prank = int(input("Enter the rank for piece to move:"))
            mfile = int(input("Enter the file for square to move:"))
            mrank = int(input("Enter the rank for square to move:"))

            match board[pfile][prank].colour: #also have to match .colour- i think u can move enemy pawns with this?
                case "W":
                    match board[pfile][prank].piece:
                        case "P":
                            if move.validateMoveWP(pfile, prank, mfile, mrank, board):
                                print("done")
                                board[mfile][mrank] = board[pfile][prank] #replaces square moved to with this piece chosen
                                board[pfile][prank] = Empty
                                p1moved = 1
                                continue
                            else:
                                print("Invalid move")
        bmove.blackmove(board)
        display.clear()
        display.show(board)

main()
#player 2
# knights
#show board func
#multiplayer
