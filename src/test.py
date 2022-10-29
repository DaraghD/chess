from move import *
from display import *

board = [
                [BRook, BKnight, Empty, BKing, Empty, Empty, BKnight, BRook],
                [BPawn, WPawn, BPawn, BPawn, BPawn, BPawn, BPawn, BPawn],
                [Empty, BQueen, Empty, Empty, Empty, Empty, Empty, Empty],
                [Empty, Empty, Empty, BQueen, Empty, Empty, Empty, Empty],
                [Empty, Empty, BQueen, WKing, BQueen, Empty, Empty, Empty],
                [Empty, Empty, Empty, BQueen, Empty, Empty, Empty, Empty],
                [WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, BQueen],
                [WRook, WKnight, WBishop, WQueen, Empty, WBishop, BQueen, Empty],
]

#bking_col = 4
#bking_row = 0
#wking_row = 4
#wking_col = 3


print(check_win_black(board))
#check_check wont work here cause we are running it only in game.py when a move is made
# which dosent happen when just validating king_move ...