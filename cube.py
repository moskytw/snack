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

angle = 0

def init():
    glClearColor(0, 0, 0, 0)
    glEnable(GL_DEPTH_TEST)

def render_cube():

    global angle

    glLoadIdentity()
    glTranslate(0, 0, -7)
    glRotate(angle, 1, 1, 1)

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

def idle():
    global angle
    angle += 2
    glutPostRedisplay()

def reshape(w, h):

    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, 0.1, 100)
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
    glutIdleFunc(idle)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutDisplayFunc(display)
    glutMainLoop()
