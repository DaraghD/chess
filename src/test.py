import move
from display import *

board = [
        [BRook, BKnight, Empty, Empty, Empty, Empty, BKnight, BRook],
        [BPawn, BPawn, Empty, Empty, Empty, Empty, Empty, Empty, ],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, WRook, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [WPawn, WPawn, Empty, Empty, Empty, Empty, Empty, Empty, ],
        [Empty, WKnight, Empty, Empty, Empty, WRook, WKnight, Empty],
    ]



print(move.validateMoveRK(3,3,0,3,board)) # moving up
print(move.validateMoveRK(3,3,5,3,board)) # down
print(move.validateMoveRK(3,3,3,0,board)) # left
print(move.validateMoveRK(3,3,3,5,board)) # right
move.validateMoveRK(3,3,3,5,board)
