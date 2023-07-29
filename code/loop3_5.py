import pygame
import sys
import math
from shape import *
# Initialize Pygame
# coordinates of the rectangle and surface of it


while True:
    timer_render = font.render(f"{math.cos(timer / 4)}", 1, (255,255,255))
    screen.fill((0,0,0))
    # use the event.key id to move
    group.update(go, timer)
    go = check_keys()
    screen.blit(timer_render, (0,0))
    pygame.display.flip()
    timer +=1
    clock.tick(60)
