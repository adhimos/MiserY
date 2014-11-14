__author__ = 'Arnaud'
import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
import Buttons
import Hex

class hexgrapg:
    def __init__(self,perso,persox,persoy):
        self.persox=persox
        self.persoy=persoy
        self.perso=perso
    def pressed(self,mouse):
        if mouse[0] > self.persox+10:
            if mouse[1] > self.persoy+10:
                if mouse[0] < self.persox+hexsizex-10:
                    if mouse[1] < self.persoy+hexsizey-10:
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False

class Coin:
    def __init__(self,perso,color,x,y):
        self.imsizex=30
        self.imsizey=30
        self.color=color
        self.x=x
        self.y=y
        self.xplot=x
        self.yplot=y
        self.perso=perso
        self.computePlotValues()
    def computePlotValues(self):
        self.xplot=self.x+hexsizex/2-self.imsizex/2+3
        self.yplot=self.y+hexsizey/2-self.imsizey/2-7
    def getXplot(self):
        return self.xplot
    def getYplot(self):
        return self.yplot

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,20), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204,24), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (0,0,0)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()

def ask(screen, question):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  display_box(screen, question + " = " + string.join(current_string,""))
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, question + " = " + string.join(current_string,""))
  return string.join(current_string,"")

def refreshboard(fenetre,hexlist,coinlist,buttonlist):
    fenetre.blit(fond,(0,0))
    for hex in hexlist:
        fenetre.blit(hex.perso, (hex.persox, hex.persoy))
    for coin in coinlist:
        fenetre.blit(coin.perso, (coin.getXplot(), coin.getYplot()))
    for button in buttonlist:
        button.draw(fenetre)
    pygame.display.flip()

def draw_board(N):
    hexboard=Hex.createBoard(N)
    board={}
    index=1
    for i in range(N+1):
        for j in range(i):
            perso = pygame.image.load("hex.png").convert_alpha()
            perso_x = hexstartx-(i)*hexsizex/2+j*hexsizex
            perso_y = hexstarty+i*hexsizey/2
            hexgraph=hexgrapg(perso,perso_x,perso_y)
            hexlist.append(hexgraph)
            board[hexgraph]=hexboard[index]
            index+=1
    return (board,hexboard)

pygame.init()

windwowsize=600

hexsizex=44
hexsizey=70

maxhexy=windwowsize/hexsizey
decalage=10

hexstartx=windwowsize/2
hexstarty=decalage

fenetre = pygame.display.set_mode((windwowsize, windwowsize))
fond = pygame.image.load("fond.jpg").convert()
redcoin = pygame.image.load("redcoin.png").convert_alpha()
blackcoin = pygame.image.load("blackcoin.png").convert_alpha()
fenetre.blit(fond, (0,0))

clock = pygame.time.Clock()

hexlist=[]
coinlist=[]
buttonlist=[]

reset=Buttons.Button((107,142,35), 50, 3*windwowsize/4, 200,    windwowsize/5,    0,        "RESET", (255,255,255))
buttonlist.append(reset)

pygame.display.flip()
N=8
continuer = 1
while continuer:
    ninput=1
    notreset=1
    choosemode=1

    vscomputerbool=False
    hexlist=[]
    coinlist=[]
    computercolor="BLACK"


    fenetre.blit(fond, (0,0))
    vscomputer=Buttons.Button((107,142,35), 50, windwowsize/2-windwowsize/8, 200,   windwowsize/4 ,    0,        "VS COMPUTER", (255,255,255))
    vsplayer=Buttons.Button((107,142,35), windwowsize/2+50, windwowsize/2-windwowsize/8, 200,   windwowsize/4 ,    0,        "VS PLAYER", (255,255,255))
    vscomputer.draw(fenetre)
    vsplayer.draw(fenetre)
    pygame.display.flip()

    while choosemode:
        for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = 0
                    choosemode=0
                    ninput=0
                    notreset=0
                    black=0
                    red=0
                elif event.type == MOUSEBUTTONDOWN:
                        if vscomputer.pressed(pygame.mouse.get_pos()):
                            vscomputerbool=True
                            choosemode=0
                        elif vsplayer.pressed(pygame.mouse.get_pos()):
                            vscomputerbool=False
                            choosemode=0

    if vscomputerbool:
        fenetre.blit(fond, (0,0))
        computerbegins=Buttons.Button((107,142,35), 50, windwowsize/2-windwowsize/8, 200,   windwowsize/4 ,    0,        "COMPUTER BEGINS", (255,255,255))
        playerbegins=Buttons.Button((107,142,35), windwowsize/2+50, windwowsize/2-windwowsize/8, 200,   windwowsize/4 ,    0,        "PLAYER BEGINS", (255,255,255))
        computerbegins.draw(fenetre)
        playerbegins.draw(fenetre)
        pygame.display.flip()

        choosemode=1
        while choosemode:
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = 0
                    choosemode=0
                    ninput=0
                    notreset=0
                    black=0
                    red=0
                elif event.type == MOUSEBUTTONDOWN:
                        if computerbegins.pressed(pygame.mouse.get_pos()):
                            computercolor="BLACK"
                            choosemode=0
                        elif playerbegins.pressed(pygame.mouse.get_pos()):
                            computercolor="RED"
                            choosemode=0

    fenetre.blit(fond, (0,0))
    pygame.display.flip()
    while ninput:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
                ninput=0
                notreset=0

        #Nchar=ask(fenetre,"SIZE")
        #N=int(Nchar)
	N = 5
        ninput=0

    graphboard,board=draw_board(N)
    while notreset:
        black=1
        red=1
        refreshboard(fenetre,hexlist,coinlist,buttonlist)
        if vscomputerbool and computercolor=="BLACK":
            hexnextmove=Hex.nextmove(board,computercolor,N)
            for hexgraph in graphboard.keys():
                if graphboard[hexgraph].index==hexnextmove.index:
                    coin=Coin(blackcoin,"BLACK",hexgraph.persox,hexgraph.persoy)
                    coinlist.append(coin)
        else:
            while black:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        continuer = 0
                        ninput=0
                        notreset=0
                        black=0
                        red=0
                    elif event.type == MOUSEBUTTONDOWN:
                        for button in buttonlist:
                            if button.pressed(pygame.mouse.get_pos()):
                                if button.text=="RESET":
                                    notreset=0
                                    black=0
                                    red=0
                        for hexgraph in hexlist:
                            boardhex=graphboard[hexgraph]
                            if hexgraph.pressed(pygame.mouse.get_pos()) and boardhex.getColor()=="EMPTY":
                                coin=Coin(blackcoin,"BLACK",hexgraph.persox,hexgraph.persoy)
                                coinlist.append(coin)
                                boardhex.changeColor("BLACK")
                                black=0
        refreshboard(fenetre,hexlist,coinlist,buttonlist)
        finished,losercolor=Hex.update_board(board,N)

        if finished:
            end=Buttons.Button((255,255,255), windwowsize/2, windwowsize-200, 200,   windwowsize/4 ,    0,        losercolor+" LOSES", (107,142,35))
            end.draw(fenetre)
            pygame.display.flip()
        if vscomputerbool and computercolor=="RED":
            hexnextmove=Hex.nextmove(board,computercolor,N)
            for hexgraph in graphboard.keys():
                if graphboard[hexgraph].index==hexnextmove.index:
                    coin=Coin(redcoin,"RED",hexgraph.persox,hexgraph.persoy)
                    coinlist.append(coin)
        else:
            while red:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        continuer = 0
                        ninput=0
                        notreset=0
                        black=0
                        red=0
                    elif event.type == MOUSEBUTTONDOWN:
                        for button in buttonlist:
                            if button.pressed(pygame.mouse.get_pos()):
                                if button.text=="RESET":
                                    notreset=0
                                    red=0
                        for hexgraph in hexlist:
                            boardhex=graphboard[hexgraph]
                            if hexgraph.pressed(pygame.mouse.get_pos()) and boardhex.getColor()=="EMPTY":
                                coin=Coin(redcoin,"RED",hexgraph.persox,hexgraph.persoy)
                                coinlist.append(coin)
                                boardhex.changeColor("RED")
                                red=0
        finished,losercolor=Hex.update_board(board,N)
        if finished:
            end=Buttons.Button((255,255,255), windwowsize/2, windwowsize-200, 200,   windwowsize/4 ,    0,        losercolor+" LOSES", (107,142,35))
            end.draw(fenetre)
            pygame.display.flip()
    clock.tick(60)
