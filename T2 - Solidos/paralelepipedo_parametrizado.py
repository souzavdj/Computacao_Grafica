#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 00:56:16 2019

@author: vinicius
"""

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import random
import sys

h = int (sys.argv[1]) if len(sys.argv) > 1 else 2
qtdlados = int (sys.argv[2]) if len(sys.argv) > 2 else 4

if (qtdlados < 3) :
    print("\nPara se caracterizar um prisma, a base tem que ter mais de 2 lados.\n")
    sys.exit()

angulo = (2*math.pi)/qtdlados
#faces = qtdlados*qtdlados;
#vertices = 2*qtdlados + 1;
#linhas = 5*qtdlados
#cores = *qtdfaces + 2
anguloAtual = 0
vertices = ()
vertices += (( 0, h, 0),)
for i in range (0, qtdlados) :
    vertices += ((math.cos(anguloAtual), h, -math.sin(anguloAtual)),)
    anguloAtual += angulo
anguloAtual = 0
for i in range (0, qtdlados) :
    vertices += ((math.cos(anguloAtual), 0, -math.sin(anguloAtual)),)
    anguloAtual += angulo
vertices +=(( 0, 0, 0),)


linhas = ()
#for i in range (1, qtdlados+1):
#    linhas += ((0,i),)
    
for i in range (1, qtdlados):
    linhas += ((i,i+1),)
linhas += ((qtdlados,1),)

for i in range (1,qtdlados+1):
    linhas += ((i, i+qtdlados),)

for i in range (qtdlados+1, 2*qtdlados):
    linhas +=((i,i+1),)
linhas += (((2*qtdlados),qtdlados+1),)

#for i in range (qtdlados+1,(2*qtdlados)+1):
#    linhas += (((2*qtdlados+1), i),)

faces = ()
for i in range (1, qtdlados):
    faces += ((0,i,i+1),)    
faces += ((0,qtdlados, 1),)

for i in range (1, qtdlados):
    faces += ((i,i+1,i+qtdlados),)
    faces += ((i+1,i+qtdlados,i+qtdlados+1),)
faces += ((qtdlados,1,2*qtdlados),)
faces += ((1,2*qtdlados,qtdlados+1),)

for i in range (1, qtdlados):
    faces += (((2*qtdlados)+1,i+qtdlados,i+qtdlados+1),)
faces += (((2*qtdlados)+1,2*qtdlados,qtdlados+1),)    

cores = ()
cor1 = random.uniform(0,1)
cor2 = random.uniform(0,1)
cor3 = random.uniform(0,1)
for i in range (0,qtdlados):
    cores += ((cor1,cor2,cor3),)

for i in range (0,qtdlados):
    cor1 = random.uniform(0,1)
    cor2 = random.uniform(0,1)
    cor3 = random.uniform(0,1)
    cores += ((cor1,cor2,cor3),)
    cores += ((cor1,cor2,cor3),)

cor1 = random.uniform(0,1)
cor2 = random.uniform(0,1)
cor3 = random.uniform(0,1)
for i in range (0,qtdlados+2):
    cores += ((cor1,cor2,cor3),)
    
def Paralelepipedo():
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
    Paralelepipedo()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Paralelepipedo Parametrizado")
glutDisplayFunc(desenhar)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
