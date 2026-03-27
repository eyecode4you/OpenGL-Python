import pygame
import random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils2 Import *

pygame.init()
screen_width = 800
screen_height = 800
ortho_left = -400
ortho_right = 400
ortho_top = -400
ortho_bottom = 400

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('SpiralsGenerator')
current_position = (0, 0)
direction = np.array([0, 1, 0])
