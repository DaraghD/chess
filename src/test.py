from move import *
from display import *

board = [
                [BRook, BKnight, Empty, Empty, Empty, Empty, BKnight, BRook],
                [BPawn, WPawn, BPawn, BPawn, BPawn, BPawn, BPawn, BPawn, ],
                [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
                [BQueen, WKing, Empty, Empty, Empty, Empty, Empty, Empty],
                [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
                [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
                [WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, WPawn],
                [WRook, WKnight, WBishop, WQueen, Empty, WBishop, WKnight, WRook],
]
print(king_move(3,1,3,2,board))
