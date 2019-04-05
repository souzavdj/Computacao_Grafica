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

a = 1
b = 1
px = 100.0 
py = 100.0
x0 = -2
xf =  2
y0 = -2
yf =  2


def f(x,y):
    return (x*x)/a*a + (y*y)/b*b


def Rede():
    dx=(xf-x0)/px
    dy=(yf-y0)/py
    y=y0
    while (y < yf):
        x=x0
        glBegin(GL_QUAD_STRIP)
        glColor3f(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
        #glColor3f(1,1,1)
        while (x < xf):
            glVertex3f(x,y,f(x,y))
            glVertex3f(x,y+dy,f(x,y+dy))
            x += dx
        y+=dy
        glEnd()

def desenha():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Rede()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("REDE")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()


