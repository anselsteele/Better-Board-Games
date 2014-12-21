#Ansel Steele
#A virtual Go board.

from Tkinter import *
import copy

root = Tk()

xscr = root.winfo_screenwidth()
yscr = root.winfo_screenheight()

cells = 21
fraction = 0.85


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


	def __init__(self,cells,side,root):

		self.canvas = Canvas(root,width = side,height = side,highlightthickness = 0)
		self.canvas.pack()
		self.canvas.bind('<Button-1>',self.click)

		self.cells = cells
		self.side = side
		self.spacing = side/cells
		self.whitegroups = {}
		self.blackgroups = {}
		self.allpieces = {}
		self.count = 0
		self.turn = "black"
		self.liberties = [[1,0],[0,1],[-1,0],[0,-1]]
		



	def drawBoard(self):

		boardcoords = []

		for row in range(1,self.cells):

			for column in range(1,self.cells):

				cornerx1 = column * self.spacing-self.spacing
				cornery1 = row * self.spacing-self.spacing
				cornerx2 = cornerx1 + self.spacing
				cornery2 = cornery1 + self.spacing

				if column == 1 or column == 20 or row == 1 or row == 20:

					ocolor = "khaki"
					fcolor = "khaki"
					tagger = "rim"

				else:

					fcolor = "beige"
					ocolor = "black"
					tagger = "celltags"

				self.canvas.create_rectangle(cornerx1,cornery1,cornerx2,cornery2,fill = fcolor,width = 1.75,tag = tagger,outline = ocolor)

				newpoint = (column,row)
				boardcoords.append(newpoint)

		self.canvas.tag_raise("celltags")

		return boardcoords

	def addPiece(self,column,row,turn):

		newpoint = (column,row)
		self.allpieces[newpoint] = turn
		self.plist = []

		for key in self.allpieces.keys():

			if self.allpieces[key] == turn:

				self.plist.append(key)

		self.count = 0

		if turn == "white":

			self.whitegroups = {}

		else:

			self.blackgroups = {}

		while len(self.plist) != 0:

			piece = self.plist[0]
			self.count += 1
			group = self.makeGroup(piece)

			if turn == "white":

				self.whitegroups[self.count] = group

			if turn == "black":

				self.blackgroups[self.count] = group

		self.count = 0

		

	def makeGroup(self,piece):

		xpiece = piece[0]
		ypiece = piece[1]
		group = [piece]
		self.plist.remove(piece)

		for item in self.liberties:

			xitem = item[0] + xpiece
			yitem = item[1] + ypiece
			newp = (xitem,yitem)

			if newp in self.plist:

				group = group + self.makeGroup(newp)

			else:

				continue

		return group


	def boardUpdate(self,groups):

		for key in groups.keys():
			
			self.checkLiberties(groups[key],key)


	def checkLiberties(self,group,key):

		surrounded = True

		for piece in group:

			xpiece = piece[0]
			ypiece = piece[1]

			for item in self.liberties:

				xitem = item[0] + xpiece
				yitem = item[1] + ypiece
				newp = (xitem,yitem)

				if newp in self.allpieces:

					continue

				elif not 1 <= xitem <= cells-2 or not 1 <= yitem <= cells-2:

					continue

				else:

					return

		for piece in group:

			del self.allpieces[piece]


	def click(self,event):

		self.count = 0
		xclick = event.x
		yclick = event.y
		column = round(xclick/self.spacing)
		row = round(yclick/self.spacing)

		if 1<= column <= cells- 2 and 1<= row <= cells - 2 and (column,row) not in self.allpieces.keys():

			self.addPiece(column,row,self.turn)

		else:

			return

		if self.turn == "white":

			self.turn = "black"
			groups = self.blackgroups

		elif self.turn == "black":

			self.turn = "white"
			groups = self.whitegroups

		self.boardUpdate(groups)
		self.canvas.delete("pieces")

		for key in self.allpieces.keys():

			color = self.allpieces[key]
			x1 = key[0] * self.spacing - (self.spacing/2)
			y1 = key[1] * self.spacing - (self.spacing/2)
			x2 = x1 + self.spacing
			y2 = y1 + self.spacing

			self.canvas.create_oval(x1,y1,x2,y2,fill = color,tag = "pieces")


	def animate(self):

		while True:

			self.canvas.update()


go = Board(cells,side,root)
go.drawBoard()
go.animate()
root.mainloop()
