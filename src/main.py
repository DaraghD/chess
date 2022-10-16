import display
import user
import move

def main():
     board = display.generate()

     p1move = user.get_move()

     if move.validateMoveWP(p1move[0][0], p1move[0][1], p1move[1][0], p1move[1][0], board):
         board[p1move[1][0]][p1move[1][1]] = board[p1move[0][0]][p1move[0][1]]

main()

