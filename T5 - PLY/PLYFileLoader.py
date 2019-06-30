#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:29:20 2019

@author: vinicius
"""

from OpenGL.GL import *

class PLY:
    def __init__(self, filename, swapyz=False):
        """Loads a Wavefront PLY file. """
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []
        qtd_vertex = 0
        iVertex = 0
        iFaces = 0
        qtd_faces = 0
        #material = None
        for line in open(filename, "r"):
            if line.startswith('#'): continue
            if line.startswith('ply'): continue
            if line.startswith('format'): continue
            if line.startswith('comment'): continue
            if line.startswith('property'): continue
            if line.startswith('element'): 
                values = line.split()
                if (values[1] == 'vertex'):
                    qtd_vertex = int(values[2])
                if (values[1] == 'face'):
                    qtd_faces = int(values[2])
                continue
            if line.startswith("end_header"): continue
            values = line.split()
            #if (iVertex == 0):
                #print("Qtd Vertex", qtd_vertex)
                #print("Qtd Faces", qtd_faces)
            if (iVertex < qtd_vertex):
                v = map(float, values[0:3])
                self.vertices.append(v)
                #print("Vertice: ", self.vertices[iVertex])
                iVertex+=1
                continue
            if (iFaces < qtd_faces):
                indices_face = map(int, values[1:4])
                v = self.vertices[indices_face[0]], self.vertices[indices_face[1]], self.vertices[indices_face[2]]
                self.faces.append(v)
                #print("Face: ", self.faces[iFaces])
                iFaces+=1
                continue
        self.gl_list = glGenLists(1)
        glNewList(self.gl_list, GL_COMPILE)
        glFrontFace(GL_CCW)
        glBegin(GL_TRIANGLES)
        
        for face in self.faces:
            glColor3f(1,1,1)
            for vertex in face:
                glVertex3fv(vertex)
            
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glEndList()
        