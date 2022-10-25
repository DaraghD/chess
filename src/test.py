from move import *
from display import *

board = [
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [WBishop, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
    ]

#checking queen directions, all true
print(validate_queen(4,3,0,1,board))
print(validate_queen(4,3,0,3,board))
print(validate_queen(4,3,7,3,board))
print(validate_queen(4,3,4,7,board))
print(validate_bishop(2,5,0,7,board))
print(diagonal_move(7,2,2,7,board))
print(validate_bishop(7,2,2,7,board))
