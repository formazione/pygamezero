import pygame
import sys

# Initialize Pygame
pygame.init()

# Create a window with a clock for frame rate speed
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
# coordinates of the rectangle and surface of it
rectx, recty = 100, 100
rectangle = pygame.Surface((10,10))
rectangle.fill((255,0,0)) # color red for it
# direction controller
go = 0
while True:
    screen.fill((0,0,0))
    # use the event.key id to move
    match go:
        case 1073741903: rectx += 1 
        case 1073741904: rectx -= 1 
        case 1073741905: recty += 1 
        case 1073741906: recty -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # If the user presses the left arrow key, move the rectangle to the left
        if event.type == pygame.KEYDOWN:
            go = event.key

    screen.blit(rectangle, (rectx, recty))
    pygame.display.flip()
    clock.tick(60)
