#!/usr/bin/python3
# ATBS Chapter 5 Practice Project

# Chess dictionary validator

# Exercise Description:
# Write a function named isValidChessBoard() that takes a dictionary argument and returns
# True or False depending on if the board is valid.
# A Valid board will have exactly one black king and exactly one white king.
# Each player can only have at most 16 pieces, at most 8 pawns, and all pieces
# must be on a valid space from '1a' to '8h'; that is, a piece can't be on space '9z'.
# The piece names begin with either a 'w' or 'b' to represent white or black, followed
# by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.  This function should detect
# when a bug has resulted in an improper chess board.

bd = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

# Test boards - these are for testing purposes while coding
validbd = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
invalidbdPosition = {'1h': 'bking', '9c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
invalidbdPieces = {'1h': 'bking', '6c': 'wking', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

validColors = ('b', 'w')
validPieces = ('bpawn', 'bpawn', 'bpawn', 'bpawn', 'bpawn', 'bpawn', 'bpawn', 'bpawn',\
        'wpawn', 'wpawn', 'wpawn', 'wpawn', 'wpawn', 'wpawn', 'wpawn', 'wpawn',\
        'wknight', 'wknight', 'wbishop', 'wbishop', 'wrook', 'wrook', 'wqueen', 'wking',\
        'bknight', 'bknight', 'bbishop', 'bbishop', 'brook', 'brook', 'bqueen', 'bking')
validBoard = ("1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", \
    "1b", "2b", "3b", "4b", "5b", "6b", "7b", "8b", \
    "1c", "2c", "3c", "4c", "5c", "6c", "7c", "8c", \
    "1d", "2d", "3d", "4d", "5d", "6d", "7d", "8d", \
    "1e", "2e", "3e", "4e", "5e", "6e", "7e", "8e", \
    "1f", "2f", "3f", "4f", "5f", "6f", "7f", "8f", \
    "1g", "2g", "3g", "4g", "5g", "6g", "7g", "8g", \
    "1h", "2h", "3h", "4h", "5h", "6h", "7h", "8h")

def isPositionValid(pos): # Return false if position isn't valid, True if it is.
    return pos in validBoard

def isPieceValid(move):
    return move in validPieces

def isValidChessBoard(bd):
    pieces = list(bd.values())
    positions = list(bd.keys())

    for pos in positions: # Ensure all positions passed are valid
        if not isPositionValid(pos):
            return False
            break
    for piece in pieces: # Ensure type and number of pieces passed are valid
        if not isPieceValid(piece):
            return False
            break
        if pieces.count(piece) > validPieces.count(piece):
            return False
            break
        return True

print("Testing valid board. Result = %s"%(isValidChessBoard(validbd)))
print("Testing invalid board (Positions). Result = %s"%(isValidChessBoard(invalidbdPosition)))
print("Testing invalid board (Pieces). Result = %s"%(isValidChessBoard(invalidbdPieces)))