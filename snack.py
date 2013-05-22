#! /usr/bin/env python
# -*- coding: utf-8 -*-

# --- import ---

import sys
from math import cos, sin, pi
from random import choice
from time import sleep

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
    glVertex(0, 0)
    glVertex(1, 0)
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
    glVertex(0, 0)
    glVertex(0, 1)
    glVertex(1, 1)
    glColor(rgbhex('#8B0000'))
    glVertex(1, 0)
    glEnd()

    glColor(rgbhex('#800000'))

    glBegin(GL_LINE_LOOP)
    glVertex(0, 0)
    glVertex(0, 1)
    glVertex(1, 1)
    glVertex(1, 0)
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
    glVertex(0.0, 0.0)
    glVertex(0.0, 1.0)
    glColor(rgbhex('#000000'))
    glVertex(1.0, 0.0)

    glColor(rgbhex('#008000'))
    glVertex(0.5, 0.0)
    glVertex(1.0, 1.0)
    glColor(rgbhex('#000000'))
    glVertex(1.5, 0.0)

    glColor(rgbhex('#008000'))
    glVertex(1.0, 0.0)
    glVertex(2.0, 1.0)
    glColor(rgbhex('#000000'))
    glVertex(2.0, 0.0)

    glEnd()

    glPopMatrix()
    glColor(*origin_color)

def disk_vertexes(delta):

    angle = .0

    while angle < 2*pi:
        glVertex(
            cos(angle),
            sin(angle),
        );
        angle += delta

def disk(x=0, y=0, size=0, angle=0):

    glPushMatrix()

    glMatrixMode(GL_PROJECTION)
    glTranslate(x, y, 0)
    glRotate(angle, 0, 0, 1)
    glScale(size, size, 1)

    glBegin(GL_POLYGON)
    disk_vertexes(1.0/size)
    glEnd()

    glPopMatrix()

def circle(x=0, y=0, size=0, angle=0):

    glPushMatrix()

    glMatrixMode(GL_PROJECTION)
    glTranslate(x, y, 0)
    glRotate(angle, 0, 0, 1)
    glScale(size, size, 1)

    glBegin(GL_LINE_LOOP)
    disk_vertexes(1.0/size)
    glEnd()

    glPopMatrix()

def fruit(x=0, y=0, size=0, angle=0):

    origin_color = glGetFloatv(GL_CURRENT_COLOR)
    glPushMatrix()

    glMatrixMode(GL_PROJECTION)
    glTranslate(x, y, 0)
    glRotate(angle, 0, 0, 1)
    glScale(size, size, 1)

    glColor(rgbhex('#DC143C'))

    glBegin(GL_QUADS)
    glVertex(0, 0)
    glVertex(0, 1)
    glVertex(1, 1)
    glColor(rgbhex('#8B0000'))
    glVertex(1, 0)
    glEnd()

    glColor(rgbhex('#800000'))

    glBegin(GL_LINE_LOOP)
    glVertex(0, 0)
    glVertex(0, 1)
    glVertex(1, 1)
    glVertex(1, 0)
    glEnd()

    glPopMatrix()
    glColor(*origin_color)

def number(x=0, y=0, size=0, angle=0):

    origin_color = glGetFloatv(GL_CURRENT_COLOR)
    glPushMatrix()

    glMatrixMode(GL_PROJECTION)
    glTranslate(x, y, 0)
    glRotate(angle, 0, 0, 1)
    glScale(size, size, 1)

    glColor(rgbhex('#008000'))

    glBegin(GL_QUADS)
    glVertex(0, 0)
    glVertex(0, 1)
    glVertex(1, 1)
    glColor(rgbhex('#000000'))
    glVertex(1, 0)
    glEnd()

    glColor(rgbhex('#006400'))

    glBegin(GL_LINE_LOOP)
    glVertex(0, 0)
    glVertex(0, 1)
    glVertex(1, 1)
    glVertex(1, 0)
    glEnd()

    glPopMatrix()
    glColor(*origin_color)

# --- main ---

UNIT   = 15
UNIT_WIDTH = 48
UNIT_HEIGHT = 27
WIDTH  = UNIT*UNIT_WIDTH
HEIGHT = UNIT*UNIT_HEIGHT

snack_face = 'TOP'
snack_refresh = 200

snack_pos = [(10, 8), (10, 7), (10, 6)]

bricks_pos = None

spaces_pos = None
fruits_pos = set([(5, 5)])

is_game_over = False

score = 0

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

game_map = list(open('maps/game.txt'))
game_over = list(open('maps/gameover.txt'))

def render_map(map_):

    global bricks_pos
    global spaces_pos

    bricks_pos = set()
    spaces_pos = []
    
    unit_y = UNIT_HEIGHT

    for blocks in map_:

        unit_x = 0
        unit_y -= 1

        for block in blocks:

            if block == '+':
                brick(x=UNIT*unit_x, y=UNIT*unit_y, size=UNIT)
                bricks_pos.add((unit_x, unit_y))
            elif block == 'G':
                grass(x=UNIT*unit_x, y=UNIT*unit_y, size=UNIT)

            if block != '+':
                spaces_pos.append((unit_x, unit_y))

            unit_x += 1

def unit_disk(x=0, y=0, size=0, angle=0):
    # put center of this disk to the center of an unit
    disk(x+UNIT*0.5, y+UNIT*0.5, size*0.5, angle)

def unit_circle(x=0, y=0, size=0, angle=0):
    # put center of this disk to the center of an unit
    circle(x+UNIT*0.5, y+UNIT*0.5, size*0.5, angle)

def render_snack_body(x=0, y=0, size=0, angle=0):

    origin_color = glGetFloatv(GL_CURRENT_COLOR)

    glColor(rgbhex('#228B22'))
    unit_disk(x, y, size, angle)
    glColor(rgbhex('#006400'))
    unit_circle(x, y, size, angle)

    glColor(*origin_color)

def render_snack_head(x=0, y=0, size=0, angle=0, face='TOP'):

    render_snack_body(x, y, size, angle)

    origin_color = glGetFloatv(GL_CURRENT_COLOR)

    # TODO: refacor it

    glColor(rgbhex('#FFFFFF'))
    if face == 'TOP':
        unit_disk(x-size*0.3, y+size*0.25, size*0.4, angle)
        unit_disk(x+size*0.3, y+size*0.25, size*0.4, angle)
    elif face == 'BOTTOM':
        unit_disk(x-size*0.3, y-size*0.25, size*0.4, angle)
        unit_disk(x+size*0.3, y-size*0.25, size*0.4, angle)
    elif face == 'RIGHT':
        unit_disk(x+size*0.3, y-size*0.25, size*0.4, angle)
        unit_disk(x+size*0.3, y+size*0.25, size*0.4, angle)
    elif face == 'LEFT':
        unit_disk(x-size*0.3, y+size*0.25, size*0.4, angle)
        unit_disk(x-size*0.3, y-size*0.25, size*0.4, angle)

    glColor(rgbhex('#000000'))
    if face == 'TOP':
        unit_disk(x-size*0.3, y+size*0.25, size*0.2, angle)
        unit_disk(x+size*0.3, y+size*0.25, size*0.2, angle)
    elif face == 'BOTTOM':
        unit_disk(x-size*0.3, y-size*0.25, size*0.2, angle)
        unit_disk(x+size*0.3, y-size*0.25, size*0.2, angle)
    elif face == 'RIGHT':
        unit_disk(x+size*0.3, y-size*0.25, size*0.2, angle)
        unit_disk(x+size*0.3, y+size*0.25, size*0.2, angle)
    elif face == 'LEFT':
        unit_disk(x-size*0.3, y+size*0.25, size*0.2, angle)
        unit_disk(x-size*0.3, y-size*0.25, size*0.2, angle)

    glColor(*origin_color)

def render_snack():

    for unit_x, unit_y in reversed(snack_pos[1:]):
        render_snack_body(x=UNIT*unit_x, y=UNIT*unit_y, size=UNIT*1.5)

    unit_x, unit_y = snack_pos[0]
    render_snack_head(x=UNIT*unit_x, y=UNIT*unit_y, size=UNIT*1.5, face=snack_face)

def render_fruits():
    for unit_x, unit_y in fruits_pos:
        fruit(x=UNIT*unit_x, y=UNIT*unit_y, size=UNIT)

numbers_map = dict((i, list(open('numbers/%s.txt' % i))) for i in range(10))

def render_number(n):

    map_ = numbers_map[n]

    unit_y = UNIT_HEIGHT

    for blocks in map_:

        unit_x = 0
        unit_y -= 1

        for block in blocks:

            if block == '+':
                number(x=UNIT*unit_x, y=UNIT*unit_y, size=UNIT)
            elif block == 'G':
                grass(x=UNIT*unit_x, y=UNIT*unit_y, size=UNIT)

            unit_x += 1

def display():

    glClear(GL_COLOR_BUFFER_BIT)

    if not is_game_over:
        render_grid()
        render_map(game_map)
        render_fruits()
        render_snack()
        render_number(0)
    else:
        render_grid()
        render_map(game_over)
        render_number(0)

    glFlush()

def reshape(w, h):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glViewport(0, 0, w, h)
    gluOrtho2D(0.0, w, 0.0, h)

def keyboard(key, x, y):
    if key == 'q':
        sys.exit(0)

def special(key, x, y):

    global snack_face

    if key == 101:
        snack_face = 'TOP'
    elif key == 103:
        snack_face = 'BOTTOM'
    elif key == 100:
        snack_face = 'LEFT'
    elif key == 102:
        snack_face = 'RIGHT'

    move_snack()

def move_snack():

    global snack_pos
    global is_game_over
    global snack_refresh
    global score

    if is_game_over:
        return

    if bricks_pos and snack_pos and snack_pos[0] in bricks_pos:
        snack_pos = []
        is_game_over = True
        glutChangeToMenuEntry(1, 'restart', 3);

    if fruits_pos and snack_pos and snack_pos[0] in fruits_pos:
        snack_refresh -= 50
        score += 1
        fruits_pos.remove(snack_pos[0])
        fruits_pos.add(choice(spaces_pos))

    if snack_pos:

        snack_pos.pop(-1)

        new_head_pos = list(snack_pos[0])
        if snack_face == 'TOP':
            new_head_pos[1] += 1
        elif snack_face == 'BOTTOM':
            new_head_pos[1] -= 1
        elif snack_face == 'LEFT':
            new_head_pos[0] -= 1
        elif snack_face == 'RIGHT':
            new_head_pos[0] += 1
        new_head_pos = tuple(new_head_pos)

        if new_head_pos in snack_pos:
            snack_pos = []
            is_game_over = True
            glutChangeToMenuEntry(1, 'restart', 3);
        else:
            snack_pos.insert(0, new_head_pos)


    glutPostRedisplay()

def interval(value):
    glutTimerFunc(snack_refresh, interval, 0)
    move_snack()

def menu(idx):

    global snack_pos
    global is_game_over

    if idx == 2:
        sys.exit()
    elif idx == 3:
        snack_pos = [[10, 8]]
        is_game_over = False

if __name__ == '__main__':

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(100, 100)
    glutCreateWindow('Bricks')
    init()
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special)
    glutDisplayFunc(display)

    glutCreateMenu(menu);
    glutAddMenuEntry('continue', 1);
    glutAddMenuEntry('exit', 2);
    glutAttachMenu(GLUT_RIGHT_BUTTON);

    #interval(0)
    glutMainLoop()
