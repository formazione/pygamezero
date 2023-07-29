import pygame
import sys
import math

'''
main.py
    loop6.py
    shape6.py
    init6.py

'''

if __name__ == "__main__":
    from init6 import *
    from shape6 import *
else:
    from code.init6 import *
    from code.shape6 import *

# Initialize Pygame


def check_keys():
    global go
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # If the user presses the left arrow key, move the rectangle to the left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            go = event.key
        else:
            go = 0
    return go


def update_display():
    pygame.display.flip()
    clock.tick(60)
    screen.fill((0,0,0))


font = pygame.font.SysFont("Arial", 20)

def run():
    ''' create ship and start the loop '''
    global timer
    spaceship_init()

    while True:
        timer_render = font.render(f"{math.cos(timer / 4)}", 1, (255,255,255))
        go = check_keys() # what key is pressed? -> go
        group.update(go, timer) # update pos based on go
        screen.blit(timer_render, (0,0))
        update_display()
        timer +=1     # this is to make fancy movements based on cos or sin... math babe!


if __name__ == "__main__":
    run()