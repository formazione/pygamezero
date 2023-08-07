import pygame

def move(self):
    keys = pygame.key.get_pressed() #check the key pressed
    if keys[pygame.K_LEFT]:
        self.rectx -= self.speed
    if keys[pygame.K_RIGHT]:
        self.rectx += self.speed
    if keys[pygame.K_UP]:
        self.recty -= self.speed
    if keys[pygame.K_DOWN]:
        self.recty += self.speed
