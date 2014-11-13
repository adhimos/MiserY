__author__ = 'Arnaud'
import numpy as np
import random
class Hex:
    def __init__(self,index,level):
        self.index=index
        self.neighbors=[]
        self.color="EMPTY"
        self.side=[]
        self.sideconnected=[]
        self.level=level
    def getColor(self):
        return self.color
    def changeColor(self,newcolor):
        self.color=newcolor
    def getNeighbors(self):
        return self.neighbors
    def addNeighbors(self,newneigh):
        self.neighbors.append(newneigh)
    def getSide(self):
        return self.side
    def addSide(self,side):
        self.side.append(side)
        self.sideconnected.append(side)
    def isSide(self,side):
        if side in self.side:
            return True
        else:
            return False
    def getLevel(self):
        return self.level

def minindexlevel(level):
    return 1+level*(level-1)/2

def maxindexlevel(level):
    return level+(level*(level-1)/2)

def findneighbors(hex,N):
    level=hex.getLevel()
    index=hex.index
    neighindex=[]

    if minindexlevel(level)<=index-1<=maxindexlevel(level):
        neighindex.append(index-1)
    if minindexlevel(level)<=index+1<=maxindexlevel(level):
        neighindex.append(index+1)

    if level-1>0:
        if minindexlevel(level-1)<=index-(level)<=maxindexlevel(level-1):
            neighindex.append(index-(level))
        if minindexlevel(level-1)<=index-(level)+1<=maxindexlevel(level-1):
            neighindex.append(index-(level)+1)
    if level+1<N+1:
        if minindexlevel(level+1)<=index+(level)<=maxindexlevel(level+1):
            neighindex.append(index+(level))
        if minindexlevel(level+1)<=index+(level)+1<=maxindexlevel(level+1):
            neighindex.append(index+(level)+1)
    return neighindex

def findpath(hex,board):
        for neigh in hex.getNeighbors():
            if neigh.getColor()==hex.getColor(): 
                for side in neigh.sideconnected:
                    hex.sideconnected.append(side)
        shrink=[]
        if 1 in hex.sideconnected:
            shrink.append(1)
        if 2 in hex.sideconnected:
            shrink.append(2)
        if 3 in hex.sideconnected:
            shrink.append(3)
        hex.sideconnected=shrink

def update_board(board,N):
    for i in range(N):
        for hex in board.values():
            if hex.getColor()!="EMPTY":
                findpath(hex,board)
                if 1 in hex.sideconnected and 2 in hex.sideconnected and 3 in hex.sideconnected:
                    return True,hex.getColor()
    return False,"EMPTY"

def willLose(board, computerColor, index, N):
	#Faire comme update_board mais sans changer la couleur
	board[index].changeColor(computerColor)
	loses, color = update_board(board,N)
	if loses and color == computerColor:
		board[index].changeColor("EMPTY")
		return True
	board[index].changeColor("EMPTY")
	return False

def createBoard(N):
    board={}
    index=1

    for i in range(1,N+1):
        for j in range(1,i+1):

            newhex=Hex(index,i)
            if j==1:
                side=1
                newhex.addSide(side)
            if j==i:
                side=2
                newhex.addSide(side)
            if i==N:
                side=3
                newhex.addSide(side)
            board[newhex.index]=newhex
            index=index+1

    for hex in board.values():
        neighborsindex=findneighbors(hex,N)
        for index in neighborsindex:
            hex.addNeighbors(board[index])

    return board

def createCornerStack(corner,N):
	tiles = []
	if corner == 1:
		#corresponds to index 1
		tiles = range(1,N*(N+1)/2 + 1)
	elif corner == 2:
		#corresponds to index N(N+1)/2 - N+1
		for l in range(0,N):
			s = len(tiles)
			for i in range(0,l):
				tiles.append(tiles[s-i-1]+1)
			tiles.append((N-l)*(N-l+1)/2 - (N-l)+ 1) #we are at level N-l
	elif corner == 3:
		#corresponds to index N(N+1)/2
		for l in range(0,N):
			s = len(tiles)
			for i in range(0,l):
				tiles.append(tiles[s-i-1]-1)
			tiles.append((N-l)*(N-l+1)/2) #we are at level N-l
	print tiles
	return tiles

def chooseCorner(board, computerColor, N):
	#we check if there is already a played corner by the computer
	corner = 1
	cornerStack = createCornerStack(corner,N)
	while board[cornerStack[0]].getColor() != computerColor and corner < 3:
		corner = corner + 1
		cornerStack = createCornerStack(corner,N)
	#if not: choose an empty corner
	if board[cornerStack[0]].getColor() != computerColor:
		corner = 1
		cornerStack = createCornerStack(corner,N)
		while board[cornerStack[0]].getColor() != "EMPTY" and corner < 3:
			corner = corner + 1
			cornerStack = createCornerStack(corner,N)
	print 'Chosen corner: ', corner
	return cornerStack

def findNextEmpty(board, cornerStack, index):
	hex = board[cornerStack[index]]
	while hex.getColor() != "EMPTY":
		hex = board[cornerStack[index]]
		index = index + 1
	return index - 1

def nextmove(board,computercolor,N):
	move = 1
	cornerStack = chooseCorner(board, computercolor, N)
	if move:
		losing = True
		index = 0
		hex = board[cornerStack[index]]
		while losing:
			index = findNextEmpty(board, cornerStack, index)
			hex = board[cornerStack[index]]
			losing = willLose(board, computercolor, cornerStack[index], N)
			index = index + 1
		print 'Index: ', cornerStack[index - 1]        
		hex.changeColor(computercolor)
        return hex


