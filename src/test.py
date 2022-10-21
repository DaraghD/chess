import move
import display


board = display.generate()
print(move.validateMoveRK(4,3,1,3,board))# works
print(move.validateMoveRK(4,3,5,3,board))# returns none?
print(move.validateMoveRK(4,3,4,0,board))# returning none
print(move.validateMoveRK(4,3,4,6,board))#works
print(move.validateMoveRK(3,7,3,0,board))
print(board[4][3])
print(move.validateMoveRK(4, 3, 5, 3, board))
