"""
Function takes a dictionary argument and returns True or False depending on if the board is valid.
There need to be one black and white king
Each player has at most 16 pieces
At most 8 pawns
Each space must be valid from 1a to 8h
Pieces begin with either w or b
and
pawn, knight, bishop, rook, queen or king
"""


chessBoard1 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
chessBoard2 = {'1g': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
chessBoard3 = {'1c': 'bking', '8c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}


validFields = ["1a","1b","1c","1d","1e","1f","1g","1h"
"2a","2b","2c","2d","2e","2f","2g","2h"
"3a","3b","3c","3d","3e","3f","3g","3h",
"4a","4b","4c","4d","4e","4f","4g","4h",
"5a","5b","5c","5d","5e","5f","5g","5h",
"6a","6b","6c","6d","6e","6f","6g","6h",
"7a","7b","7c","7d","7e","7f","7g","7h",
"8a","8b","8c","8d","8e","8f","8g","8h"]

validPieces = ["bpawn","wpawn","bknight","wknight","bbishop",
"wbishop","brook","wrook","bqueen",
"wqueen","wking","bking"]

# A list to check if to pieces have the same field which cant be the case
duplicateFieldChecker = []
# piecesCounter is responsible to count how many pieces are on the board
piecesCounter = {"bking":0,"wking":0,"bpawn":0,"wpawn":0,"bknight":0,"wknight":0,"bbishop":0,
"wbishop":0,"brook":0,"wrook":0,"bqueen":0,
"wqueen":0}

invalidBoardCheck = 0
# we have to seperate the dictionary into keys and values
def isValidChessBoard(board):
    fields = list(board.keys())
    pieces = list(board.values())
    for item in fields:
        if item in validFields:
            # Now I want to check if the field has a duplicate
            # If the item IS in the checker list then put out an error
            if item in duplicateFieldChecker:
                return print("2 Pieces cant be on the same field at the same time")
            else:
                duplicateFieldChecker.append(item)
                continue
        else:
            return print("Invalid Field " + item)
    # The for loop that goes through each value in the dictionary
    for item in pieces:
        if item in validPieces:
            pieceChecker(item)

        else:
            return print("Invalid Piece " + item)

    duplicateFieldChecker.clear()
    # makes ever value in the piecesCounter Dictionary go back to 0 so you can check multiple boards
    for item in piecesCounter:
        piecesCounter[item] = 0

    return print("This is a valid board!")

"""
pieceChecker takes a piece and then
bumps the counter up by 1
the counter indicates if a limit has been reached
Example: there can only be one "wking"
so if a board has 2 "wking" then the board is invalid
"""
def pieceChecker(piece):
    # bumps up the counter by one on the specifc piece

    # a check if the max number of pieces has been reached
    if (piece == "bking" or piece == "wking") and piecesCounter[piece] + 1 < 2:
        piecesCounter[piece] += 1
        print(piecesCounter[piece])

    else:
        print("There can only be one king for each side. Invalid Board")
        quit()


    if (piece == "bpawn" or "wpawn") and piecesCounter[piece] + 1 < 8:
        piecesCounter[piece] += 1

    else:
        print("Too many pawns. Invalid Board")
        quit()


    if (piece == "bknight" or piece == "wknight") and piecesCounter[piece] + 1 < 2:
        piecesCounter[piece] += 1


    else:
        print("There can only be 2 knights for each side. Invalid Board")
        quit()


    if (piece == "bbishop" or "wbishop") and piecesCounter[piece] + 1 < 2:
        piecesCounter[piece] += 1
    else:
        print("There can only be 2 bishops for each side. Invalid Board")
        quit()


    if (piece == "brook" or "wrook") and piecesCounter[piece] + 1 < 2:
        piecesCounter[piece] += 1

    else:
        print("There can only be 2 rooks for each side. Invalid Board")
        quit()


    if (piece == "bqueen" or "wqueen") and piecesCounter[piece] + 1 < 1:
        piecesCounter[piece] += 1

    else:
        print("There can only be one Queen for each side. Invalid Board")
        quit()



isValidChessBoard(chessBoard1)
isValidChessBoard(chessBoard2)
isValidChessBoard(chessBoard3)






