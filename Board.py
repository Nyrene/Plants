from Plant import Plant
import Constants
import random


import curses

class Tile:
	plant = None

	#def display(self):
	#	if self.plant == None:
	#		#print("+", end=Constants.BOARD_SPACING)
	#		stdscr.addstr("." + Constants.BOARD_SPACING)
	#	else:
	#		self.plant.display()

	def getStr(self):
		if self.plant == None:
			return ("+" + Constants.BOARD_SPACING)
		else:
			return self.plant.getStr()




class Board:
	tiles = [[Tile() for i in range(Constants.BOARD_COLUMNS)] for j in range(Constants.BOARD_ROWS)]
	plants = []
	newPlants = [] # used and cleared on each step
	stdscr = None

	def __init__(self):
		#test placing a plant
		#self.tiles[Constants.BOARD_ROWS-3][Constants.BOARD_COLUMNS-2].plant = Plant()
		# text, background
		#curses.init_pair(1, plant, curses.COLOR_WHITE)
		self.placePlant(Plant(), Constants.BOARD_ROWS-3, Constants.BOARD_COLUMNS-2)


	def display(self):
		for row in range(Constants.BOARD_ROWS):
			for col in range(Constants.BOARD_COLUMNS):
				if col == 0:
					self.stdscr.addstr("\n")
				self.stdscr.addstr(self.tiles[row][col].getStr())


	def placePlant(self, newPlant, row, col):
		if newPlant != None:
			if row < Constants.BOARD_ROWS and col < Constants.BOARD_COLUMNS:
				self.tiles[col][row].plant = newPlant
				newPlant.setCoordinates(col, row)
				self.plants.append(newPlant)

			else:
				print("\nError: can't place plant at out of bounds location: " + str(row) + ", " + str(col))
		return



	def step(self):
		# for each plant on the board, call its step function
		# the plant step function doesn't do bounds checking or
		# checks for existing plants.

		# for overwriting plants: flowers don't override, but
		# weeds do. do we check type here?
		

		# refactor placePlant and this function to pass coords object directly
		for p in self.plants:
			newGrowthCoords = Plant(p).step()
			if newGrowthCoords != None:
				newPlant = Plant()
				self.placePlant(newPlant, newGrowthCoords.x, newGrowthCoords.y)
				self.newPlants.append(newPlant)


		# at the end, append all new plants to the main ones
		self.plants.append(self.newPlants)
		self.newPlants = []

		return


	def run(self, seconds=10):
		for i in range(seconds):
			self.stdscr.clear()
			self.step()
			self.display()
			self.stdscr.refresh()
			sleep(1)


		return





	def run1():
		return
		



