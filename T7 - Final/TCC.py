#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:55:21 2019

@author: vinicius
"""
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import random
import png
import math

# Escolhendo a imagem e a extensão, que neste caso sempre será .png.
pastaImagem = 'Imagens/' 
nomeImagem = 'garrafa4'
extensaoImagem = '.png'

reader = png.Reader(filename=pastaImagem+nomeImagem+extensaoImagem)
w, h, pixels, metadata = reader.read_flat()

if(metadata['alpha']):
	bytesPerPixel = 4
else:
	bytesPerPixel = 3

#print bytesPerPixel

imagemNova = [0,0,0,0] * w * h
colunaPreenchidas = [[0],[0]]

novaImagemBinaria = []

def posicao(linha, coluna):
	return bytesPerPixel*(w*linha+coluna)

# Identificando as bordas da imagem. 
for linha in range(1,h-1):
    printarImagemColuna = []
    for coluna in range(1,w-1):
        pc = posicao(linha-1,coluna)
        pb = posicao(linha+1,coluna)
        p = posicao(linha,coluna)
        pe = posicao(linha,coluna-1)
        pd = posicao(linha,coluna+1)
        dv = abs(pixels[pc]-pixels[pb])
        dh = abs(pixels[pe]-pixels[pd])
        d = int(max(dv,dh))
        if d > 10:
            printarImagemColuna.append(1)
            novaImagemBinaria.append(1)
            d = 255
        else :
            printarImagemColuna.append(0)
            novaImagemBinaria.append(0)
        imagemNova[p] = d
        imagemNova[p+1] = d
        imagemNova[p+2] = d
        imagemNova[p+3] = 255
        
    #Para printar matriz binaria da borda
    #print(printarImagemColuna)

#Gerando uma imagem só com as bordas. 
output = open(pastaImagem+nomeImagem+'Borda'+extensaoImagem, 'wb')
writer = png.Writer(w, h, **metadata)
writer.write_array(output, imagemNova)
output.close()

# Identificando o centro da imagem para poder fazer o corte no meio da imagem.
estados = ["FORA", "BORDA-1", "DENTRO", "BORDA-2"]
estado = "FORA"
coluna=0
while(coluna < w-2):
    if (estado == estados[0]):
        if (novaImagemBinaria[int(((w-2)*((h-2)/2))+coluna)] == 1):
            colunaPreenchidas[0] = coluna
            estado = "BORDA-1"
            
    if (estado == estados[1]):
        if (novaImagemBinaria[int(((w-2)*((h-2)/2))+coluna)] == 0):
            estado = "DENTRO"
            
    if (estado == estados[2]):
        if (novaImagemBinaria[int(((w-2)*((h-2)/2))+coluna)] == 1):
            colunaPreenchidas[1] = coluna
            estado = "BORDA-2"
            
    if (estado == estados[3]):
        if (novaImagemBinaria[int(((w-2)*((h-2)/2))+coluna)] == 0):
            estado = "FORA"
    # Verificando as colunas para poder verificar se o algoritmo está funcionando 
    # corretamente observando as colunas printadas. 
    #print("Coluna: ")
    #print(novaImagemBinaria[((w-2)*((h-2)/2))+coluna])
    coluna+=1

#Centro identificado.
centro = (colunaPreenchidas[0] + colunaPreenchidas[1])/2

# Printando matriz binaria cortada no centro da imagem.
#for linha in range(0,h-2):
#    printarImagemColuna = []
#    for coluna in range(0,w-2):
#        if (coluna >= centro) :
#            if (novaImagemBinaria[int(((w-2)*(linha)) + coluna)] == 1) :
#                printarImagemColuna.append(1)
#            else :
#                printarImagemColuna.append(0)
#    print(printarImagemColuna)

# Printando uma serie de variaveis que me auxiliaram nos calculos do corte
# da imagem.
#print ("Largura: ")
#print (w-2)
#print ("\n")
#print ("Altura: ")
#print(h-2)
#print("Quantidade de Colulas: ")
#print(w-2)
#print("Colulas Preenchidas: ")
#print(colunaPreenchidas[0])
#print("Colulas Preenchidas: ")
#print(colunaPreenchidas[1])
#print("Centro: ")
#print((colunaPreenchidas[0] + colunaPreenchidas[1])/2)
#print("Tamanha vet: ")
#print(len(novaImagemBinaria))
#print((h-2)*(w-2))

# TRANSFORMANDO A IMAGEM EM UM SÓLIDO EM 3D.
# Variaveis e funções de apoio.
phi0 = 0
phiF = (2*math.pi)
def Px (r, phi):
    return r*math.cos(phi)

def Pz (r, phi):
    return r*math.sin(phi)

def NormalizaH (atual) :
    return ((2.0*atual)/(h-2.0))-1.0

def NormalizaW (atual) :
    return atual/((w-2.0))

# Função que executa a transformação a imagem em sólida.
def Solido():
    glBegin(GL_TRIANGLES)
    y=(h-2)+0.0
    x=0.0
    for linha in range(0,h-2):
        printarImagemColuna = []
        for coluna in range(centro,w-2):
            if (novaImagemBinaria[int(((w-2)*(linha)) + coluna)] == 1) :
                phi = phi0
                t = NormalizaH(y)
                r = NormalizaW(x)
                while phi < phiF:
                    r1 = NormalizaW(x+1.0)
                    t1 = NormalizaH(y-1.0)
                    phi1 = phi + (math.pi/10)
                    phi2 = phi1 + (math.pi/10)
                    atual = (Px(r,phi),t,Pz(r,phi))
                    x1 =  (Px(r1,phi1), t, Pz (r1,phi1))
                    y1 = (Px(r,phi2), t1, Pz (r,phi2))
                    xy = (Px(r1,phi1), t1, Pz (r1,phi1))
                    # Determinando as faces dos triangulos.
                    # Triagulo 1
                    glVertex3fv(atual)
                    glVertex3fv(x1)
                    glVertex3fv(y1)
                    # Triangulo 2
                    glVertex3fv(x1)
                    glVertex3fv(y1)
                    glVertex3fv(xy)
                    # Para fazer o sólido sortear uma cor para cada face.
                    glColor3f(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
                    phi += (math.pi/10)
                break
            x+=1.0
        y-=1.0
        x=0.0
    # Para deixar o solido todo na cor branca.
    #glColor3f(1,1,1)
    glEnd()

# Funções para desenhar e girar o sólido na placa de vídeo.
def desenha():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Solido()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL DO GLUT
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow(nomeImagem.upper() + ' SOLIDO(A)')
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()