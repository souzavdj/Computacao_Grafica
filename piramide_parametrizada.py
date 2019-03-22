#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 20:02:48 2019

@author: vinicius
"""

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import random
import sys

h = int (sys.argv[1]) if len(sys.argv) > 1 else 1.7
qtdlados = int (sys.argv[2]) if len(sys.argv) > 2 else 4

if (qtdlados < 3) :
    print("\nPara se caracterizar uma piramide, a base tem que ter mais de 2 lados.\n")
    sys.exit()
    
angulo = (2*math.pi)/qtdlados
#faces = 2*qtdlados;
#vertices = qtdlados + 2;
#linhas = 3*qtdlados
#cores = 2*qtdlados
anguloAtual = 0
vertices = ()
vertices += (( 0, h, 0), (1, 0, 0),)

for i in range (0, qtdlados-1) :
    anguloAtual += angulo
    vertices += ((math.cos(anguloAtual), 0, -math.sin(anguloAtual)),)
vertices +=(( 0, 0, 0),)


linhas = ()
for i in range (1, qtdlados+1):
    linhas += ((0,i),)
    
for i in range (1, qtdlados):
    linhas += ((i,i+1),)
linhas += ((qtdlados,1),)
#for i in range (1,qtdlados+1):
#    linhas += ((qtdlados+1, i),)


faces = ()
for i in range (1, qtdlados+1):
    faces += ((0,i,i+1),)    
faces += ((0,qtdlados, 1),)
for i in range (1, qtdlados):
    faces += ((qtdlados+1,i,i+1),)
faces += ((qtdlados+1,qtdlados,1),)    

cores = ()
for i in range (0,qtdlados+1):
    cores += ((random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)),)
corDaBase = random.uniform(0,1)
for i in range (0,qtdlados+2):
    cores += ((corDaBase,corDaBase,corDaBase),)

def Piramide():
    glBegin(GL_TRIANGLES)
    i = 0
    for face in faces:
        glColor3fv(cores[i])
        for vertex in face:
            #glColor3fv(cores[vertex])
            glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()

    glColor3fv((0,0.5,0))
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()

def desenhar():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(3,2,4,0)
    Piramide()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Piramide")
glutDisplayFunc(desenhar)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
