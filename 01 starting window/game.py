import pygame
from init import *


class Game():
    ''' create ship and start the loop '''
    def __init__(self):
        self.timer = 0

    def update(self):
        ''' Things refreshed for each frame '''
        quit() # init.py
        update_display() # init.py
        self.timer += 1
