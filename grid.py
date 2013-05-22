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

WIDTH = 500
HEIGHT = 500

def init():
    glClearColor(0, 0, 0, 0)

def render_line():
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(1, 0)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glPushMatrix()
    glMatrixMode(GL_PROJECTION)
    glTranslate(0, 100, 0)
    glScale(100, 1, 1)
    glColor(0, 1, 0)
    render_line()
    glPopMatrix()

    glPushMatrix()
    glMatrixMode(GL_PROJECTION)
    glTranslate(0, 200, 0)
    glScale(100, 1, 1)
    glColor(1, 0, 0)
    render_line()
    glPopMatrix()

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
