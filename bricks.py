#! /usr/bin/env python
# -*- coding: utf-8 -*-

# --- import ---

import sys
import struct

try:
  from OpenGL.GL import *
  from OpenGL.GLU import *
  from OpenGL.GLUT import *
except:
    print 'It needs PyOpenGL and OpenGL.'
    sys.exit()

# --- helpers ---

def rgbhex(rgbhex):

    rgbhex = rgbhex.strip('# ')

    if len(rgbhex) == 3:
        rgbhex = rgbhex[0]*2 + rgbhex[1]*2 + rgbhex[2]*2
    if len(rgbhex) == 6:
        return (int(rgbhex[ :2], 16)/255.0,
                int(rgbhex[2:4], 16)/255.0,
                int(rgbhex[4: ], 16)/255.0,
                1)

def line(x=0, y=0, size=0, angle=0):

    glPushMatrix()

    glMatrixMode(GL_PROJECTION)
    glTranslate(x, y, 0)
    glRotate(angle, 0, 0, 1)
    glScale(size, 1, 1)

    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(1, 0)
    glEnd()

    glPopMatrix()

def brick(x=0, y=0, size=0, angle=0):

    glPushMatrix()

    glMatrixMode(GL_PROJECTION)
    glTranslate(x, y, 0)
    glRotate(angle, 0, 0, 1)
    glScale(size, size, 1)

    origin_color = glGetFloatv(GL_CURRENT_COLOR)

    glColor(rgbhex('#B22222'))
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, 1)
    glVertex2f(1, 1)
    glVertex2f(1, 0)
    glEnd()

    glColor(rgbhex('#800000'))
    glBegin(GL_LINE_LOOP)
    glVertex2f(0, 0)
    glVertex2f(0, 1)
    glVertex2f(1, 1)
    glVertex2f(1, 0)
    glEnd()

    glColor(*origin_color)

    glPopMatrix()

# --- main ---

WIDTH = 500
HEIGHT = 500
UNIT = 100

def init():
    glClearColor(*rgbhex('#FFFFFF'))

def load_game():

    y = HEIGHT

    for blocks in open('maps/game.txt'):

        x = 0
        y -= UNIT

        for block in blocks:
            if block == '+':
                brick(x=x, y=y, size=UNIT)
            x += UNIT

def display():

    glClear(GL_COLOR_BUFFER_BIT)

    glColor(rgbhex('#00FF00'))

    for x in range(0, WIDTH, UNIT):
        line(x=x, size=HEIGHT, angle=90)

    for y in range(0, HEIGHT, UNIT):
        line(y=y, size=WIDTH)

    brick(x=UNIT, y=UNIT, size=UNIT, angle=30)

    load_game()

    glFlush()

def reshape(w, h):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glViewport(0, 0, w, h)
    gluOrtho2D(0.0, w, 0.0, h)

def keyboard(key, x, y):
    if key == 'q':
        sys.exit(0)

if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(100, 100)
    glutCreateWindow('Grid')
    init()
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutDisplayFunc(display)
    glutMainLoop()
