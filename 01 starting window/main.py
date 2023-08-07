import pygame
import sys
from game import Game

if __name__ == "__main__":
    window = Game()
    while True:
        window.update()