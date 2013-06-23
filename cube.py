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
    glEnable(GL_DEPTH_TEST)

def render_cube():

    glLoadIdentity()
    glTranslatef(0, 0, -7)
    glRotatef(30, 1, 1, 1)

    glBegin(GL_QUADS)

    glColor3f(0, 1, 0)
    glVertex3f( 1,  1, -1)
    glVertex3f(-1,  1, -1)
    glVertex3f(-1,  1,  1)
    glVertex3f( 1,  1,  1)

    glColor3f(1, 0.5,  0)
    glVertex3f( 1, -1,  1)
    glVertex3f(-1, -1,  1)
    glVertex3f(-1, -1, -1)
    glVertex3f( 1, -1, -1)

    glColor3f(1, 0, 0)
    glVertex3f( 1,  1,  1)
    glVertex3f(-1,  1,  1)
    glVertex3f(-1, -1,  1)
    glVertex3f( 1, -1,  1)

    glColor3f(1, 1, 0)
    glVertex3f( 1, -1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1,  1, -1)
    glVertex3f( 1,  1, -1)

    glColor3f(0, 0, 1)
    glVertex3f(-1,  1,  1)
    glVertex3f(-1,  1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1,  1)

    glColor3f(1, 0, 1)
    glVertex3f( 1,  1, -1)
    glVertex3f( 1,  1,  1)
    glVertex3f( 1, -1,  1)
    glVertex3f( 1, -1, -1)

    glEnd()

def display():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    render_cube()

    glutSwapBuffers()

def reshape(w, h):

    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, w/h, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    if key == 'q':
        sys.exit(0)

if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow('Cube')
    init()
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutDisplayFunc(display)
    glutMainLoop()
