""" Setting up screen/window in PyGame & OpenGL """
import pygame
from pygame.locals import *

pygame.init()
screen_width, screen_height = 1000, 800

# setup screen in pygame, use OpenGL double-buffering
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
