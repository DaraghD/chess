import display
import user
import move
import bmove

def main():
    global board
    board = display.generate()
    display.show(board)

    while True:
        p1moved = 0

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
                        continue
                    else:
                        print("Invalid move")

        display.clear()
        display.show(board)

main()
#player 2
# knights
#show board func
#multiplayer