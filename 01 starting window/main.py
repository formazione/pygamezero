import pygame
import sys
from game import Game

'''
main.py run
game.py self.update() self.timer
init.py quit() update_display() screen, clock, frame, group

'''
if __name__ == "__main__":
    run = Game()
    while True:
        run.update()