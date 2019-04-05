#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:24:53 2019

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
        glBegin(GL_TRIANGLES)
        glColor3f(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
        tetaAux = teta + (math.pi/50)
        phi = phi0
        while phi < phiF:
            phiAux = phi + (math.pi/25)
            p = (Qx(Px(teta),phi),Py(teta),Qz(Px(teta),phi))
            q = (Qx(Px(tetaAux),phi),Py(tetaAux),Qz(Px(tetaAux),phi)) 
            r = (Qx(Px(teta),phiAux),Py(teta),Qz(Px(teta),phiAux))
            s = (Qx(Px(tetaAux),phiAux),Py(tetaAux),Qz(Px(tetaAux),phiAux))
            glVertex3fv(p)
            glVertex3fv(q)
            glVertex3fv(r)
            glVertex3fv(r)
            glVertex3fv(s)
            glVertex3fv(q)
            phi = phi + (math.pi/25)
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