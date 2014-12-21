#Ansel Steele
#A virtual Chess board.

import math
from Tkinter import *
root = Tk()
xscr = 800
yscr = 800
cells = 8
fraction = 0.85
pieces = 32

pawn = [0.0, 0.0, 8.0, 0.0, 14.0, 6.0, 14.0, 14.0, 8.0, 20.0, 8.0, 24.0, 10.0, 44.0, 14.0, 52.0, 16.0, 54.0, 20.0, 54.0, 22.0, 56.0, 22.0, 58.0, 22.0, 60.0, 2.0, 60.0, -4.0, 60.0, -12.0, 60.0, -12.0, 56.0, -10.0, 54.0, -6.0, 54.0, -2.0, 44.0, 0.0, 20.0, -6.0, 14.0, -6.0, 6.0, 0.0, 0.0]
rook = [0, 9, 6, 9, 6, 15, 9, 15, 9, 9, 15, 9, 15, 15, 18, 15, 18, 9, 24, 9, 24, 15, 24, 18, 21, 24, 18, 33, 18, 42, 21, 51, 24, 57, 27, 57, 30, 60, 30, 63, 12, 63, 3, 63, -6, 63, -6, 60, -3, 57, 0, 57, 3, 51, 6, 42, 6, 33, 3, 24, 0, 18, 0, 9]
bishop = [0, -12, 3, -12, 6, -12, 9, -9, 9, -3, 6, 0, 9, 3, 12, 9, 15, 15, 15, 27, 12, 33, 9, 39, 9, 51, 12, 54, 15, 54, 18, 57, 18, 60, 3, 60, -12, 60, -12, 57, -9, 54, -6, 54, -3, 51, -3, 39, -6, 33, -9, 27, -9, 15, -6, 9, -3, 3, 0, 0, -3, -3, -3, -9, 0, -12]
knight = [0, -8, 0, -11, 6, -11, 9, -8, 9, -5, 15, -5, 15, -2, 12, 0, 15, 6, 15, 12, 9, 24, 9, 33, 15, 42, 15, 45, 12, 48, 12, 51, 15, 51, 18, 54, 18, 57, -15, 57, -15, 54, -12, 51, -9, 51, -9, 48, -12, 45, -15, 39, -15, 33, -15, 30, -9, 21, -6, 18, -9, 15, -12, 12, -15, 12, -18, 12, -21, 12, -24, 9, -24, 3, -21, 0, -12, 0, -6, -2, -3, -5, 0, -5, 0, -8]
king = [9, 3, 9, -3, 12, -3, 12, 3, 18, 3, 18, 6, 12, 6, 12, 15, 24, 15, 18, 27, 21, 27, 21, 33, 18, 33, 18, 57, 18, 60, 21, 60, 24, 63, 24, 66, 12, 66, 9, 66, -3, 66, -3, 63, 0, 60, 3, 60, 3, 33, 0, 33, 0, 27, 3, 27, -3, 15, 9, 15, 9, 6, 3, 6, 3, 3, 9, 3]
queen = [0, 0, -3, 9, -6, 3, -9, 9, -12, 3, -9, 15, -6, 21, -3, 24, -9, 30, -3, 33, -6, 33, -6, 36, -3, 36, 0, 39, 0, 63, -3, 66, -3, 69, 21, 69, 21, 66, 18, 63, 18, 39, 21, 36, 24, 36, 24, 33, 21, 33, 27, 30, 21, 24, 24, 21, 27, 15, 30, 3, 27, 9, 24, 3, 21, 9, 18, 0, 0, 0]
wknight = [18, -8, 18, -11, 12, -11, 9, -8, 9, -5, 3, -5, 3, -2, 6, 0, 3, 6, 3, 12, 9, 24, 9, 33, 3, 42, 3, 45, 6, 48, 6, 51, 3, 51, 0, 54, 0, 57, 33, 57, 33, 54, 30, 51, 27, 51, 27, 48, 30, 45, 33, 39, 33, 33, 33, 30, 27, 21, 24, 18, 27, 15, 30, 12, 33, 12, 36, 12, 39, 12, 42, 9, 42, 3, 39, 0, 30, 0, 24, -2, 21, -5, 18, -5, 18, -8]

movepawn = [[1,0],[1,1],[1,-1]]
moveknight = [[2,1],[-2,1],[2,-1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
movebishop = [[1,1],[-1,1],[1,-1],[-1,-1]]
moverook = [[1,0],[-1,0],[0,1],[0,-1]]
movequeen = movebishop + moverook
moveking = movequeen

polydict = {}
polydict['pawn'] = pawn
polydict['rook'] = rook
polydict['knight'] = knight
polydict['bishop'] = bishop
polydict['queen'] = queen
polydict['king'] = king
polydict['wknight'] = wknight

instructions = ['rook','knight','bishop','queen','king','bishop','knight','rook',
'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']


def boardSize(xscr,yscr,cells,fraction):
	if xscr > yscr:
		side = yscr
	else:
		side = xscr
	side = side * fraction
	side = side - (side%cells)
	return side

side = boardSize(xscr,yscr,cells,fraction)

class Board:


	def __init__(self,cells,side,root,pieces,polydict,instructions):

		self.canvas = Canvas(root,width = side,height = side)
		self.canvas.pack()
		self.canvas.bind('<Button-1>',self.click)

		self.cells = cells
		self.side = side
		self.spacing = side/cells
		self.polydict = polydict
		self.pieces = pieces
		self.instructions = instructions
		self.selected = 0
		self.piecedata = []
		self.colorpairs = {}
		self.unmoved = []
		self.castleinfo = []
		self.turn = "white"


	def drawBoard(self):

		oscillate = 1
		self.canvas.create_rectangle(0,0,self.side,self.side,fill = 'black')
		midpoints = []

		for x in range(0,cells+1):

			for y in range(0,cells+1):

				cornerx1 = (self.spacing * x) - self.spacing
				cornery1 = (self.spacing * y) - self.spacing
				cornerx2 = self.spacing * x
				cornery2 = self.spacing * y

				avgx = (cornerx1 + cornerx2)/2
				avgy = (cornery1 + cornery2)/2

				midpoint = [avgx,avgy]
				midpoints.append(midpoint)

				oscillate = oscillate * -1

				if oscillate == 1:

					self.canvas.create_rectangle(cornerx1,cornery1,cornerx2,cornery2,fill = 'red')

				else:

					self.canvas.create_rectangle(cornerx1,cornery1,cornerx2,cornery2,fill = 'blue')

		return midpoints


	def makePiece(self,name,color,ptype,squarey,squarex):

		data = []
		coords = self.polydict[ptype]

		if ptype == "knight" and color == "white":

			coords = self.polydict["wknight"]

		self.canvas.create_polygon(coords,fill = color,tag = name)

		xmove = squarex * self.spacing
		ymove = squarey * self.spacing

		self.canvas.tag_raise(name)
		self.canvas.move(name,xmove,ymove)

		data = [name,color,ptype,squarex,squarey]

		self.unmoved.append(name)

		return data


	def setup(self,color):

		newpieces = self.pieces/2

		if color == 'white':

			rows = [0,1]

		else:

			rows = [7,6]

		for count in range(0,newpieces):

			if count < 8:

				row = rows[0]
				column = count

			else:

				row = rows[1]
				column = count - 8

			ptype = self.instructions[count]
			name = ptype + str(count) + str(color)
			data = self.makePiece(name,color,ptype,column,row)

			self.piecedata.append(data)
			self.colorpairs[(row,column)] = color

		self.allign()


	def allign(self):

		for piece in self.piecedata:

			tagger = piece[0]
			color = piece[1]
			ptype = piece[2]
			mover = [0,0]

			if ptype == "pawn":

				if color == "white":
					mover = [36,8]
				else:
					mover = [20,4]

			if ptype == "knight":

				if color == "white":
					mover = [24,16]
				else:
					mover = [22,9]

			if ptype == "rook":

				if color == "white":
					mover = [30,3]
				else:
					mover = [16,3]

			if ptype == "king":

				if color == "white":
					mover = [33,9]
				else:
					mover = [18,5]

			if ptype == "queen":

				if color == "white":
					mover = [31,7]
				else:
					mover = [19,5]

			if ptype == "bishop":

				if color == "white":
					mover = [37,17]
				else:
					mover = [22,8]
		
			self.canvas.move(tagger,mover[0],mover[1])


	def click(self,event):

		xclick = event.x
		yclick = event.y

		if self.selected == 0:

			row = int(yclick/self.spacing)
			column = int(xclick/self.spacing)

			for piece in self.piecedata:

				if column == piece[3] and row == piece[4]:

					if piece[1] != self.turn:
						return

					self.selected = piece
					self.possible = self.pieceCheck()

					if self.selected[2] == "king":

						self.castleCheck()

		else:

			newtag = self.selected[0]
			color = self.selected[1]
			ptype = self.selected[2]
			xstart = self.selected[3] * self.spacing
			ystart = self.selected[4] * self.spacing

			xend = int(xclick/self.spacing)
			yend = int(yclick/self.spacing)

			if (xend,yend) not in self.possible:

				self.selected = 0
				return

			xend = xend * self.spacing
			yend = yend * self.spacing

			self.piecedata.remove(self.selected)

			xcoords = int(xclick/self.spacing)
			ycoords = int(yclick/self.spacing)

			if (xcoords,ycoords) in self.colorpairs.keys():

				del self.colorpairs[(xcoords,ycoords)]

				for item in self.piecedata:

					if item[3] == xcoords and item[4] == ycoords:

						self.piecedata.remove(item)
						tagger = item[0]
						self.canvas.delete(tagger)

			xmove = xend - xstart
			ymove = yend - ystart
			self.canvas.move(newtag,xmove,ymove)

			newdata = [newtag,color,ptype,xcoords,ycoords]
			self.piecedata.append(newdata)

			if ptype == "king" and math.fabs(self.selected[4] - ycoords) == 2:

				self.castRook(ycoords)

			del self.colorpairs[(self.selected[3],self.selected[4])]

			try:

				self.unmoved.remove(newtag)
				
			except:

				pass

			self.selected = 0

			self.colorpairs[(xcoords,ycoords)] = color

			if self.turn == "white":
				self.turn = "black"
			else:
				self.turn = "white"


	def pieceCheck(self):

		static = False
		color = self.selected[1]
		ptype = self.selected[2]
		xposit = self.selected[3]
		yposit = self.selected[4]

		if ptype == "pawn":
			return self.pawnCheck()
		if ptype == "knight":
			move = moveknight
			static = True
		if ptype == "bishop":
			move = movebishop
		if ptype == "rook":
			move = moverook
		if ptype == "queen":
			move = movequeen
		if ptype == "king":
			move = moveking
			static = True

		pmoves = []

		if static == True:

			for item in move:

				newx = xposit + item[0]
				newy = yposit + item[1]
				newcoords = (newx,newy)

				if newcoords in self.colorpairs and self.colorpairs[newcoords] == color:

					continue

				else:

					pmoves.append(newcoords)

		else:

			for item in move:

				done = False
				newx = xposit
				newy = yposit

				while not done:

					newx = newx + item[0]
					newy = newy + item[1]
					newcoords = (newx,newy)

					if newcoords in self.colorpairs and self.colorpairs[newcoords] == color:

						done = True

					elif newx > 7 or newx < 0 or newy > 7 or newy < 0:

						done = True

					else:

						pmoves.append(newcoords)

		return pmoves


	def pawnCheck(self):

		pmoves = []

		color = self.selected[1]
		xposit = self.selected[3]
		yposit = self.selected[4]

		mpawn = movepawn

		if color == "black":

			mpawn = [[-1,0],[-1,1],[-1,-1]]

		forward1 = mpawn[0]
		bigx = forward1[0] * 2

		attack1 = mpawn[1]
		attack2 = mpawn[2]

		newx = xposit + forward1[0]
		newy = yposit
		pair = (newx,yposit)

		if pair not in self.colorpairs.keys():

			pmoves.append(pair)

		if color == "white" and xposit == 1 or color == "black" and xposit == 6:

			newx = xposit + bigx
			newy = yposit
			pair = (newx,newy)

			if pair not in self.colorpairs.keys():

				pmoves.append(pair)

		newx = xposit + attack1[0]
		newy = yposit + attack1[1]
		pair = (newx,newy)

		if pair in self.colorpairs.keys() and self.colorpairs[pair] != color:

			pmoves.append(pair)

		newx = xposit + attack2[0]
		newy = yposit + attack2[1]
		pair = (newx,newy)

		if pair in self.colorpairs.keys() and self.colorpairs[pair] != color:

			pmoves.append(pair)

		return pmoves


	def castleCheck(self):

		self.castleinfo = []
		kingx = self.selected[3]
		kingy = self.selected[4]
		tagger = self.selected[0]
		color = self.selected[1]

		if tagger in self.unmoved:

			for item in self.piecedata:

				if item[1] == color and item[2] == "rook" and item[0] in self.unmoved:

					rookx = item[3]
					rooky = item[4]

					if rooky < kingy:

						castle = True

						for y in range(1,4):

							if (rookx,rooky + y) not in self.colorpairs.keys():

								continue

							else:

								castle = False

						if castle == True:

							self.possible.append((kingx,kingy - 2))
							self.castleinfo.append((item[0],kingy - 2))

					if rooky > kingy:

						castle = True

						for y in range(1,3):

							if (rookx,rooky - y) not in self.colorpairs.keys():

								continue

							else:

								castle = False

						if castle == True:

							self.possible.append((kingx,kingy + 2))
							self.castleinfo.append((item[0],kingy + 2))


	def castRook(self,newy):

		for item in self.castleinfo:

			if item[1] == newy:

				tagger = item[0]

		for item in self.piecedata:

			if item[0] == tagger:

				correct = item

		if newy > correct[4]:

			finaly = newy + 1

		if newy < correct[4]:

			finaly = newy - 1

		tagger = correct[0] 
		color = correct[1]
		ptype = correct[2]
		xcoords = correct[3]
		ycoords = correct[4]

		ystart = ycoords * self.spacing
		yend = finaly * self.spacing
		ymove = yend - ystart

		newdata = [tagger,color,ptype,xcoords,finaly]

		self.canvas.move(tagger,0,ymove)

		self.piecedata.remove(correct)

		self.piecedata.append(newdata)

		del self.colorpairs[(xcoords,ycoords)]

		self.unmoved.remove(tagger)

		self.colorpairs[(xcoords,finaly)] = color		
		

	def animate(self):
		while True:
			self.canvas.update()


chess = Board(cells,side,root,pieces,polydict,instructions)

chess.drawBoard()
chess.setup('black')
chess.setup('white')
chess.animate()

root.mainloop()
