import pygame, math, os, time

sprites = pygame.sprite.Group()
screen = pygame.display.set_mode((600, 400))
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, color, pos=""):
        super().__init__()
        self.rectx, self.recty = x, y
        self.w = 10
        self.h = 10
        self.surface = pygame.Surface((self.w,self.h))
        self.surface.fill(color) # color red for it
        self.speed = 4
        self.pos = pos
        self.drct = ""
        sprites.add(self) # adding each square to this pygame.sprite.Group to update easily


    def update(self, timer):
        keys = pygame.key.get_pressed() #check the key pressed
        if keys[pygame.K_LEFT]:
            self.rectx -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rectx += self.speed
        if keys[pygame.K_UP]:
            self.recty -= self.speed
        if keys[pygame.K_DOWN]:
            self.recty += self.speed
        if self.drct != "":
            self.drct == ""
        self.pulsar(timer) # changing pos and color each frame


    def colorvariation(self): # <- pulsar
        ''' fills the surfaces with variable colors '''
        self.surface.fill((
            self.colorvar,
            self.colorvar2,
            self.colorvar3))

    def pulsar(self,timer):
        ''' making fancy movements and colors '''
        variation = math.cos(timer/8)
        self.colorvar = 255-abs(int(math.sin(timer/16)*100))
        self.colorvar2 = 255-abs(int(math.cos(timer/32)*100))
        self.colorvar3 = 255-abs(int(math.sin(timer/32)*100))
        # print(int(math.cos(timer/2)*100))
        match self.pos:
            case "right":
                self.rectx += variation
            case "left":
                self.rectx -= variation
            case "top":
                self.recty -= variation
            case "bottom":
                self.recty += variation
            case "center":
                pass
        # self.colorvariation()
        screen.blit(self.surface, (self.rectx, self.recty))



def ship_init():
    Ship(100,100,(255,0,0), "center")
    Ship(100,86,(255,255,0), "top")
    Ship(86,100,(255,255,255), "left")
    Ship(114,100,(0,255,0), "right")
    Ship(100,114,(0,255,255), "bottom")


