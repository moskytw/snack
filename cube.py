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

def init():
    glClearColor(0, 0, 0, 0)

def render_box():
    glBegin(GL_QUADS)
    glVertex(0, 0) # bottom left
    glVertex(1, 0) # bottom right
    glVertex(1, 1) # top right
    glVertex(0, 1) # top left
    glEnd()

def display():

    glClear(GL_COLOR_BUFFER_BIT)

    glTranslate(1, 1, 0)
    glScale(1, 2, 1)
    glColor(0, 1, 0)
    render_box()

    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if(w <= h):
        gluOrtho2D(0.0, 10.0, 0.0, 10.0 * h/w)
    else:
        gluOrtho2D(0.0, 10.0 * w/h, 0.0, 10.0)
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    if key == 'q':
        sys.exit(0)

if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow('Box')
    init()
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutDisplayFunc(display)
    glutMainLoop()
