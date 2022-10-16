from display import *
import display
import pprint
import user
import move
import random

def blackmove(board):
    while True:
        pfile = random.randrange(0, 7, 1)
        prank = random.randrange(0, 7, 1)
        mfile = random.randrange(0, 7, 1)
        mrank = random.randrange(0, 7, 1)
        print(pfile,prank,mfile,mrank)
        match board[pfile][prank].colour:
            case "black":
                print("found colour")
                match board[pfile][prank].piece:
                    case "P":
                        print("found colour")
                        if move.validateMoveBP(pfile,prank,mfile,mrank,board):
                            print("done")
                            board[pfile][prank].hasMoved = True
                            board[mfile][mrank] = board[pfile][prank]
                            board[pfile][prank] = Empty
                            break
                        else:
                            continue



