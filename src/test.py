from move import *
from display import *

board = [
                [BRook, BKnight, Empty, BKing, Empty, Empty, BKnight, Empty],
                [BPawn, WPawn, BPawn, BPawn, BPawn, BPawn, BPawn, BPawn],
                [Empty, BQueen, Empty, Empty, Empty, Empty, Empty, Empty],
                [Empty, Empty, Empty, BQueen, Empty, Empty, Empty, Empty],
                [Empty, Empty, BQueen, WKing, Empty, Empty, Empty, Empty],
                [Empty, Empty, BQueen, BQueen, BQueen, Empty, Empty, Empty],
                [WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, BQueen],
                [WRook, WKnight, WBishop, WQueen, Empty, WBishop, BQueen, Empty],
]


check_win(board,"B") #for some reason when we run this , queen validate returns false, but when we dont its true
checkboard = generate_checkboard(3,3,board)
#print(check_check(3,3,checkboard,"black"))
#print(validate_queen(4,2,3,3,checkboard))

