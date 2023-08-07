import pygame
import sys
import math

'''
main.py
    loop6.py
    shape6.py
    init6.py

'''

if __name__ == "__main__":
    from init6 import *
    from shape6 import *
    from fps import *
    from tts import *
else:
    from code2.init6 import *
    from code2.shape6 import *
    from code2.fps import *
    from code2.tts import *

# Initialize Pygame


def quit():
    ''' way to QUIT the window '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            speak("Thank you for playing","en")
            pygame.quit()
            sys.exit()
        # If the user presses the left arrow key, move the rectangle to the left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


def update_display():
    pygame.display.flip()
    clock.tick(60)
    screen.fill((0,0,0))
    render_fps(1)


font = pygame.font.SysFont("Arial", 20)

def run():
    ''' create ship and start the loop '''
    global timer

    spaceship_init()
    speak("Chapter I","en")

    while True:
        quit()
        group.update(timer) # updates spaceship
        update_display()
        timer += 1


if __name__ == "__main__":
    run()