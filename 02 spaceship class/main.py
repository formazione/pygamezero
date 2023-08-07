import pygame
from ship import *




class Game():
    ''' create ship and start the loop '''
    def __init__(self):
        self.timer = 0

    def quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def update_display(self):
        pygame.display.flip()
        clock.tick(frame)
        screen.fill((0,0,0))

    def update(self):
        self.quit() # init.py
        sprites.update(self.timer)
        self.update_display() # init.py
        self.timer += 1


pygame.init()
clock = pygame.time.Clock()
frame = 60
ship_init()

if __name__ == "__main__":
    window = Game()
    while True:
        window.update()
