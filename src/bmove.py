import display
import pprint
import user
import move
import random
import pprint
from main import *
#circuclar import ^^ @?? /
def blackmove():
    pfile = random.randrange(0, 7, 1)
    prank = random.randrange(0, 7, 1)
    mfile = random.randrange(0, 7, 1)
    mrank = random.randrange(0, 7, 1)
    match main.board[pfile][prank]:
        case "BP":
            if move.validateMoveBP(pfile, prank, mfile, mrank, main.board):
                print("done")
                main.board[mfile][mrank] = main.board[pfile][prank]
                main.board[pfile][prank] = 0
                p2moved = 1
                pp = pprint.PrettyPrinter(indent=4)
                pp.pprint(main.board)
                p1moved = 0
            while not move.validateMoveBP(pfile, prank, mfile, mrank, main.board):
                blackmove()
