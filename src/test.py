from move import *
from display import *
from game import find_kings

board = [
                [BRook, BKnight, Empty, BKing, Empty, Empty, BKnight, BRook],
                [BPawn, WPawn, BPawn, BPawn, BPawn, BPawn, BPawn, BPawn, ],
                [Empty, BQueen, Empty, Empty, Empty, Empty, Empty, Empty],
                [Empty, Empty, WKing, BQueen, Empty, Empty, Empty, Empty],
                [Empty, Empty, BQueen, Empty, BQueen, Empty, Empty, Empty],
                [Empty, Empty, Empty, BQueen, Empty, Empty, Empty, Empty],
                [WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, WPawn],
                [WRook, WKnight, WBishop, WQueen, Empty, WBishop, WKnight, WRook],
]

#bking_col = 4
#bking_row = 0
#wking_row = 4
#wking_col = 3


print(check_win_white(board))

#check_check wont work here cause we are running it only in game.py when a move is made
# which dosent happen when just validating king_move ...