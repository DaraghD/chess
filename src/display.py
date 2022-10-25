import os
import pprint
from dataclasses import dataclass


@dataclass
class Piece:
    colour: str
    piece: str
    hasMoved: bool
    EnPassant: bool

BPawn = Piece("B", "P", False, False)
WPawn = Piece("W", "P", False, False)
Empty = Piece("empty", "empty", False, False)
WKnight = Piece("W", "N", False, False)
BKnight = Piece("B", "K", False, False)
WRook = Piece("W", "R", False, False)
BRook = Piece("B", "R", False, False)
WBishop = Piece("W", "B", False, False)
BBishop = Piece("B", "B", False, False)
WQueen = Piece("W","Q",False, False)
WKing = Piece("W","K",False, False)


def generate():
    board = [
        [BRook, BKnight, Empty, Empty, Empty, Empty, BKnight, BRook],
        [BPawn, WPawn, BPawn, BPawn, BPawn, BPawn, BPawn, BPawn, ],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
        [WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, WPawn, WPawn],
        [WRook, WKnight, WBishop, WQueen, Empty, WBishop, WKnight, WRook],
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

        if x == 7:
            i += 1
            print("|")
            x = 0
        else:
            c += 1
            x += 1
        if i > 7:
            break


def new_board(board):
    i = 0
    x = 0
    c = 0

    new_board = [
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
    ]

    while True:
        if board[i][x].piece == "empty":
            new_board[i][x] = "  "
        else:
            print(f"{board[i][x].colour}{board[i][x].piece}", end="")
            new_board[i][x] = board[i][x].colour + board[i][x].piece
            print(new_board[i][x])

        if x >= 7:
            i += 1
            x = 0
        if i > 7:
            break

        c += 1
        x += 1

    return new_board


def show_emoji(board):
    emoji_dict = {"WP": "♙", "BP": "♟", "WN": "♘", "BK": "♞", "WR": "♖", "BR": "♜", "WQ":"♕","WB":"♗"}
    i = 0
    x = 0
    c = 0
    n = 8

    print("A B C")

    while True:

        print("|", end="")

        if board[i][x].piece == "empty":
            print("  ", end="")
        else:
            p = board[i][x].colour + board[i][x].piece
            print(f" {emoji_dict[p]}", end="")

        if x == 7:
            i += 1
            print(f"| {n}")
            x = 0
            n -= 1
        else:
            c += 1
            x += 1
        if i > 7:
            break
