README.TXT

----------------------------------------
- main.py
----------------------------------------
import pygame, sys
from game import Game

window 				istanza della classe Game
window.update() 	metodo che refresh screen -> <class Game>

----------------------------------
-game.py
----------------------------------
import pygame
from init import *

class Game
	__init__(self)
		self.timer
	
	update_display(self)
	
	update(self): refresh screen e sprites.update() <class Ship>

---------------------------------
-init.py
---------------------------------
import pygame
import sys

quit()
clock
frame


''''''''''''
ship
''''''''''''

screen
sprites   pygame.sprite.Group
Ship <class>
spaceship_init()