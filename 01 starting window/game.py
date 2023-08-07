import pygame
from init import *


class Game():
    ''' create ship and start the loop '''
    def __init__(self):
        self.timer = 0

    def quit(self):
        ''' way to QUIT the window '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # If the user presses the left arrow key, move the rectangle to the left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def update_display(self):
        pygame.display.flip()
        clock.tick(frame)
        screen.fill((0,0,0))

    def update(self):
        ''' Things refreshed for each frame '''
        self.quit() # init.py
        self.update_display() # init.py
        self.timer += 1

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
frame = 60
group = pygame.sprite.Group()