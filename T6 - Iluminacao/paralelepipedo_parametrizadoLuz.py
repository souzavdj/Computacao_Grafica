#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 00:38:48 2019

@author: vinicius
"""

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
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
    faces += ((i+1,i,i+qtdlados),)
    faces += ((i+1,i+qtdlados,i+qtdlados+1),)
faces += ((1, qtdlados,2*qtdlados),)
faces += ((1,2*qtdlados,qtdlados+1),)

for i in range (1, qtdlados):
    faces += (((2*qtdlados)+1,i+qtdlados,i+qtdlados+1),)
faces += (((2*qtdlados)+1,2*qtdlados,qtdlados+1),)    

def calculaNormalFace(face):
    x = 0
    y = 1
    z = 2
    v0 = vertices[face[0]]
    v1 = vertices[face[1]]
    v2 = vertices[face[2]]
    U = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
    V = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
    N = ( (U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
    NLength = math.sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
    return ( N[x]/NLength, N[y]/NLength, N[z]/NLength)

def calculaNormalFaceLado(face):
    x = 0
    y = 1
    z = 2
    v0 = vertices[face[0]]
    v1 = vertices[face[1]]
    v2 = vertices[face[2]]
    U = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
    V = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
    N = ( (U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
    NLength = math.sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
    return ( N[x]/NLength, N[y]/NLength, N[z]/NLength)

def Paralelepipedo():    
    for face in faces:
        glBegin(GL_TRIANGLES)
        glNormal3fv(calculaNormalFace(face))
        for vertex in face:
            glVertex3fv(vertices[vertex])
        glEnd()
    
def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Paralelepipedo()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,1,5,0,0,0,0,1,0)

def init():
    mat_ambient = (0.0, 0.0, 0.5, 1.0)
    mat_ambient = (0.4, 0.0, 0.0, 1.0)
    mat_diffuse = (1.0, 0.0, 0.0, 1.0)
    mat_specular = (0.0, 1.0, 0.0, 1.0)
    mat_shininess = (50,)
    light_position = (0.5, 0.5, 0.5)
    glClearColor(0.0,0.0,0.0,0.0)
    glShadeModel(GL_FLAT)
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Paralelepipedo Parametrizado com Luz")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutTimerFunc(50,timer,1)
    init()
    glutMainLoop()

main()
