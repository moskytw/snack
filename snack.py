#! /usr/bin/env python
# -*- coding: utf-8 -*-

# --- import ---

import sys
from math import cos, sin, pi
from random import choice, randint
from time import sleep

import Image

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

    glTranslate(x, y, 0)
    glRotate(angle, 0, 0, 1)
    glScale(size, size, 1)

    glColor(rgbhex('#800000'))

    glBegin(GL_LINE_LOOP)
    glVertex(0, 0)
    glVertex(0, 1)
    glVertex(1, 1)
    glVertex(1, 0)
    glEnd()

    glColor(rgbhex('#B22222'))

    glBegin(GL_QUADS)
    glVertex(0, 0)
    glVertex(0, 1)
    glVertex(1, 1)
    glColor(rgbhex('#8B0000'))
    glVertex(1, 0)
    glEnd()

    glPopMatrix()
    glColor(*origin_color)

def brick_3d(x=0, y=0, size=0, angle=0):

    origin_color = glGetFloatv(GL_CURRENT_COLOR)
    glPushMatrix()

    glTranslate(x+size/2, y+size/2, 0)
    glRotate(angle, 0, 0, 1)
    glScale(size/2, size/2, size/2)

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

    glPopMatrix()

def grass(x=0, y=0, size=0, angle=0):

    origin_color = glGetFloatv(GL_CURRENT_COLOR)
    glPushMatrix()

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

    glTranslate(x, y, 0)
    glRotate(angle, 0, 0, 1)
    glScale(size, size, 1)

    glBegin(GL_POLYGON)
    disk_vertexes(1.0/size)
    glEnd()

    glPopMatrix()

def circle(x=0, y=0, size=0, angle=0):

    glPushMatrix()

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

    glTranslate(x, y, 0)
    glRotate(angle, 0, 0, 1)
    glScale(size, size, 1)

    glColor(rgbhex('#DAA520'))

    glBegin(GL_LINE_LOOP)
    glVertex(0, 0)
    glVertex(0, 1)
    glVertex(1, 1)
    glVertex(1, 0)
    glEnd()

    glColor(rgbhex('#FFFF00'))

    glBegin(GL_QUADS)
    glVertex(0, 0)
    glVertex(0, 1)
    glVertex(1, 1)
    glColor(rgbhex('#FFD700'))
    glVertex(1, 0)
    glEnd()

    glPopMatrix()
    glColor(*origin_color)

def number(x=0, y=0, size=0, angle=0):

    origin_color = glGetFloatv(GL_CURRENT_COLOR)
    glPushMatrix()

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


def load_texture(name):

    img = Image.open(name)
    img_width, img_height = img.size
    img_data = img.tostring("raw", "RGBX", 0, -1)

    texture_id = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texture_id)

    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, img_width, img_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

    return texture_id

# --- main ---

# -- globals --

UNIT = 15
UNIT_WIDTH  = 48
UNIT_HEIGHT = 27
WIDTH  = UNIT*UNIT_WIDTH
HEIGHT = UNIT*UNIT_HEIGHT

snack_face    = None # TOP, BOTTOM, LEFT, or RIGHT
snack_refresh = None # int in msec
snack_pos     = None # tuples in list

game_score = None
game_status = 'INIT'

bricks_pos = None # set
spaces_pos = None # list
fruits_pos = None # set

map_gaming   = list(open('maps/game.txt'))
map_gameover = list(open('maps/gameover.txt'))
map_numbers  = dict((i, list(open('numbers/%s.txt' % i))) for i in range(10))

texture_floor = None

# -- end --

def init():
    glClearColor(*rgbhex('#FFFFFF'))
    glEnable(GL_DEPTH_TEST)

    global texture_floor
    texture_floor = load_texture('textures/floor.png')

def render_grid():

    origin_color = glGetFloatv(GL_CURRENT_COLOR)

    glColor(rgbhex('#00FF00'))

    for x in range(0, WIDTH, UNIT):
        line(x=x, size=HEIGHT, angle=90)

    for y in range(0, HEIGHT, UNIT):
        line(y=y, size=WIDTH)

    glColor(*origin_color)

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
                brick_3d(x=UNIT*unit_x, y=UNIT*unit_y, size=UNIT)
                bricks_pos.add((unit_x, unit_y))
            elif block == 'G':
                grass(x=UNIT*unit_x, y=UNIT*unit_y, size=UNIT)

            if block != '+' and unit_y >= 2:
                spaces_pos.append((unit_x, unit_y))

            unit_x += 1

    #global texture_floor

    #glEnable(GL_TEXTURE_2D)
    #glPushMatrix()

    #glBindTexture(GL_TEXTURE_2D, texture_floor);
    #glTranslate(0, 0, -10)

    #glBegin(GL_QUADS)

    #glTexCoord(0, 0)
    #glVertex(0, 0)

    #glTexCoord(1, 0)
    #glVertex(WIDTH, 0)

    #glTexCoord(1, 1)
    #glVertex(WIDTH, HEIGHT)

    #glTexCoord(0, 1)
    #glVertex(0, HEIGHT)

    #glEnd()

    #glPopMatrix()
    #glDisable(GL_TEXTURE_2D)

def unit_disk(x=0, y=0, size=0, angle=0):
    # put center of this disk to the center of an unit
    disk(x+UNIT*0.5, y+UNIT*0.5, size*0.5, angle)

def unit_circle(x=0, y=0, size=0, angle=0):
    # put center of this disk to the center of an unit
    circle(x+UNIT*0.5, y+UNIT*0.5, size*0.5, angle)

def render_snack_body(x=0, y=0, size=0, angle=0):

    origin_color = glGetFloatv(GL_CURRENT_COLOR)

    glColor(rgbhex('#006400'))
    unit_circle(x, y, size, angle)
    glColor(rgbhex('#228B22'))
    unit_disk(x, y, size, angle)

    glColor(*origin_color)

def render_snack_head(x=0, y=0, size=0, angle=0, face='TOP'):

    origin_color = glGetFloatv(GL_CURRENT_COLOR)

    # TODO: refacor it

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

        glColor(rgbhex('#000000'))
    if face == 'TOP':
        unit_circle(x-size*0.3, y+size*0.25, size*0.4, angle)
        unit_circle(x+size*0.3, y+size*0.25, size*0.4, angle)
        glColor(rgbhex('#FFFFFF'))
        unit_disk(x-size*0.3, y+size*0.25, size*0.4, angle)
        unit_disk(x+size*0.3, y+size*0.25, size*0.4, angle)
    elif face == 'BOTTOM':
        unit_circle(x-size*0.3, y-size*0.25, size*0.4, angle)
        unit_circle(x+size*0.3, y-size*0.25, size*0.4, angle)
        glColor(rgbhex('#FFFFFF'))
        unit_disk(x-size*0.3, y-size*0.25, size*0.4, angle)
        unit_disk(x+size*0.3, y-size*0.25, size*0.4, angle)
    elif face == 'RIGHT':
        unit_circle(x+size*0.3, y-size*0.25, size*0.4, angle)
        unit_circle(x+size*0.3, y+size*0.25, size*0.4, angle)
        glColor(rgbhex('#FFFFFF'))
        unit_disk(x+size*0.3, y-size*0.25, size*0.4, angle)
        unit_disk(x+size*0.3, y+size*0.25, size*0.4, angle)
    elif face == 'LEFT':
        unit_circle(x-size*0.3, y+size*0.25, size*0.4, angle)
        unit_circle(x-size*0.3, y-size*0.25, size*0.4, angle)
        glColor(rgbhex('#FFFFFF'))
        unit_disk(x-size*0.3, y+size*0.25, size*0.4, angle)
        unit_disk(x-size*0.3, y-size*0.25, size*0.4, angle)

    render_snack_body(x, y, size, angle)

    glColor(*origin_color)

def render_snack():

    for unit_x, unit_y in reversed(snack_pos[1:]):
        render_snack_body(x=UNIT*unit_x, y=UNIT*unit_y, size=UNIT*1.3)

    if snack_pos:
        unit_x, unit_y = snack_pos[0]
        render_snack_head(x=UNIT*unit_x, y=UNIT*unit_y, size=UNIT*1.5, face=snack_face)

def render_fruits():
    for unit_x, unit_y in fruits_pos:
        fruit(x=UNIT*unit_x, y=UNIT*unit_y, size=UNIT)

def render_number(n, unit_x_offset=0, unit_y_offset=0):

    map_ = map_numbers[n]

    unit_y = UNIT_HEIGHT-unit_y_offset

    for blocks in map_:

        unit_x = unit_x_offset
        unit_y -= 1

        for block in blocks:

            if block == '+':
                number(x=UNIT*unit_x, y=UNIT*unit_y, size=UNIT)
            elif block == 'G':
                grass(x=UNIT*unit_x, y=UNIT*unit_y, size=UNIT)

            unit_x += 1

    return (unit_x, unit_y)

def render_test():

    origin_color = glGetFloatv(GL_CURRENT_COLOR)
    glPushMatrix()

    glTranslate(100, 100, 0)
    glRotate(0, 0, 0, 1)
    glScale(15, 15, 1)

    glColor(rgbhex('#B22222'))

    glBegin(GL_QUADS)
    glVertex(0, 0, -1)
    glVertex(0, 1, -1)
    glVertex(1, 1, -1)
    glColor(rgbhex('#8B0000'))
    glVertex(1, 0, -1)
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


def display():

    global snack_face
    global snack_refresh
    global snack_pos
    global fruits_pos
    global game_score
    global game_status

    if game_status == 'INIT':

        snack_face    = 'TOP'
        snack_refresh = 500
        snack_pos     = [(10, 8), (10, 7), (10, 6)]

        fruits_pos = set([(5, 5)])

        game_score = 0

        # for loading the bricks_pos and spaces_pos
        render_map(map_gaming)

        glutChangeToMenuEntry(1, 'continue', 1);

        game_status = 'GAMING'

        glutPostRedisplay()
        return

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    if game_status in ('GAMING', 'DYING', 'PAUSE'):

        render_fruits()
        render_snack()
        render_map(map_gaming)

    elif game_status == 'GAMEOVER':

        unit_x_offset = 28
        unit_y_offset = 19
        for c in str(game_score):
            pos = render_number(int(c), unit_x_offset, unit_y_offset)
            unit_x_offset = pos[0]

        render_map(map_gameover)

    render_grid()

    glutSwapBuffers()

def reshape(w, h):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glViewport(0, 0, w, h)
    glOrtho(0, w, 0, h, 0, 100)
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):

    global game_status

    if key == 'p':
        if game_status == 'GAMING':
            game_status = 'PAUSE'
        elif game_status == 'PAUSE':
            game_status = 'GAMING'
            move_snack()
    elif key == 'r':
        game_status = 'INIT'
        glutPostRedisplay()
    elif key == 'q':
        sys.exit(0)

def special(key, x, y):

    global snack_face

    if game_status == 'GAMING':

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

    global snack_refresh
    global snack_pos
    global fruits_pos
    global game_score
    global game_status

    if game_status == 'GAMING':

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

        ate_fruit = False

        if new_head_pos in fruits_pos:

            snack_refresh = int(snack_refresh*0.8)
            game_score += 1

            fruits_pos.remove(new_head_pos)
            fruits_pos.add(choice(spaces_pos))
            if randint(0, 1) == 1:
                fruits_pos.add(choice(spaces_pos))

            ate_fruit = True

        if new_head_pos in bricks_pos or new_head_pos in snack_pos:
            game_status = 'DYING'

        if not ate_fruit:
            snack_pos.pop()

        if game_status != 'DYING':
            snack_pos.insert(0, new_head_pos)

    elif game_status == 'DYING':

        snack_pos.pop()
        if not snack_pos:
            # change menu only one time
            glutChangeToMenuEntry(1, 'restart', 3);
            game_status = 'GAMEOVER'

    glutPostRedisplay()

def timer(value):
    glutTimerFunc(snack_refresh, timer, None)
    move_snack()

def menu(idx):

    global game_status

    if idx == 1:
        game_status = 'GAMING'
        glutPostRedisplay()
    elif idx == 2:
        sys.exit()
    elif idx == 3:
        game_status = 'INIT'
        glutPostRedisplay()

    return 0

if __name__ == '__main__':

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(100, 100)
    glutCreateWindow('Snack')

    init()

    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special)
    glutDisplayFunc(display)

    glutCreateMenu(menu);
    glutAddMenuEntry('continue', 1);
    glutAddMenuEntry('exit', 2);
    glutAttachMenu(GLUT_RIGHT_BUTTON);

    timer(None)

    glutMainLoop()
