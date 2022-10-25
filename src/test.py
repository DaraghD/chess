from move import *
from display import *

board = [
                [BRook, BKnight, Empty, Empty, Empty, Empty, BKnight, BRook],
                [BPawn, WPawn, BPawn, BPawn, BPawn, BPawn, BPawn, BPawn, ],
                [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
                [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
                [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
                [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
                [WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, WPawn],
                [WRook, WKnight, WBishop, WQueen, Empty, WBishop, WKnight, WRook],
]
for row in board:
    for col in row:
        if col.colour == "B":
                if col.piece == "Q":
                        validate_queen(col,row,kingrow,kingqueen,board)
                print(col.colour)

