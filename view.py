import pygame

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
    king = pygame.image.load("images/king-b.svg")
    scaled_chess_piece_image = pygame.transform.scale(king, (SQUARE_WIDTH, SQUARE_HEIGHT))
    screen.blit(scaled_chess_piece_image, (0, 0))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()