from move import *
from display import *

board = [
                [BRook, BKnight, Empty, BKing, Empty, Empty, BKnight, WKing],
                [BPawn, WPawn, BPawn, BPawn, BPawn, BPawn, BPawn, BPawn],
                [Empty, BQueen, Empty, Empty, Empty, Empty, Empty, Empty],
                [Empty, Empty, Empty, BQueen, Empty, Empty, Empty, Empty],
                [Empty, Empty, BQueen, Empty, BQueen, Empty, Empty, Empty],
                [Empty, Empty, Empty, BQueen, Empty, Empty, Empty, Empty],
                [WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, BQueen],
                [WRook, WKnight, WBishop, WQueen, Empty, WBishop, BQueen, Empty],
]


board = generate_checkboard(0,7,board)
print(validate_queen(2,1,0,7,board)) #somehow this is valid move
print(diagonal_move(2,1,0,7,board))

queen_validate1 = "This is the result of {bool}"
print(queen_validate1.format(bool = validate_queen(2,1,0,7,board)))
#check_check wont work here cause we are running it only in game.py when a move is made
# which dosent happen when just validating king_move ...