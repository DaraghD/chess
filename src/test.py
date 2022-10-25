from move import *
from display import *

board = [
                [BRook, BKnight, Empty, Empty, Empty, Empty, BKnight, BRook],
                [BPawn, WPawn, BPawn, BPawn, BPawn, BPawn, BPawn, BPawn, ],
                [Empty, BQueen, Empty, Empty, Empty, Empty, Empty, Empty],
                [Empty, WKing, Empty, Empty, Empty, Empty, Empty, Empty],
                [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
                [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
                [WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, WPawn],
                [WRook, WKnight, WBishop, WQueen, Empty, WBishop, WKnight, WRook],
]

print(king_move(3,1,4,2,board)) #3,2 given to the queen
print(king_move(3,1,4,2,board)) #3,2 given to the queen
print(king_move(3,1,4,1,board)) #3,2 given to the queen

#ignore king in queen
