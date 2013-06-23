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

def cube():

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

    glPushMatrix()

    glScale(200, 200, 200)

    cube()

    glPopMatrix()

    glutSwapBuffers()

eye_x = 0
eye_y = 0
eye_z = -500

def reshape(w, h):

    global eye_x, eye_y

    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, 1, 1, 1000)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(eye_x, eye_y, eye_z, 0, 0, 0, 0, 1, 0)

def keyboard(key, x, y):
    if key == 'q':
        sys.exit(0)

def special(key, x, y):

    global eye_x, eye_y, eye_z

    if key == 101:
        eye_y += 5
    elif key == 103:
        eye_y -= 5
    elif key == 100:
        eye_x += 5
    elif key == 102:
        eye_x -= 5
    elif key == 104:
        eye_z += 5
    elif key == 105:
        eye_z -= 5

    print eye_x, eye_y, eye_z

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(eye_x, eye_y, eye_z, 0, 0, 0, 0, 1, 0)
    glutPostRedisplay()

if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow('Cube')
    init()
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special)
    glutDisplayFunc(display)
    glutMainLoop()
