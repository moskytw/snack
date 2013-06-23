import sys

try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print '''
ERROR: PyOpenGL not installed properly.
        '''
  sys.exit()


spin = 0

#  Initialize material property, light source, lighting model,
#  and depth buffer.
def init():
   glClearColor (0.0, 0.0, 0.0, 0.0)
   glShadeModel (GL_SMOOTH)
   glEnable(GL_LIGHTING)
   glEnable(GL_LIGHT0)
   glEnable(GL_DEPTH_TEST)

#  Here is where the light position is reset after the modeling
#  transformation (glRotated) is called.  This places the
#  light at a new position in world coordinates.  The cube
#  represents the position of the light.
def display():
   position =  [0.0, 0.0, 1.5, 1.0]

   glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   glPushMatrix ()
   gluLookAt (0.0, 0, 5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

   glPushMatrix ()
   glRotated (spin, 1.0, 0.0, 0.0)
   glLightfv (GL_LIGHT0, GL_POSITION, position)

   glTranslated (0.0, 0.0, 1.5)
   glDisable (GL_LIGHTING)
   glColor3f (0.0, 1.0, 1.0)
   glutWireCube (0.1)
   glEnable (GL_LIGHTING)
   glPopMatrix ()

   glutSolidTorus (0.275, 0.85, 8, 15)
   glPopMatrix ()
   glFlush ()

def reshape (w, h):
   glViewport (0, 0, w, h)
   glMatrixMode (GL_PROJECTION)
   glLoadIdentity()
   gluPerspective(40.0, w/h, 1.0, 20.0)
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()

def mouse(button, state, x, y):
   global spin
   if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
       spin = (spin + 30) % 360
       glutPostRedisplay()

def keyboard(key, x, y):
   if key == chr(27):
       sys.exit(0)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (500, 500);
glutInitWindowPosition(100, 100)
glutCreateWindow("movelight")
init()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMouseFunc(mouse)
glutKeyboardFunc(keyboard)
glutMainLoop()
