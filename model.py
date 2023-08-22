# board
# 2d array (8x8)
# hashmap of piece to location
# (1, 2)

# - move (piece, location)

# piece
# - white or black
# - enum type

# - getMoves
# - 

from enum import Enum

board = [[]]
locations = {}
starting_position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

for char in starting_position:
    if char 
class Piece:
    white : bool
    piece_type : str

PIECE_TYPES = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

def initialize_board():
    board[0] = ['rook', 'knight', 'bishop', '']


locations['']