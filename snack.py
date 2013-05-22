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

    origin_color = glGetFloatv(GL_CURRENT_COLOR)
    glPushMatrix()

    glMatrixMode(GL_PROJECTION)
    glTranslate(x, y, 0)
    glRotate(angle, 0, 0, 1)
    glScale(size, size, 1)

    glColor(rgbhex('#B22222'))

    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, 1)
    glVertex2f(1, 1)
    glColor(rgbhex('#8B0000'))
    glVertex2f(1, 0)
    glEnd()

    glColor(rgbhex('#800000'))

    glBegin(GL_LINE_LOOP)
    glVertex2f(0, 0)
    glVertex2f(0, 1)
    glVertex2f(1, 1)
    glVertex2f(1, 0)
    glEnd()

    glPopMatrix()
    glColor(*origin_color)

def grass(x=0, y=0, size=0, angle=0):

    origin_color = glGetFloatv(GL_CURRENT_COLOR)
    glPushMatrix()

    glMatrixMode(GL_PROJECTION)
    glTranslate(x, y, 0)
    glRotate(angle, 0, 0, 1)
    glScale(size, size, 1)

    glBegin(GL_TRIANGLES)

    glColor(rgbhex('#008000'))
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 1.0)
    glColor(rgbhex('#000000'))
    glVertex2f(1.0, 0.0)

    glColor(rgbhex('#008000'))
    glVertex2f(0.5, 0.0)
    glVertex2f(1.0, 1.0)
    glColor(rgbhex('#000000'))
    glVertex2f(1.5, 0.0)

    glColor(rgbhex('#008000'))
    glVertex2f(1.0, 0.0)
    glVertex2f(2.0, 1.0)
    glColor(rgbhex('#000000'))
    glVertex2f(2.0, 0.0)

    glEnd()

    glPopMatrix()
    glColor(*origin_color)


# --- main ---

UNIT   = 15
WIDTH  = UNIT*48
HEIGHT = UNIT*27

def init():
    glClearColor(*rgbhex('#FFFFFF'))
    glShadeModel(GL_SMOOTH)

def render_grid():

    origin_color = glGetFloatv(GL_CURRENT_COLOR)

    glColor(rgbhex('#00FF00'))

    for x in range(0, WIDTH, UNIT):
        line(x=x, size=HEIGHT, angle=90)

    for y in range(0, HEIGHT, UNIT):
        line(y=y, size=WIDTH)

    glColor(*origin_color)

def load_game():

    y = HEIGHT

    for blocks in open('maps/game.txt'):

        x = 0
        y -= UNIT

        for block in blocks:
            if block == '+':
                brick(x=x, y=y, size=UNIT)
            elif block == 'G':
                grass(x=x, y=y, size=UNIT)
            x += UNIT

def display():

    glClear(GL_COLOR_BUFFER_BIT)

    render_grid()
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
    glutCreateWindow('Bricks')
    init()
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutDisplayFunc(display)
    glutMainLoop()
