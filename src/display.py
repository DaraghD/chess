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


def generate():
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [BPawn, BPawn, BPawn, BPawn, BPawn, BPawn, BPawn, BPawn, ],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, ],
        [0, 0, 0, 0, 0, 0, 0, 0],
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
