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
  
def randomize():
  global x1, x2, x3, x4
  x1 = random.randint(0, 150)
  x2 = random.randint(0, 190)
  x3 = random.randint(0, 150)
  x4 = random.randint(0, 62)
  
def draw_turtle():
  for i in range(100):
    forward(x1)
    rotate(x2)
    forward(x3)
    rotate(x4)
    
def forward(draw_length):
  new_x = current_position[0] + direction[0] * draw_length
  new_y = current_position[1] + direction[1] * draw_length
  line_to(new_x, new_y)
  
def rotate(angle):
  global direction
  direction = z_rotation(direction, math.radians(angle))

init_ortho()
done = False
glLineWidth(1)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    randomize()
    pygame.time.wait(500)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glBegin(GL_POINTS)
    glVertex2f(0, 0)
    glEnd()
    reset_turtle()
    draw_turtle()
    pygame.display.flip()
pygame.quit()
