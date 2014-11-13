import pygame
from pygame.locals import *

pygame.init()

N=8
windwowsize=600

class hexgrapg:
    def __init__(self,perso,persox,persoy):
        self.persox=persox
        self.persoy=persoy
        self.perso=perso

hexsizex=44
hexsizey=70

maxhexy=windwowsize/hexsizey
decalage=(maxhexy-N)*hexsizey

hexstartx=windwowsize/2
hexstarty=decalage


fenetre = pygame.display.set_mode((windwowsize, windwowsize))



fond = pygame.image.load("fond.jpg").convert()
fenetre.blit(fond, (0,0))

hexlist=[]
for i in range(N):
        for j in range(i):
            perso = pygame.image.load("hex.png").convert_alpha()
            perso_x = hexstartx-(i)*hexsizex/2+j*hexsizex
            perso_y = hexstarty+i*hexsizey/2
            hexlist.append(hexgrapg(perso,perso_x,perso_y))
for hex in hexlist:
    fenetre.blit(hex.perso, (hex.persox, hex.persoy))


pygame.display.flip()

continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                perso_x = event.pos[0]
                perso_y = event.pos[1]


    fenetre.blit(fond,(0,0))
    for hex in hexlist:
        fenetre.blit(hex.perso, (hex.persox, hex.persoy))
    pygame.display.flip()