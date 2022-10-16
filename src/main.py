import display
import user
import move

def main():
     board = display.generate()
     print(move.validateMoveWP(6,0,5,1,board))

     pfile = int(input("Enter the file for piece to move:"))
     prank = int(input("Enter the rank for piece to move:"))

     mfile = int(input("Enter the file for square to move:"))
     mrank = int(input("Enter the rank for square to move:"))


     if move.validateMoveWP(pfile, prank, mfile, mrank, board):
         print("done")
         board[pfile][prank] = board[mfile][mrank]

main()

