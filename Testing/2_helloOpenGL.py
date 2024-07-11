import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
screen_width, screen_height = 1000, 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')


def init_ortho():
    """ Setup 2D Graphic Generation (orthographic) Mode """
    glMatrixMode(GL_PROJECTION)  # for camera/world projection
    glLoadIdentity()  # clear GL_PROJECTION & provide new palette
    gluOrtho2D(0, 640, 0, 480)  # set window coords (x1, x2, y1, y2)


done = False
init_ortho()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()  # clear GL_MODELVIEW
    glPointSize(5)  # set size of points on screen
    glBegin(GL_POINTS)  # every glBegin needs a matching glEnd
    glVertex2i(320, 100)  # put a point at x,y coord
    glVertex2i(260, 135)
    glVertex2i(235, 165)
    glVertex2i(300, 160)
    glVertex2i(380, 165)
    glEnd()

    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
