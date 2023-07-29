import pygame
import sys
import math
# Initialize Pygame
pygame.init()

# Create a window with a clock for frame rate speed
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
# coordinates of the rectangle and surface of it
class Shape(pygame.sprite.Sprite):
    def __init__(self, x, y, color, pos=""):
        super().__init__()
        self.rectx, self.recty = x, y
        self.surface = pygame.Surface((10,10))
        self.surface.fill(color) # color red for it
        self.speed = 4
        self.pos = pos
        group.add(self)
    def update(self, go):
        match go:
            case 1073741903: self.rectx += self.speed
            case 1073741904: self.rectx -= self.speed
            case 1073741905: self.recty += self.speed
            case 1073741906: self.recty -= self.speed
        self.pulsar()

    def pulsar(self):
        if self.pos == "right":
            self.rectx += math.cos(timer / 4)
        if self.pos == "left":
            self.rectx -= math.cos(timer / 4)
        if self.pos == "top":
            self.recty -= math.cos(timer / 4)
        if self.pos == "bottom":
            self.recty += math.cos(timer / 4)
        screen.blit(self.surface, (self.rectx, self.recty))


# direction controller
group = pygame.sprite.Group()
rec1 = Shape(100,100,(255,0,0), "center")
rec2 = Shape(100,86,(255,255,0), "top")
rec3 = Shape(86,100,(255,255,255), "left")
rec4 = Shape(114,100,(0,255,0), "right")
rec5 = Shape(100,114,(0,255,255), "bottom")
go = 0
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

timer = 0
font = pygame.font.SysFont("Arial", 20)
while True:
    timer_render = font.render(f"{math.cos(timer / 4)}", 1, (255,255,255))
    screen.fill((0,0,0))
    # use the event.key id to move
    group.update(go)
    go = check_keys()
    screen.blit(timer_render, (0,0))
    pygame.display.flip()
    timer +=1
    clock.tick(60)
