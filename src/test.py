from move import *
from display import *

board = [
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [WBishop, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, WPawn, WKing, BPawn, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
    ]

print(king_move(4, 2, 4, 1, board))
print(king_move(4, 2, 4, 3, board))
print(king_move(4, 2, 3, 3, board))
