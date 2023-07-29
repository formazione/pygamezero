import pygame


pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
go = 0 # this contains the id of the key pressed to move the spaceship
timer = 0
group = pygame.sprite.Group()