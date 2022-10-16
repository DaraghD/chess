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
        match board[pfile][prank]:
            case "BP":
                if move.validateMoveBP(pfile,prank,mfile,mrank,board):
                    print("done")
                    board[mfile][mrank] = board[pfile][prank]
                    board[pfile][prank] = 0
                    break
                else:
                    continue



