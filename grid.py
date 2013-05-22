#! /usr/bin/env python
# -*- coding: utf-8 -*-

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

def line(size=0, x=0, y=0, angle=0):

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

# --- end ---

WIDTH = 500
HEIGHT = 500
UNIT = 100

def init():
    glClearColor(0, 0, 0, 0)

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor(0, 1, 0)

    for x in range(0, WIDTH, UNIT):
        line(size=HEIGHT, x=x, angle=90)

    for y in range(0, HEIGHT, UNIT):
        line(size=WIDTH, y=y)

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
