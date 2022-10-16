def get_move():
    pfile = input("Enter the file for piece to move:")
    prank = input("Enter the rank for piece to move:")

    mfile = input("Enter the file for square to move:")
    mrank = input("Enter the rank for square to move:")

    piece = (pfile, prank)

    square = (mfile, mrank)

    return (piece, square)

