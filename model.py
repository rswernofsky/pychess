import pygame

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

board = []
locations = {}
starting_position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

class Piece:
    white : bool
    piece_type : str

    def __init__(self, white, piece_type):
        self.white = white
        self.piece_type = piece_type

for row_number, row in enumerate(starting_position.split("/")):
    curr_row = []
    for char in row:
        if char.isdigit():
            for i in range(int(char)):
                curr_row.append(None)
        else:
            color = char.isupper()
            curr_row.append(Piece(color, char.lower()))
    board.append(curr_row)



PIECE_TYPES = ['p', 'n', 'b', 'r', 'q', 'k']

def initialize_board():
    board[0] = ['rook', 'knight', 'bishop', '']




pygame.init()
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    # RENDER YOUR GAME HERE
    SQUARE_WIDTH = SCREEN_WIDTH / 8
    SQUARE_HEIGHT = SCREEN_HEIGHT / 8
    for x in range(8):    
        for y in range(8): 
            color = "grey" if (x + y) % 2 != 0 else "beige" 
            pygame.draw.rect(screen, color, pygame.Rect(x * SQUARE_WIDTH, y * SQUARE_HEIGHT, SQUARE_WIDTH, SQUARE_HEIGHT))
    # king = pygame.image.load("images/king-b.svg")
    # scaled_chess_piece_image = pygame.transform.scale(king, (SQUARE_WIDTH, SQUARE_HEIGHT))
    # screen.blit(scaled_chess_piece_image, (0, 0))

    for y, row in enumerate(board):
        for x, piece in enumerate(row):
            if not piece:
                continue
            color = "w" if piece.white else "b"
            piece_type = piece.piece_type
            image = pygame.image.load(f"images/{piece_type}-{color}.svg")
            scaled_chess_piece_image = pygame.transform.scale(image, (SQUARE_WIDTH, SQUARE_HEIGHT))
            screen.blit(scaled_chess_piece_image, (x * SQUARE_WIDTH, y * SQUARE_HEIGHT))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()