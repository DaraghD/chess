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

BPawn = Piece("black", "P", False)
WPawn = Piece("white", "P", False)
Empty = Piece("empty", "empty",False)


def generate():
    board = [
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [BPawn, BPawn, BPawn, BPawn, BPawn, BPawn, BPawn, BPawn, ],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, ],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
    ]
    return board


def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def show(board):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(board)
