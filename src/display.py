import os
import pprint
from dataclasses import dataclass


@dataclass
class Piece:
    colour: str
    piece: str
    hasMoved: bool
## PIECE, 0 = PAWN,
## 0 = Black, 1 = white

BPawn = Piece("B", "P", False)
WPawn = Piece("W", "P", False)
Empty = Piece("empty", "empty",False)


def generate():
    board = [
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [BPawn, BPawn, BPawn, BPawn, BPawn, BPawn, BPawn, BPawn, ],
        [Empty, WPawn, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, BPawn, Empty, Empty, Empty, Empty, Empty, Empty],
        [WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, ],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
    ]
    return board


def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def show_debug(board):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(board)

def show(board):
    i = 0
    x = 0
    c = 0

    while True:

        print("|", end="")


        if board[i][x].piece == "empty":
            print("  ", end="")
        else:
            print(f"{board[i][x].colour}{board[i][x].piece}", end="")

        if x >= 7:
            i += 1
            print("|")
            x = 0
        if i > 7:
            break
        
        c += 1
        x += 1
