import pygame
import sys

'''
quit()
update_display()
screen,
clock,
frame,
group

'''


# ==========================================QUIT WINDOW
def quit():
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

def update_display():
    pygame.display.flip()
    clock.tick(frame)
    screen.fill((0,0,0))

#========================================INITIALIZE PYGAME
pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
frame = 60
group = pygame.sprite.Group()
