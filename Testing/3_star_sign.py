""" Draw Leo Star Sign with OpenGL Vertexes """
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
screen_width, screen_height = 1000, 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL Constellation')


def init_ortho():
    """ Setup 2D Graphic Generation (orthographic) Mode """
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 0, 480)


def draw_star(x, y, size):
    """ Draw a point on screen """
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()


done = False
init_ortho()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    draw_star(231, 151, 20)
    draw_star(257, 253, 20)
    draw_star(303, 181, 15)
    draw_star(443, 228, 20)
    draw_star(435, 287, 10)
    draw_star(385, 315, 20)
    draw_star(371, 343, 10)
    draw_star(397, 377, 10)
    draw_star(435, 373, 20)

    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
