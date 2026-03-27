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
x1, x2, x3, x4 = 150, 190, 150, -62

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('SpiralsGenerator')
current_position = (0, 0)
direction = np.array([0, 1, 0])

def init_ortho():
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)
  
def line_to(x, y):
  global current_position
  glBegin(GL_LINE_STRIP)
  glVertex2f(current_position[0], current_position[1])
  glVertex2f(x, y)
  current_position = (x, y)
  glEnd()
  
def move_to(x, y):
  global current_position
  current_position = (x, y)
  
def reset_turtle():
  global current_position, direction
  current_position = (0, 0)
  direction = np.array([0, 1, 0])
  
