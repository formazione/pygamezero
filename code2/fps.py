import pygame
try:
    from code.init6 import *
except:
    from init6 import *
''' Example to show fps with pygame 28.12.2021 - python 3.10 '''


def scale(x):
	scaled = pygame.transform.scale(x, (50,50))
	return scaled


def render_fps(background=""):
	''' shows the frame rate on the screen '''

	fps_text = font.render(str(int(clock.get_fps())),1,(255,255,255)) # get the clocl'fps
	if background != "":
		bck.fill((255,0,0))
		bck.blit(fps_text,(0,0))
		screen.blit(scale(bck),(0,0))
	else:
		screen.blit(scale(fps_text),(0,0))


def mainloop():
	''' Infinite event loop where thing happens every frame '''

	while True:
		# screen.fill(0)
		render_fps(1)# call the function to blit fps
		for event in pygame.event.get(): # close window
			if event.type == pygame.QUIT:
				pygame.quit()
		pygame.display.update() # update the display
		clock.tick(60) # max frame rate to save memory


# FONT INIT
size = 20
font = pygame.font.SysFont("Arial", size) # a font for the fps
bck = pygame.Surface((size,size))
bck.fill((255,0,0))

if __name__ == "__main__":
	# INIT
	pygame.init()
	screen = pygame.display.set_mode((600, 400)) # the screen surface
	clock = pygame.time.Clock()
	mainloop()