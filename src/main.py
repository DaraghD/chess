import display
import pprint
import user
import move

def main():
     board = display.generate()
     p1moved = 0
     print(move.validateMoveWP(6,0,5,1,board))

     while p1moved == 0:
         pfile = int(input("Enter the file for piece to move:"))
         prank = int(input("Enter the rank for piece to move:"))

         mfile = int(input("Enter the file for square to move:"))
         mrank = int(input("Enter the rank for square to move:"))


         match board[pfile][prank]:
             case "WP":
                 if move.validateMoveWP(pfile, prank, mfile, mrank, board):
                     print("done")
                     board[mfile][mrank] = board[pfile][prank]
                     board[pfile][prank] = 0
                     p1moved = 1
                 else:
                     print("Invalid move")

     pp = pprint.PrettyPrinter(indent=4)
     pp.pprint(board)

main()

