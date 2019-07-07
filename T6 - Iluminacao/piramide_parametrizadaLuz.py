#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:30:24 2019

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

#https://www.opengl.org/wiki/Calculating_a_Surface_Normal
#Begin Function CalculateSurfaceNormal (Input Triangle) Returns Vector
#  Set Vector U to (Triangle.p2 minus Triangle.p1)
#  Set Vector V to (Triangle.p3 minus Triangle.p1)
#  Set Normal.x to (multiply U.y by V.z) minus (multiply U.z by V.y)
#  Set Normal.y to (multiply U.z by V.x) minus (multiply U.x by V.z)
#  Set Normal.z to (multiply U.x by V.y) minus (multiply U.y by V.x)
#  Returning Normal
#End Function
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

def Piramide():
	glBegin(GL_TRIANGLES)
	for face in faces:
		glNormal3fv(calculaNormalFace(face))
		for vertex in face:
			glVertex3fv(vertices[vertex])
	glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Piramide()
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
    glutCreateWindow("Piramide com Luz")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutTimerFunc(50,timer,1)
    init()
    glutMainLoop()

main()
