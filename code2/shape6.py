import pygame, math, os, time
try:
    from code.init6 import *
except:
    from init6 import *
    from tts import *
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
        self.drct = ""
        group.add(self) # adding each square to this pygame.sprite.Group to update easily


    def diagonal_movements(self):
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


    def update(self, timer):
        ''' 3 type of movements '''
        self.diagonal_movements()
        # self.ortogonal_movements()
        # self.bad_movements(go)
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
    speak("run loop","en")
    from tkinter import messagebox
    messagebox.showinfo("Not main file","Run loop7.py")
    os.system("py loop7.py")
    os.system("kill")