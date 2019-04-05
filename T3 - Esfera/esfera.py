#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:37:22 2019

@author: vinicius
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 15:46:34 2019

@author: vinicius
"""

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import random
import math

teta0 = (-math.pi)/2
tetaF = (math.pi) /2
phi0 = 0
phiF = (2*math.pi)
r = 3

def Px (teta):
    return r*math.cos(teta)

def Py (teta):
    return r*math.sin(teta)

def Qx (r2,phi):
    return r2*math.cos(phi)

def Qz (r2,phi):
    return r2*math.sin(phi)

def Esfera():
    teta = teta0
    phi = phi0
    while teta < tetaF:
        glBegin(GL_POINTS)
        glVertex3f(Px(teta),Py(teta),0)
        glColor3f(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
        phi = phi0
        while phi < phiF:
            glVertex3f(Qx(Px(teta),phi),Py(teta),Qz(Px(teta),phi))
            phi = phi + (math.pi/100)
        glEnd()
        teta = teta + (math.pi/50)
        
def desenha():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Esfera()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("ESFERA")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()


