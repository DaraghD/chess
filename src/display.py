import os
import pprint

def generate():
    board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    ["BP","BP","BP","BP","BP","BP","BP","BP",],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ["WP","WP","WP","WP","WP","WP","WP","WP",],
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
