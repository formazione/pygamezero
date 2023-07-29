import pygame, math, os, time
try:
    from code.init6 import *
except:
    from init6 import *
class Shape(pygame.sprite.Sprite):
    def __init__(self, x, y, color, pos=""):
        super().__init__()
        self.rectx, self.recty = x, y
        self.w = 10
        self.h = 10
        self.surface = pygame.Surface((self.w,self.h))
        self.surface.fill(color) # color red for it
        self.speed = 4
        self.pos = pos
        group.add(self) # adding each square to this pygame.sprite.Group to update easily
    def update(self, go, timer):
        ''' moving squares by the id of the key pressed '''
        match go:
            case 1073741903: self.rectx += self.speed
            case 1073741904: self.rectx -= self.speed
            case 1073741905: self.recty += self.speed
            case 1073741906: self.recty -= self.speed
        self.pulsar(timer) # changing pos and color each frame

    def colorvariation(self): # <- pulsar
        ''' fills the surfaces with variable colors '''
        self.surface.fill((
            self.colorvar,
            self.colorvar2,
            0))

    def pulsar(self,timer):
        ''' making fancy movements and colors '''
        variation = math.cos(timer/8)
        self.colorvar = 255-abs(int(math.sin(timer/16)*100))
        self.colorvar2 = 255-abs(int(math.cos(timer/32)*100))
        # print(int(math.cos(timer/2)*100))
        match self.pos:
            case "right":
                self.rectx += variation
                self.colorvariation()
            case "left":
                self.rectx -= variation
                self.colorvariation()
            case "top":
                self.recty -= variation
                self.colorvariation()
            case "bottom":
                self.recty += variation
                self.colorvariation()
            case "center":
                self.colorvariation()
        screen.blit(self.surface, (self.rectx, self.recty))



def spaceship_init():
    Shape(100,100,(255,0,0), "center")
    Shape(100,86,(255,255,0), "top")
    Shape(86,100,(255,255,255), "left")
    Shape(114,100,(0,255,0), "right")
    Shape(100,114,(0,255,255), "bottom")


if __name__ == "__main__":
    print("Cannot run from here: THIS IS JUST SPRITES MODULE START FROM loop4.py")
    time.sleep(1)
    os.system("kill")